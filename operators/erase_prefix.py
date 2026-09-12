import bpy

class OBJECT_OT_erase_prefix(bpy.types.Operator):
    bl_idname = "object.erase_prefix"
    bl_label = "Erase Prefix"
    bl_description = "Removes everything before the first underscore from selected objects"
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        renamed_count = 0
        for obj in context.selected_objects:
            # Find the first underscore
            if '_' in obj.name:
                # Split on first underscore and take everything after it
                new_name = obj.name.split('_', 1)[1]
                obj.name = new_name
                renamed_count += 1
        
        if renamed_count > 0:
            self.report({'INFO'}, f"Removed prefix from {renamed_count} object(s)")
        else:
            self.report({'INFO'}, "No prefixes found to remove")
        
        return {'FINISHED'}

