"""Individual Blender authoring scenes and the linked, combined animation library."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

import bpy
from bpy.app.handlers import persistent

SCRIPT_DIRECTORY = Path(__file__).resolve().parent.parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

DIRECTORY_PROPERTY = "animation_file_directory"
SOURCE_PROPERTY = "animation_file_source"
TEMPLATE_PROPERTY = "animation_file_template"
TRACKS_PROPERTY = "animation_file_tracks"
REFERENCES_PROPERTY = "animation_file_actions"
SHARED_FILENAME = "shared_scene_data.blend"
BAKED_SUFFIXES = (".baked", "_baked")
STRIP_PROPERTIES = (
    "action_frame_start", "action_frame_end", "scale", "repeat", "frame_start",
    "frame_end", "blend_type", "extrapolation", "use_animated_influence",
    "use_animated_time", "use_animated_time_cyclic", "strip_time", "influence",
    "blend_in", "blend_out", "use_auto_blend", "use_reverse", "use_sync_length", "mute",
)


def retrieve_project_directory(source):
    source = Path(source).resolve()
    return next((directory for directory in source.parents
                 if (directory / "package.json").is_file()), source.parent)


def retrieve_base_name(name):
    return next((name[:-len(suffix)] for suffix in BAKED_SUFFIXES
                 if name.endswith(suffix)), name)


def retrieve_owners():
    return [owner for owner in bpy.data.user_map()
            if hasattr(owner, "animation_data") and owner.is_editable and owner.animation_data]


class AnimationTracks:
    """Capture the native clip timing, action slots, and owner bindings."""

    def __init__(self):
        self.owners = retrieve_owners()
        self.tracks = []
        self.active = []
        for owner in self.owners:
            animation = owner.animation_data
            self.active.append((owner, animation.action, animation.action_slot))
            for track in animation.nla_tracks:
                strips = []
                for strip in track.strips:
                    if strip.type != "CLIP" or strip.fcurves or strip.modifiers:
                        raise ValueError(f"Use action clips for file splitting: {owner.name}/{track.name}")
                    if strip.action:
                        strips.append(dict(action=strip.action, slot=strip.action_slot,
                                           name=strip.name,
                                           properties={key: getattr(strip, key) for key in STRIP_PROPERTIES}))
                self.tracks.append((owner, track.name, track.mute, track.lock, strips))

    def clear(self):
        for owner in self.owners:
            animation = owner.animation_data
            animation.use_tweak_mode = False
            animation.action = None
            animation.use_nla = True
            for track in list(animation.nla_tracks):
                animation.nla_tracks.remove(track)

    def retrieve_bindings(self, actions):
        bindings = []
        for owner, name, muted, locked, strips in self.tracks:
            for strip in strips:
                if strip["action"] in actions:
                    bindings.append(dict(owner=owner.name, type=owner.id_type, track=name,
                                         action=strip["action"].name,
                                         slot=strip["slot"].identifier if strip["slot"] else "",
                                         properties=strip["properties"]))
        for owner, action, slot in self.active:
            if action in actions and not any(binding["owner"] == owner.name and binding["type"] == owner.id_type
                                             and binding["action"] == action.name for binding in bindings):
                start, end = action.frame_range
                bindings.append(dict(owner=owner.name, type=owner.id_type, track=action.name,
                                     action=action.name, slot=slot.identifier if slot else "",
                                     properties=dict(frame_start=start, frame_end=max(start + 1, end),
                                                     action_frame_start=start, action_frame_end=end,
                                                     use_sync_length=True)))
        return bindings

    def install(self, actions):
        self.clear()
        bindings = []
        for owner, name, muted, locked, strips in self.tracks:
            selected = [strip for strip in strips if strip["action"] in actions]
            if selected:
                track = owner.animation_data.nla_tracks.new()
                track.name, track.mute, track.lock = name, muted, locked
                for saved in selected:
                    strip = track.strips.new(saved["name"], int(saved["properties"]["frame_start"]), saved["action"])
                    if saved["slot"]:
                        strip.action_slot = saved["slot"]
                    for key, value in saved["properties"].items():
                        setattr(strip, key, value)
                    bindings.append(dict(owner=owner.name, type=owner.id_type, track=name,
                                         action=saved["action"].name,
                                         slot=saved["slot"].identifier if saved["slot"] else "",
                                         properties=saved["properties"]))
        for owner, action, slot in self.active:
            if action in actions:
                animation = owner.animation_data
                animation.action = action
                if slot:
                    animation.action_slot = slot
                if not any(binding["owner"] == owner.name and binding["type"] == owner.id_type
                           and binding["action"] == action.name for binding in bindings):
                    track = animation.nla_tracks.new()
                    track.name, track.mute = action.name, True
                    strip = track.strips.new(action.name, int(action.frame_range[0]), action)
                    if slot:
                        strip.action_slot = slot
                    bindings.append(dict(owner=owner.name, type=owner.id_type, track=action.name,
                                         action=action.name, slot=slot.identifier if slot else "",
                                         properties={key: getattr(strip, key) for key in STRIP_PROPERTIES}))
        return bindings


class AnimationFileSplitter:
    """Write action files that compose a shared, editable authoring scene at load."""

    def __init__(self, directory):
        self.directory = Path(directory).resolve()

    def split(self, names=None):
        from animation_editing import finish_tweaking
        from animation_viewport import AnimationViewport
        finish_tweaking(bpy.context)
        sources = {action.name: action for action in bpy.data.actions
                   if action.library is None and retrieve_base_name(action.name) == action.name}
        selected = sorted(sources if names is None else names)
        if set(selected) - sources.keys():
            raise ValueError("Choose authoring actions from this Blender scene")
        filenames = self._retrieve_filenames(selected)
        destinations = [self.directory / filename for filename in filenames.values()]
        if any(path.exists() for path in destinations):
            raise FileExistsError("Animation source files already exist; choose a fresh directory")
        self.directory.mkdir(parents=True, exist_ok=True)
        (self.directory / ".gdignore").touch()
        scene = bpy.context.scene
        tracks = AnimationTracks()
        bakery = [(item, item.Action) for item in getattr(scene, "GRT_Action_Bakery", [])]
        AnimationViewport.suspended += 1
        try:
            tracks.clear()
            for item, action in bakery:
                item.Action = None
            template = self.directory / SHARED_FILENAME
            if template.exists():
                raise FileExistsError("Shared scene data already exists; choose a fresh directory")
            bpy.data.libraries.write(str(template), {scene}, path_remap="RELATIVE_ALL", compress=True)
            for index, name in enumerate(selected, 1):
                action = sources[name]
                family = {candidate for candidate in bpy.data.actions if candidate.library is None
                          and retrieve_base_name(candidate.name) == name}
                action[TRACKS_PROPERTY] = json.dumps(tracks.retrieve_bindings(family))
                AnimationFileWriter().write(action, template, self.directory / filenames[name])
                print(f"Animation files: {index}/{len(selected)} {name}", flush=True)
        finally:
            AnimationViewport.suspended -= 1
        return destinations

    @staticmethod
    def _retrieve_filenames(names):
        result = {}
        used = set()
        for name in names:
            stem = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_") or "animation"
            if stem in used or stem == Path(SHARED_FILENAME).stem or stem.upper() in {
                    "CON", "PRN", "AUX", "NUL", *(f"COM{number}" for number in range(1, 10)),
                    *(f"LPT{number}" for number in range(1, 10))}:
                stem += "_" + hashlib.sha256(name.encode()).hexdigest()[:12]
            used.add(stem)
            result[name] = stem + ".blend"
        return result


class AnimationFileWriter:
    def write(self, action, template, destination):
        from animation_viewport import AnimationViewport
        destination = Path(destination).resolve()
        destination.parent.mkdir(parents=True, exist_ok=True)
        scene = bpy.context.scene
        family = {candidate for candidate in bpy.data.actions if candidate.library is None
                  and retrieve_base_name(candidate.name) == action.name}
        originals = {member: member.name for member in family}
        copies = set()
        descriptor = bpy.data.scenes.new("Animation file")
        AnimationViewport.suspended += 1
        try:
            bpy.context.window.scene = descriptor
            bpy.context.view_layer.update()
            descriptor.use_fake_user = True
            descriptor.render.fps, descriptor.render.fps_base = scene.render.fps, scene.render.fps_base
            descriptor[TEMPLATE_PROPERTY] = os.path.relpath(template, destination.parent).replace("\\", "/")
            descriptor[SOURCE_PROPERTY] = action.name
            descriptor.frame_start, descriptor.frame_end = (int(value) for value in action.frame_range)
            if action.get("animation_loop_end_exclusive", False):
                descriptor.frame_end -= 1
            for member, original_name in originals.items():
                member.name = original_name + "_split_source"
                duplicate = member.copy()
                duplicate.name = original_name
                duplicate['animation_frame_rate'] = [scene.render.fps, scene.render.fps_base]
                if member.asset_data:
                    duplicate.asset_mark()
                    for field in ("author", "description", "copyright", "license", "catalog_id"):
                        setattr(duplicate.asset_data, field, getattr(member.asset_data, field))
                    for tag in member.asset_data.tags:
                        if tag.name not in duplicate.asset_data.tags:
                            duplicate.asset_data.tags.new(tag.name)
                duplicate.use_fake_user = True
                copies.add(duplicate)
            AnimationFileReferences(copies).store()
            bpy.data.libraries.write(str(destination), {descriptor, *copies},
                                     path_remap="RELATIVE_ALL", compress=True)
        finally:
            bpy.context.window.scene = scene
            bpy.data.scenes.remove(descriptor)
            bpy.data.batch_remove(ids=copies)
            for member, original_name in originals.items():
                member.name = original_name
            AnimationViewport.suspended -= 1
        return destination


class AnimationFileReferences:
    FIELDS = {"animation_objects": ("object",),
              "animation_interactables": ("receiver", "contact_object")}

    def __init__(self, actions):
        import animation_objects
        import animation_interactables
        animation_objects.register_properties()
        animation_interactables.register_properties()
        self.actions = actions

    def store(self):
        for action in self.actions:
            for collection, fields in self.FIELDS.items():
                for choice in getattr(action, collection, []):
                    for field in fields:
                        obj = getattr(choice, field)
                        if obj:
                            choice[field + "_name"] = obj.name
                            setattr(choice, field, None)

    def restore(self, scene):
        for action in self.actions:
            for collection, fields in self.FIELDS.items():
                for choice in getattr(action, collection, []):
                    for field in fields:
                        name = choice.get(field + "_name")
                        if name:
                            setattr(choice, field, scene.objects.get(name))


def retrieve_choice_object(choice, field="object", scene=None):
    scene = scene or bpy.context.scene
    obj = getattr(choice, field, None)
    name = obj.name if obj else choice.get(field + "_name", "")
    return scene.objects.get(name) if name else None


class AnimationAuthoringScene:
    """Compose local working rigs using Blender's native runtime data flag."""

    @staticmethod
    def retrieve_descriptor():
        descriptor = next((scene for scene in bpy.data.scenes
                           if scene.get(TEMPLATE_PROPERTY) and not scene.is_runtime_data), None)
        if descriptor is None and bpy.data.filepath:
            source = Path(bpy.data.filepath).resolve()
            root = retrieve_project_directory(source)
            template = root / "animations" / SHARED_FILENAME
            action = bpy.data.actions.get(source.stem)
            if (len(bpy.context.scene.objects) == 0 and source.parent.name == "sources"
                    and source.is_relative_to(root / "animations")
                    and template.is_file() and action and action.library is None):
                descriptor = bpy.context.scene
                descriptor[TEMPLATE_PROPERTY] = os.path.relpath(template, source.parent).replace("\\", "/")
                descriptor[SOURCE_PROPERTY] = action.name
                descriptor.use_fake_user = True
        return descriptor

    @staticmethod
    def prepare():
        descriptor = AnimationAuthoringScene.retrieve_descriptor()
        if descriptor and not bpy.context.scene.is_runtime_data:
            directory = Path(bpy.data.filepath).resolve().parent
            for other in bpy.data.scenes:
                if other != descriptor and not other.is_runtime_data:
                    other.name = "Animation file startup"
            existing = set(bpy.data.user_map())
            template = directory / descriptor[TEMPLATE_PROPERTY]
            if not template.is_file():
                template = retrieve_project_directory(bpy.data.filepath) / "animations" / SHARED_FILENAME
                descriptor[TEMPLATE_PROPERTY] = os.path.relpath(template, directory).replace("\\", "/")
            with bpy.data.libraries.load(str(template), link=False) as (available, loaded):
                loaded.scenes = available.scenes
            scene = loaded.scenes[0]
            scene['animation_default_frame_rate'] = [scene.render.fps, scene.render.fps_base]
            scene.render.fps, scene.render.fps_base = descriptor.render.fps, descriptor.render.fps_base
            for owner in set(bpy.data.user_map()) - existing:
                if owner.library is None:
                    owner.is_runtime_data = True
            scene[SOURCE_PROPERTY] = descriptor[SOURCE_PROPERTY]
            scene[TEMPLATE_PROPERTY] = descriptor[TEMPLATE_PROPERTY]
            bpy.context.window.scene = scene
            actions = [action for action in bpy.data.actions if action.library is None]
            AnimationFileReferences(actions).restore(scene)
            for action in sorted(actions, key=lambda action: action.name.endswith(BAKED_SUFFIXES)):
                AnimationFileLibrary._install_bindings(action)
            name = descriptor[SOURCE_PROPERTY]
            action = bpy.data.actions.get(name)
            if action:
                action['animation_frame_rate'] = [descriptor.render.fps, descriptor.render.fps_base]
            binding = next((binding for binding in json.loads(action.get(TRACKS_PROPERTY, "[]"))
                            if binding["action"] == name), None) if action else None
            if action:
                from track_chooser import TrackChooser
                chooser = TrackChooser(scene)
                track = binding["track"] if binding else name
                if track in chooser.retrieve_tracks():
                    chooser.apply(track)
                else:
                    scene.frame_start = int(action.frame_range[0])
                    scene.frame_end = int(action.frame_range[1])
                    scene.frame_set(scene.frame_start)
            scene.tool_settings.use_keyframe_insert_auto = True


@persistent
def prepare_animation_file(*args):
    from animation_viewport import AnimationViewport
    AnimationViewport.suspended += 1
    try:
        AnimationAuthoringScene.prepare()
    finally:
        AnimationViewport.suspended -= 1


@persistent
def store_animation_file(*args):
    from animation_viewport import AnimationViewport
    scene = bpy.context.scene
    if scene and scene.is_runtime_data and scene.get(SOURCE_PROPERTY):
        actions = {action for action in bpy.data.actions if action.library is None}
        primary = scene[SOURCE_PROPERTY]
        if primary not in {action.name for action in actions}:
            from animation_participants import retrieve_active_action
            active = retrieve_active_action(bpy.context)
            if active:
                primary = retrieve_base_name(active.name)
                scene[SOURCE_PROPERTY] = primary
                for descriptor in bpy.data.scenes:
                    if descriptor.get(TEMPLATE_PROPERTY) and not descriptor.is_runtime_data:
                        descriptor[SOURCE_PROPERTY] = primary
        for action in actions:
            action.is_runtime_data = retrieve_base_name(action.name) != primary
        actions = {action for action in actions if not action.is_runtime_data}
        if retrieve_base_name(scene.get("Track Chooser Selection", primary)) == primary:
            for action in actions:
                action['animation_frame_rate'] = [scene.render.fps, scene.render.fps_base]
            for descriptor in bpy.data.scenes:
                if descriptor.get(TEMPLATE_PROPERTY) and not descriptor.is_runtime_data:
                    descriptor.render.fps, descriptor.render.fps_base = scene.render.fps, scene.render.fps_base
        snapshot = AnimationTracks()
        for action in actions:
            family = {candidate for candidate in actions if retrieve_base_name(candidate.name) == action.name}
            if retrieve_base_name(action.name) == action.name:
                action[TRACKS_PROPERTY] = json.dumps(snapshot.retrieve_bindings(family))
            action.use_fake_user = True
        AnimationViewport.suspended += 1
        try:
            AnimationFileReferences(actions).store()
        finally:
            AnimationViewport.suspended -= 1


@persistent
def restore_animation_file(*args):
    from animation_viewport import AnimationViewport
    scene = bpy.context.scene
    if scene and scene.is_runtime_data and scene.get(SOURCE_PROPERTY):
        for action in bpy.data.actions:
            if action.library is None:
                action.is_runtime_data = False
        AnimationViewport.suspended += 1
        try:
            AnimationFileReferences([action for action in bpy.data.actions if action.library is None]).restore(scene)
        finally:
            AnimationViewport.suspended -= 1


class AnimationFileLibrary:
    def __init__(self, directory):
        self.directory = Path(directory).resolve()

    def link(self, paths=None):
        from animation_viewport import AnimationViewport
        from animation_editing import finish_tweaking
        finish_tweaking(bpy.context)
        AnimationViewport.suspended += 1
        try:
            targets = {action.name: action for action in bpy.data.actions if action.library is None
                       or Path(bpy.path.abspath(action.library.filepath)).resolve().is_relative_to(self.directory)}
            local_ids = {(owner.id_type, owner.name): owner for owner in bpy.data.user_map()
                         if owner.library is None}
            paths = sorted(path for path in self.directory.rglob("sources/*.blend") if path.name != SHARED_FILENAME) if paths is None else paths
            for index, path in enumerate(paths, 1):
                missing = {action.name[len(retrieve_base_name(action.name)):]: action
                           for action in targets.values() if action.is_missing and action.library
                           and Path(bpy.path.abspath(action.library.filepath)).resolve() == path.resolve()}
                with bpy.data.libraries.load(str(path), link=True) as (available, loaded):
                    loaded.actions = available.actions
                for action in loaded.actions:
                    action.library.filepath = bpy.path.relpath(str(path))
                for action in loaded.actions:
                    suffix = action.name[len(retrieve_base_name(action.name)):]
                    previous = missing.get(suffix) or targets.get(action.name)
                    if previous and previous != action:
                        targets.pop(previous.name, None)
                        self._replace_action(previous, action)
                    targets[action.name] = action
                for action in sorted(loaded.actions, key=lambda action: action.name.endswith(BAKED_SUFFIXES)):
                    self._install_bindings(action, local_ids)
                print(f"Animation library: {index}/{len(paths)} {path.name}", flush=True)
            bpy.context.scene[DIRECTORY_PROPERTY] = bpy.path.relpath(str(self.directory))
            references = [action for action in bpy.data.actions if action.library
                          and Path(bpy.path.abspath(action.library.filepath)).resolve().is_relative_to(self.directory)]
            # ID-property keys have a shorter limit than Blender action names.
            bpy.context.scene[REFERENCES_PROPERTY] = {str(index): action for index, action in enumerate(references)}
        finally:
            AnimationViewport.suspended -= 1

    @staticmethod
    def _replace_action(previous, action):
        if previous.name != action.name:
            for owner in retrieve_owners():
                for track in owner.animation_data.nla_tracks:
                    if any(strip.action == previous for strip in track.strips):
                        if track.name == previous.name:
                            track.name = action.name
                        for strip in track.strips:
                            if strip.action == previous and strip.name == previous.name:
                                strip.name = action.name
            for scene in bpy.data.scenes:
                if scene.get("Track Chooser Selection") == previous.name:
                    scene["Track Chooser Selection"] = action.name
        previous.user_remap(action)
        bpy.data.actions.remove(previous)

    @staticmethod
    def _install_bindings(action, owners=None):
        owners = owners if owners is not None else {
            (owner.id_type, owner.name): owner for owner in bpy.data.user_map() if owner.library is None}
        bindings = json.loads(action.get(TRACKS_PROPERTY, "[]"))
        explicit_bindings = bool(bindings)
        if not bindings:
            start, end = action.frame_range
            bindings = [dict(owner=slot.name_display, type=slot.target_id_type, track=action.name,
                             action=action.name, slot=slot.identifier,
                             properties=dict(frame_start=start, frame_end=max(start + 1, end),
                                             action_frame_start=start, action_frame_end=end, use_sync_length=True))
                        for slot in action.slots]
        for binding in bindings:
            owner = owners.get((binding["type"], binding["owner"]))
            bound_action = next((candidate for candidate in bpy.data.actions
                                 if candidate.library == action.library and candidate.name == binding["action"]), None)
            if owner and bound_action:
                animation = owner.animation_data_create()
                existing = any((track.name == binding["track"] or not explicit_bindings)
                               and any(strip.action == bound_action for strip in track.strips)
                               for track in animation.nla_tracks)
                if not existing:
                    track = animation.nla_tracks.new()
                    track.name, track.mute = binding["track"], True
                    strip = track.strips.new(bound_action.name, int(binding["properties"]["frame_start"]), bound_action)
                    if binding["slot"]:
                        strip.action_slot = next(slot for slot in bound_action.slots if slot.identifier == binding["slot"])
                    for key, value in binding["properties"].items():
                        setattr(strip, key, value)


@persistent
def discover_animation_files(*args):
    scene = bpy.context.scene
    if scene and scene.get(DIRECTORY_PROPERTY):
        directory = Path(bpy.path.abspath(scene[DIRECTORY_PROPERTY])).resolve()
        loaded = {}
        for action in bpy.data.actions:
            if action.library:
                path = Path(bpy.path.abspath(action.library.filepath)).resolve()
                loaded.setdefault(path, set()).add(action.name)
        paths = set() if scene.get('animation_library_lazy') else {path for path in directory.rglob("sources/*.blend") if path.name != SHARED_FILENAME and path not in loaded}
        for action in bpy.data.actions:
            if action.library:
                path = Path(bpy.path.abspath(action.library.filepath)).resolve()
                if path.is_relative_to(directory) and (action.is_missing or any(
                        binding["action"] not in loaded[path]
                        for binding in json.loads(action.get(TRACKS_PROPERTY, "[]")))):
                    paths.add(path)
        if paths:
            AnimationFileLibrary(directory).link(sorted(paths))


@persistent
def remap_animation_dependencies(*args):
    scene = getattr(bpy.context, "scene", None)
    if scene and scene.get(DIRECTORY_PROPERTY):
        directory = Path(bpy.path.abspath(scene[DIRECTORY_PROPERTY])).resolve()
        targets = {(owner.id_type, owner.name): owner for owner in bpy.data.user_map() if owner.library is None}
        for owner in list(bpy.data.user_map()):
            if owner.library and Path(bpy.path.abspath(owner.library.filepath)).resolve().is_relative_to(directory):
                target = targets.get((owner.id_type, owner.name))
                if target and not isinstance(owner, bpy.types.Action):
                    owner.user_remap(target)


class AnimationFileWindow:
    """Open an authoring window with the checkout's animation and export helpers."""

    def open(self, source):
        startup = Path(__file__).parent.parent / "open_studio.py"
        return subprocess.Popen(
            [bpy.app.binary_path, "--factory-startup", str(source), "--python", str(startup)],
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)


class ANIMATION_OT_open_source_file(bpy.types.Operator):
    bl_idname = "animation.open_source_file"
    bl_label = "Edit animation file"
    bl_description = "Open this animation's source in a separate Blender window"

    @classmethod
    def poll(cls, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        return bool(action and action.library)

    def execute(self, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        AnimationFileWindow().open(bpy.path.abspath(action.library.filepath))
        return {"FINISHED"}


class ANIMATION_OT_save_source_file(bpy.types.Operator):
    bl_idname = "animation.save_source_file"
    bl_label = "Save animation as file"
    bl_description = "Save the active animation as its own source file and open a separate Blender window"

    @classmethod
    def poll(cls, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        return bool(action and action.is_editable and
                    (context.scene.get(TEMPLATE_PROPERTY) or context.scene.get(DIRECTORY_PROPERTY)))

    def execute(self, context):
        from animation_participants import retrieve_active_action
        action = retrieve_active_action(context)
        if context.scene.get(DIRECTORY_PROPERTY):
            directory = Path(bpy.path.abspath(context.scene[DIRECTORY_PROPERTY])).resolve()
            template = directory / SHARED_FILENAME
        else:
            template = Path(bpy.data.filepath).resolve().parent / context.scene[TEMPLATE_PROPERTY]
            directory = template.parent
        filename = AnimationFileSplitter._retrieve_filenames([action.name])[action.name]
        from import_assets import style_for
        style = style_for(action.name) or "freestyle"
        destination = retrieve_project_directory(bpy.data.filepath) / "animations" / style / "sources" / filename
        if destination.exists():
            self.report({"ERROR"}, "Choose a distinct animation name for the new file")
            return {"CANCELLED"}
        family = {candidate for candidate in bpy.data.actions if candidate.library is None
                  and retrieve_base_name(candidate.name) == action.name}
        action[TRACKS_PROPERTY] = json.dumps(AnimationTracks().retrieve_bindings(family))
        AnimationFileWriter().write(action, template, destination)
        AnimationFileWindow().open(destination)
        self.report({"INFO"}, f"Saved {destination.name}")
        return {"FINISHED"}


def register():
    if bpy.types.Operator.bl_rna_get_subclass_py("ANIMATION_OT_open_source_file") is None:
        bpy.utils.register_class(ANIMATION_OT_open_source_file)
    if bpy.types.Operator.bl_rna_get_subclass_py("ANIMATION_OT_save_source_file") is None:
        bpy.utils.register_class(ANIMATION_OT_save_source_file)
    if remap_animation_dependencies not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.insert(0, remap_animation_dependencies)
    for handlers, handler in ((bpy.app.handlers.load_post, prepare_animation_file),
                              (bpy.app.handlers.load_post, discover_animation_files),
                              (bpy.app.handlers.save_pre, store_animation_file),
                              (bpy.app.handlers.save_post, restore_animation_file)):
        if handler not in handlers:
            handlers.append(handler)
    remap_animation_dependencies()


def unregister():
    for handlers, handler in ((bpy.app.handlers.load_post, prepare_animation_file),
                              (bpy.app.handlers.load_post, discover_animation_files),
                              (bpy.app.handlers.save_pre, store_animation_file),
                              (bpy.app.handlers.save_post, restore_animation_file)):
        if handler in handlers:
            handlers.remove(handler)
    if remap_animation_dependencies in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(remap_animation_dependencies)
    bpy.utils.unregister_class(ANIMATION_OT_open_source_file)
    bpy.utils.unregister_class(ANIMATION_OT_save_source_file)
