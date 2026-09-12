import bpy

class OBJECT_OT_rename_data_blocks(bpy.types.Operator):
    bl_idname = "object.rename_data_blocks"
    bl_label = "Rename Object Data"
    bl_description = "Renames the data of objects with only one user"

    def execute(self, context):
        for obj in bpy.data.objects:
            if obj.data and obj.data.users == 1:
                obj.data.name = obj.name
        self.report({'INFO'}, "Data renamed successfully.")
        return {'FINISHED'}
