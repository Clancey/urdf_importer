#!/usr/bin/python3

import bpy
from bpy_extras.io_utils import ImportHelper

from .robot_builder import RobotBuilder


def read_data(filepath, merge_duplicate_materials, should_check_material_name, rename_materials, apply_weld, unique_name):
    RobotBuilder(filepath, merge_duplicate_materials, should_check_material_name, rename_materials, apply_weld, unique_name)

    return {'FINISHED'}


class URDFImporter(bpy.types.Operator, ImportHelper):
    """Load a URDF file"""
    bl_idname = "import_scene.urdf"
    bl_label = "Import URDF"

    merge_duplicate_materials: bpy.props.EnumProperty(
        name = "Merge duplicate materials method",
        description = "Options to merge duplicate materials",
        items=[('OP1', "With name check", "Merge materials if they have the same name and same content"),
               ('OP2', "Without name check", "Merge materials if they have the same content, regardless of whether they have the same name")]
    )
    rename_materials: bpy.props.BoolProperty(name="Rename materials", default=True)
    apply_weld: bpy.props.BoolProperty(name="Apply weld modifier", default=True)
    unique_name: bpy.props.BoolProperty(name="Each texture has an unique name", default=True)
    

    # ImportHelper mixin class uses this
    filename_ext = ".urdf"

    def execute(self, _):
        if self.merge_duplicate_materials == 'OP1':
            return read_data(self.filepath, self.merge_duplicate_materials, True, self.rename_materials, self.apply_weld, self.unique_name)
        elif self.merge_duplicate_materials == 'OP2':
            return read_data(self.filepath, self.merge_duplicate_materials, False, self.rename_materials, self.apply_weld, self.unique_name)
        else:
            return {'FINISHED'}