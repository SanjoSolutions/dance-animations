"""Build native, ordered hand-contact stages in the open Blender character file."""

import bpy
from mathutils import Matrix


CHARACTERS = {
    "Man": "Man.body",
    "Woman": "Woman.body",
}
CONTACT_CONSTRAINTS = {"Palm Contact Wrist", "Finger Surface Rotation", "Natural Wrist Rotation"}
ORDER_PROPERTY = "Contact Order"
STAGE_COLLECTION = "Contact Evaluation Stages"


def retrieve_owners(obj):
    return [obj, *obj.pose.bones] if obj.type == "ARMATURE" else [obj]


class PropertyLink:
    @staticmethod
    def copy_constraint(source, owner, name):
        result = owner.constraints.new(source.type)
        result.name = name
        for prop in source.bl_rna.properties:
            if prop.identifier not in {"rna_type", "name", "type"} and not prop.is_readonly:
                setattr(result, prop.identifier, getattr(source, prop.identifier))
        animation = source.id_data.animation_data
        driver = animation.drivers.find(source.path_from_id("influence")) if animation else None
        if driver:
            PropertyLink.copy_driver(driver, result, "influence")
        return result

    @staticmethod
    def expression(driver):
        names = [variable.name for variable in driver.variables]
        if driver.type == "SCRIPTED":
            result = driver.expression
        elif driver.type == "AVERAGE":
            result = "(" + " + ".join(names) + f") / {len(names)}"
        elif driver.type == "SUM":
            result = " + ".join(names)
        else:
            result = driver.type.lower() + "(" + ", ".join(names) + ")"
        return result

    @staticmethod
    def copy_driver(source, owner, path):
        result = owner.driver_add(path)
        result.driver.type = source.driver.type
        result.driver.expression = source.driver.expression
        result.driver.use_self = source.driver.use_self
        for variable in source.driver.variables:
            copied = result.driver.variables.new()
            copied.name = variable.name
            copied.type = variable.type
            for target, copied_target in zip(variable.targets, copied.targets):
                copied_target.id_type = target.id_type
                copied_target.id = target.id
                for name in ("data_path", "bone_target", "transform_type", "transform_space", "rotation_mode"):
                    setattr(copied_target, name, getattr(target, name))
        return result

    @staticmethod
    def bind(owner, property_path, source, source_path, index=None):
        curve = owner.driver_add(property_path) if index is None else owner.driver_add(property_path, index)
        driver = curve.driver
        driver.type = "SCRIPTED"
        for variable in list(driver.variables):
            driver.variables.remove(variable)
        variable = driver.variables.new()
        variable.name = "value"
        variable.type = "SINGLE_PROP"
        variable.targets[0].id_type = source.id_type
        variable.targets[0].id = source
        variable.targets[0].data_path = source_path
        driver.expression = "value"

    @staticmethod
    def follow_pose(source, destination):
        driven = {(curve.data_path, curve.array_index) for curve in destination.animation_data.drivers}
        for bone in destination.pose.bones:
            source_bone = source.pose.bones[bone.name]
            direct_deform_control = bone.name.startswith("DEF-") and len(source_bone.constraints) == 0
            if direct_deform_control or not bone.name.startswith(("DEF-", "ORG-", "MCH-", "VIS_")):
                rotation = {"QUATERNION": "rotation_quaternion", "AXIS_ANGLE": "rotation_axis_angle"}.get(bone.rotation_mode, "rotation_euler")
                for property_name in ("location", rotation, "scale"):
                    path = bone.path_from_id(property_name)
                    for index in range(len(getattr(bone, property_name))):
                        if (path, index) not in driven:
                            PropertyLink.bind(bone, property_name, source, f"{path}[{index}]", index)
            for name, value in source_bone.items():
                if isinstance(value, (int, float)):
                    property_path = f'["{bpy.utils.escape_identifier(name)}"]'
                    path = source_bone.path_from_id() + property_path
                    if (path, 0) not in driven:
                        PropertyLink.bind(bone, property_path, source, path)


class ObjectCopies:
    def __init__(self, collection, parent):
        self.collection = collection
        self.parent = parent

    def create(self, source, name):
        result = source.copy()
        result.name = name
        if source.type == "ARMATURE":
            result.data = source.data.copy()
        if result.animation_data:
            result.animation_data.use_tweak_mode = False
            result.animation_data.action = None
            for track in list(result.animation_data.nla_tracks):
                result.animation_data.nla_tracks.remove(track)
        self.collection.objects.link(result)
        result.hide_render = True
        result.hide_set(True)
        result.hide_select = True
        return result

    def remap(self, obj, mapping):
        if obj.parent in mapping:
            obj.parent = mapping[obj.parent]
        elif obj.parent is None:
            obj.parent = self.parent
            obj.matrix_parent_inverse = Matrix.Identity(4)
        for owner in retrieve_owners(obj):
            for constraint in owner.constraints:
                self.remap_pointers(constraint, mapping)
                if hasattr(constraint, "targets"):
                    for target in constraint.targets:
                        self.remap_pointers(target, mapping)
        for modifier in obj.modifiers:
            self.remap_pointers(modifier, mapping)
        for owner in (obj, obj.data):
            if owner and owner.animation_data:
                for curve in owner.animation_data.drivers:
                    for variable in curve.driver.variables:
                        for target in variable.targets:
                            if target.id in mapping:
                                target.id = mapping[target.id]

    @staticmethod
    def remap_pointers(owner, mapping):
        for prop in owner.bl_rna.properties:
            if prop.type == "POINTER" and not prop.is_readonly:
                value = getattr(owner, prop.identifier)
                if isinstance(value, bpy.types.ID) and value in mapping:
                    setattr(owner, prop.identifier, mapping[value])


class ContactStage:
    def __init__(self, character, name, source, helpers, copies):
        self.character = character
        self.rig = copies.create(source, f"{character}.Contact{name}-noimp")
        self.rig["Contact Input"] = source
        self.objects = {source: self.rig}
        for helper in helpers:
            self.objects[helper] = copies.create(helper, f"{helper.name}.Contact{name}-noimp")
        for obj in self.objects.values():
            copies.remap(obj, self.objects)
        transform = self.rig.constraints.new("COPY_TRANSFORMS")
        transform.name = "Follow Source Object"
        transform.target = source
        PropertyLink.follow_pose(source, self.rig)
        self.helpers = [self.objects[helper] for helper in helpers]
        for side in ("L", "R"):
            helper = self.objects[bpy.data.objects[f"{character}.PalmContact.{side}"]]
            PropertyLink.bind(helper, '["Finger Contact"]', source, f'pose.bones["hand_ik.{side}"]["Finger Contact"]')

    def target(self, body):
        for obj in self.helpers:
            for constraint in obj.constraints:
                if constraint.type == "SHRINKWRAP":
                    constraint.target = body


class ContactOrderInstaller:
    def __init__(self):
        self.scene = bpy.context.scene

    def install(self):
        if STAGE_COLLECTION in bpy.data.collections:
            raise RuntimeError("Contact stages are already installed in this file")
        collection = bpy.data.collections.new(STAGE_COLLECTION)
        self.scene.collection.children.link(collection)
        root = bpy.data.objects.new("ContactStages-noimp", None)
        collection.objects.link(root)
        root.hide_render = True
        root.hide_set(True)
        copies = ObjectCopies(collection, root)
        sources = {name: bpy.data.objects[f"{name}.rigify"] for name in CHARACTERS}
        for source in sources.values():
            for bone in source.pose.bones:
                for constraint in list(bone.constraints):
                    target = getattr(constraint, "target", None)
                    if constraint.mute and target and target.type == "MESH":
                        constraint.driver_remove("influence")
                        bone.constraints.remove(constraint)
        helper_sets = {
            name: [obj for obj in bpy.data.objects if obj.type == "EMPTY" and obj.name.startswith(name + ".")]
            for name in CHARACTERS
        }
        for name, source in sources.items():
            for side in ("L", "R"):
                bone = source.pose.bones[f"hand_ik.{side}"]
                bone["Finger Contact"] = float(bpy.data.objects[f"{name}.PalmContact.{side}"]["Finger Contact"])
                bone.id_properties_ui("Finger Contact").update(
                    min=0.0, max=1.0, default=1.0,
                    description="Blend authored finger poses with finger surface contact",
                )
        stages = {
            name: {stage: ContactStage(name, stage, source, helper_sets[name], copies) for stage in ("First", "Final")}
            for name, source in sources.items()
        }
        surfaces = {
            name: {
                stage: self.create_surface(name, stage, source, copies)
                for stage, source in (("Base", sources[name]), ("First", stages[name]["First"].rig))
            }
            for name in CHARACTERS
        }
        self.scene[ORDER_PROPERTY] = 0
        self.scene.id_properties_ui(ORDER_PROPERTY).update(
            min=0, max=1, default=0,
            description="0: Man first, Woman follows. 1: Woman first, Man follows.",
            items=[("MAN_FIRST", "Man first", "Man contacts Woman's base pose; Woman follows Man's result", 0),
                   ("WOMAN_FIRST", "Woman first", "Woman contacts Man's base pose; Man follows Woman's result", 1)],
        )
        for index, (name, source) in enumerate(sources.items()):
            other = "Woman" if name == "Man" else "Man"
            stages[name]["First"].target(surfaces[other]["Base"])
            final = stages[name]["Final"]
            final.target(surfaces[other]["Base"])
            for helper in final.helpers:
                self.add_ordered_targets(helper, surfaces[other]["First"], index)
            deform = bpy.data.objects[f"{name}.rigify_deform"]
            for bone in deform.pose.bones:
                for constraint in bone.constraints:
                    if getattr(constraint, "target", None) == source:
                        constraint.target = final.rig
            self.remove_source_contact(source)
            for helper in helper_sets[name]:
                bpy.data.objects.remove(helper, do_unlink=True)
            source["Contact First Stage"] = stages[name]["First"].rig
            source["Contact Final Stage"] = final.rig
            self.update_panel(source)
        self.write_instructions()
        for keying_set in self.scene.keying_sets:
            if keying_set.bl_label == "Source Rigs":
                keying_set.paths.add(self.scene, f'["{ORDER_PROPERTY}"]', group_method="NAMED", group_name=ORDER_PROPERTY)
        self.scene["Contact Stages Version"] = 1
        bpy.context.view_layer.update()
        return stages

    def create_surface(self, character, stage, rig, copies):
        deform_source = bpy.data.objects[f"{character}.rigify_deform"]
        deform = copies.create(deform_source, f"{character}.Contact{stage}Deform-noimp")
        body_source = bpy.data.objects[CHARACTERS[character]]
        body = copies.create(body_source, f"{character}.Contact{stage}Body-noimp")
        mapping = {bpy.data.objects[f"{character}.rigify"]: rig, deform_source: deform, body_source: body}
        copies.remap(deform, mapping)
        copies.remap(body, mapping)
        return body

    def add_ordered_targets(self, helper, first_surface, first_order):
        for constraint in list(helper.constraints):
            if constraint.type == "SHRINKWRAP":
                alternative = PropertyLink.copy_constraint(constraint, helper, constraint.name + " - Following")
                alternative.target = first_surface
                index = list(helper.constraints).index(constraint)
                helper.constraints.move(len(helper.constraints) - 1, index + 1)
                self.order_influence(constraint, first_order)
                self.order_influence(alternative, 1 - first_order)

    def order_influence(self, constraint, order):
        influence = constraint.influence
        path = constraint.path_from_id("influence")
        animation = constraint.id_data.animation_data
        existing = animation.drivers.find(path) if animation else None
        curve = existing or constraint.driver_add("influence")
        expression = PropertyLink.expression(existing.driver) if existing else repr(influence)
        variable = curve.driver.variables.new()
        variable.name = "contact_order"
        variable.type = "SINGLE_PROP"
        variable.targets[0].id_type = "SCENE"
        variable.targets[0].id = self.scene
        variable.targets[0].data_path = f'["{ORDER_PROPERTY}"]'
        curve.driver.type = "SCRIPTED"
        curve.driver.expression = f"({expression}) if contact_order == {order} else 0.0"

    @staticmethod
    def remove_source_contact(rig):
        for bone in rig.pose.bones:
            for constraint in list(bone.constraints):
                if constraint.name in CONTACT_CONSTRAINTS:
                    constraint.driver_remove("influence")
                    bone.constraints.remove(constraint)

    @staticmethod
    def update_panel(rig):
        text = rig["rig_ui"]
        source = text.as_string()
        anchor = "        layout = self.layout"
        row = '        layout.prop(context.scene, \'["Contact Order"]\', text="Contact Order")'
        assert anchor in source, text.name
        if row not in source:
            source = source.replace(anchor, anchor + "\n" + row, 1)
        for side in ("L", "R"):
            slider = f'            layout.prop(pose_bones[\'hand_ik.{side}\'], \'["Surface Contact"]\', text=\'Surface Contact ({side})\', slider=True)'
            finger_slider = f'            layout.prop(pose_bones[\'hand_ik.{side}\'], \'["Finger Contact"]\', text=\'Finger Contact ({side})\', slider=True)'
            assert slider in source, text.name
            if finger_slider not in source:
                source = source.replace(slider, slider + "\n" + finger_slider)
        compile(source, text.name, "exec")
        text.from_string(source)

    @staticmethod
    def write_instructions():
        text = bpy.data.texts.get("Contact Order - Instructions") or bpy.data.texts.new("Contact Order - Instructions")
        text.from_string(
            "Contact Order\n\n"
            "Select either source rig and use Item > Rig Main Properties > Contact Order.\n"
            "Man first: Man contacts Woman's base pose; Woman contacts Man's resulting pose.\n"
            "Woman first: Woman contacts Man's base pose; Man contacts Woman's resulting pose.\n"
            "Right-click Contact Order > Insert Keyframe. Use Constant interpolation for switches.\n"
            "The shared property belongs to the Scene and follows the scene timeline.\n"
            "Pose and animate the original Rigify controls and Surface Contact sliders as usual.\n"
            "Finger Contact on each hand controls its finger contribution in both stages.\n"
            "The visible deform rigs display the final contact result.\n"
            "Contact Evaluation Stages contains hidden full-body evaluation surfaces and rigs.\n"
            "Native constraints and drivers evaluate Base, First, Final in that order.\n"
            "The -noimp hierarchy keeps evaluation helpers out of Godot scenes.\n"
        )
        for character in CHARACTERS:
            existing = bpy.data.texts[f"{character} Palm Contacts - Instructions"]
            existing.from_string(text.as_string())


if __name__ == "__main__":
    ContactOrderInstaller().install()
    print("Installed keyframeable Contact Order")
