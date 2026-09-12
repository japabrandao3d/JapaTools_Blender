import bpy

class OBJECT_OT_add_prefix(bpy.types.Operator):
    bl_idname = "object.add_prefix"
    bl_label = "Add Prefix"
    bl_description = "Adds a prefix to selected objects"
    
    prefix: bpy.props.StringProperty(
        name="Prefix",
        description="The prefix to add",
        default=""
    )
    
    def execute(self, context):
        if not self.prefix:
            self.report({'ERROR'}, "No prefix specified")
            return {'CANCELLED'}
        
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        for obj in context.selected_objects:
            # Add prefix with underscore at the beginning
            obj.name = f"{self.prefix}_{obj.name}"
        
        self.report({'INFO'}, f"Added prefix '{self.prefix}' to {len(context.selected_objects)} object(s)")
        return {'FINISHED'}

