import bpy

class OBJECT_OT_rename_object_with_material(bpy.types.Operator):
    bl_idname = "object.rename_with_material"
    bl_label = "Rename Object with Material"
    bl_description = "Renames selected objects with their active material's name"

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.active_material:
                obj.name = obj.active_material.name
        self.report({'INFO'}, "Objects renamed using material names.")
        return {'FINISHED'}
