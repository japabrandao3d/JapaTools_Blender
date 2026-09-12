import bpy

class OBJECT_OT_add_data_transfer_modifier(bpy.types.Operator):
    bl_idname = "object.add_data_transfer_modifier"
    bl_label = "Add Data Transfer Modifier"
    bl_description = "Adds a Data Transfer modifier to the selected objects"

    def execute(self, context):
        source = context.scene.source_object
        apply_vgroup = context.scene.apply_first_vertex_group

        if not source:
            self.report({'ERROR'}, "No source object selected.")
            return {'CANCELLED'}

        count = 0
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj != source:
                mod = obj.modifiers.new(name="DataTransfer", type='DATA_TRANSFER')
                mod.object = source
                mod.use_loop_data = True
                mod.data_types_loops = {'CUSTOM_NORMAL'}
                mod.loop_mapping = 'POLYINTERP_NEAREST'

                if apply_vgroup and obj.vertex_groups:
                    mod.vertex_group = obj.vertex_groups[0].name

                count += 1

        if count == 0:
            self.report({'WARNING'}, "No valid mesh objects selected (excluding source).")
        else:
            self.report({'INFO'}, f"Data Transfer modifiers added to {count} object(s).")

        return {'FINISHED'}
