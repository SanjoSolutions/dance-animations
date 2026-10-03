"""Reuse sampled glTF clips while Blender evaluates the complete source scene."""

from contextlib import contextmanager
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import struct
import sys
from types import ModuleType

import bpy

from animation_export_evaluation import AnimationExportEvaluation


class AnimationDocument:
    def __init__(self, contents):
        magic, version, length = struct.unpack_from("<III", contents)
        if (magic, version, length) != (0x46546C67, 2, len(contents)):
            raise ValueError("Expected a complete GLB version 2 document")
        size, kind = struct.unpack_from("<II", contents, 12)
        if kind != 0x4E4F534A:
            raise ValueError("Expected a GLB JSON chunk")
        self.document = json.loads(contents[20:20 + size])
        offset = 20 + size
        self.binary = bytearray()
        if offset < len(contents):
            size, kind = struct.unpack_from("<II", contents, offset)
            if kind != 0x004E4942:
                raise ValueError("Expected a GLB binary chunk")
            self.binary.extend(contents[offset + 8:offset + 8 + size])

    def retrieve_node_paths(self):
        return self._retrieve_paths(lambda index, node: node.get("name", ""))

    def retrieve_node_keys(self):
        joints = {joint for skin in self.document.get("skins", []) for joint in skin["joints"]}
        paths = self._retrieve_paths(lambda index, node: (
            node.get("name", ""), "joint" if index in joints else "mesh" if "mesh" in node else "node",
        ))
        if len(paths) != len(set(paths)):
            raise ValueError("Animation nodes require distinct names within their roles")
        return paths

    def _retrieve_paths(self, retrieve_segment):
        nodes = self.document.get("nodes", [])
        parents = {child: index for index, node in enumerate(nodes) for child in node.get("children", [])}

        def path(index):
            name = retrieve_segment(index, nodes[index])
            return (*path(parents[index]), name) if index in parents else (name,)

        return [path(index) for index in range(len(nodes))]

    def reuse(self, previous, names):
        source_paths = previous.retrieve_node_keys()
        targets = {path: index for index, path in enumerate(self.retrieve_node_keys())}
        accessors = {}
        views = {}

        def copy_view(index):
            if index not in views:
                view = deepcopy(previous.document["bufferViews"][index])
                if view.get("buffer", 0) != 0:
                    raise ValueError("Animation buffers belong to the GLB")
                offset = view.get("byteOffset", 0)
                self.binary.extend(b"\0" * (-len(self.binary) % 4))
                view["byteOffset"] = len(self.binary)
                self.binary.extend(previous.binary[offset:offset + view["byteLength"]])
                view["buffer"] = 0
                views[index] = len(self.document.setdefault("bufferViews", []))
                self.document["bufferViews"].append(view)
            return views[index]

        def copy_accessor(index):
            if index not in accessors:
                accessor = deepcopy(previous.document["accessors"][index])
                if "bufferView" in accessor:
                    accessor["bufferView"] = copy_view(accessor["bufferView"])
                if "sparse" in accessor:
                    for part in ("indices", "values"):
                        item = accessor["sparse"][part]
                        item["bufferView"] = copy_view(item["bufferView"])
                accessors[index] = len(self.document.setdefault("accessors", []))
                self.document["accessors"].append(accessor)
            return accessors[index]

        for original in previous.document.get("animations", []):
            if original["name"] in names:
                animation = deepcopy(original)
                for channel in animation["channels"]:
                    target = channel["target"]
                    target["node"] = targets[source_paths[target["node"]]]
                for sampler in animation["samplers"]:
                    for key in ("input", "output"):
                        sampler[key] = copy_accessor(sampler[key])
                self.document.setdefault("animations", []).append(animation)

    def retain(self, names):
        self.document["animations"] = [clip for clip in self.document.get("animations", []) if clip["name"] in names]

    def append_values(self, values, bounds=False):
        contents = struct.pack("<" + "f" * len(values), *values)
        self.binary.extend(b"\0" * (-len(self.binary) % 4))
        accessor = dict(bufferView=len(self.document["bufferViews"]), componentType=5126,
                        count=len(values), type="SCALAR")
        if bounds:
            accessor.update(min=[min(values)], max=[max(values)])
        self.document["bufferViews"].append(dict(buffer=0, byteOffset=len(self.binary), byteLength=len(contents)))
        self.binary.extend(contents)
        index = len(self.document["accessors"])
        self.document["accessors"].append(accessor)
        return index

    def retrieve_bytes(self):
        animations = self.document.pop("animations", [])
        if animations:
            self.document["animations"] = sorted(animations, key=lambda clip: clip["name"])
        self.document["buffers"] = [{"byteLength": len(self.binary)}]
        document = json.dumps(self.document, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        document += b" " * (-len(document) % 4)
        binary = bytes(self.binary) + b"\0" * (-len(self.binary) % 4)
        return (struct.pack("<IIIII", 0x46546C67, 2, 28 + len(document) + len(binary), len(document), 0x4E4F534A)
                + document + struct.pack("<II", len(binary), 0x004E4942) + binary)


class AnimationExportCache:
    def __init__(self, output, signatures):
        self.destination = Path(output) / "animations.glb"
        self.manifest = Path(output) / ".animation_cache" / "manifest.json"
        self.signatures = signatures
        self.previous = None
        self.reused = set()
        self.current = False
        try:
            saved = json.loads(self.manifest.read_text(encoding="utf-8"))
            if not isinstance(saved, dict) or not isinstance(saved.get("clips"), dict):
                raise ValueError("Expected clip signatures")
            contents = self.destination.read_bytes()
            if saved["digest"] == hashlib.sha256(contents).hexdigest():
                self.previous = AnimationDocument(contents)
                available = {clip["name"] for clip in self.previous.document.get("animations", [])}
                self.reused = {name for name, signature in signatures.items()
                               if saved["clips"].get(name) == signature and name in available}
                self.current = saved["clips"] == signatures and self.reused == set(signatures)
        except (OSError, ValueError, KeyError, TypeError, struct.error):
            self.previous = None
            self.reused = set()
            self.current = False
        self.changed = set(signatures) - self.reused

    @contextmanager
    def select_tracks(self, report_progress=print):
        changed = self.changed
        evaluation = AnimationExportEvaluation(bpy.context.selected_objects)

        class ClipSelection:
            def __init__(self):
                self.skipped = {}

            def gather_scene_hook(self, scene, blender_scene, export_settings):
                evaluation.prepare()

            def pre_animation_track_switch_hook(self, blender_object, track, name, kind, export_settings):
                report_progress(f"Sampling {blender_object.name}: {name}")

            def gather_gltf_hook(self, active_scene, scenes, animations, export_settings):
                evaluation.restore()
                report_progress("Writing animation GLB...")

            def gather_tracks_hook(self, blender_object, tracks_data, export_settings):
                skipped = []
                for group in tracks_data.tracks:
                    if group.name not in changed:
                        owner = blender_object if group.on_type == "OBJECT" else blender_object.data.shape_keys
                        skipped.extend(owner.animation_data.nla_tracks[track.idx] for track in group.tracks)
                self.skipped[blender_object] = [(track, track.mute) for track in skipped]
                tracks_data.tracks[:] = [track for track in tracks_data.tracks if track.name in changed]

            def animation_track_switch_loop_hook(self, blender_object, completed, export_settings):
                for track, muted in self.skipped.get(blender_object, []):
                    track.mute = muted if completed else True

        # Blender discovers export extensions through enabled add-on modules.
        name = "player_assets_clip_selection"
        module = ModuleType(name)
        module.glTF2ExportUserExtension = ClipSelection
        sys.modules[name] = module
        addon = bpy.context.preferences.addons.new()
        addon.module = name
        try:
            yield
        finally:
            evaluation.restore()
            bpy.context.preferences.addons.remove(addon)
            del sys.modules[name]

    def combine(self, contents):
        current = AnimationDocument(contents)
        if self.reused:
            current.reuse(self.previous, self.reused)
        return current.retrieve_bytes()

    def retrieve_pruned(self):
        self.previous.retain(self.signatures)
        return self.previous.retrieve_bytes()

    def store(self):
        contents = self.destination.read_bytes()
        self.manifest.parent.mkdir(parents=True, exist_ok=True)
        staging = self.manifest.with_suffix(".pending")
        scene = bpy.context.scene
        staging.write_text(json.dumps({"clips": self.signatures, "digest": hashlib.sha256(contents).hexdigest(),
                                       "frame_rate": scene.render.fps / scene.render.fps_base}),
                           encoding="utf-8")
        staging.replace(self.manifest)
