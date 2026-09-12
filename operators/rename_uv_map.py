import bpy


class OBJECT_OT_uv_rename(bpy.types.Operator):
    bl_idname = "object.uv_rename"
    bl_label = "Rename UV Map"
    bl_description = "Overwrite the active UV map name on all selected mesh objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        new_name = context.scene.uv_rename_name.strip()

        if not new_name:
            self.report({'WARNING'}, "Please provide a UV name before renaming.")
            return {'CANCELLED'}

        renamed_count = 0

        for obj in context.selected_objects:
            if obj.type != 'MESH' or not obj.data or not obj.data.uv_layers:
                continue

            active_layer = obj.data.uv_layers.active

            if active_layer is None:
                obj.data.uv_layers.active_index = 0
                active_layer = obj.data.uv_layers.active

            active_layer.name = new_name
            renamed_count += 1

        if renamed_count == 0:
            self.report({'WARNING'}, "No selected mesh objects have UV maps to rename.")
            return {'CANCELLED'}

        plural = "s" if renamed_count != 1 else ""
        self.report({'INFO'}, f"Renamed {renamed_count} UV map{plural}.")
        return {'FINISHED'}


class OBJECT_OT_uv_delete_inactive(bpy.types.Operator):
    bl_idname = "object.uv_delete_inactive"
    bl_label = "Delete Other UV Maps"
    bl_description = "Remove every UV map except the active one on selected meshes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        removed_layers = 0
        affected_objects = 0

        for obj in context.selected_objects:
            if obj.type != 'MESH' or not obj.data:
                continue

            uv_layers = obj.data.uv_layers

            if len(uv_layers) <= 1:
                continue

            if uv_layers.active_index < 0:
                uv_layers.active_index = 0

            indices_to_remove = [i for i in range(len(uv_layers)) if i != uv_layers.active_index]

            if not indices_to_remove:
                continue

            for idx in sorted(indices_to_remove, reverse=True):
                uv_layers.remove(uv_layers[idx])
                removed_layers += 1

            affected_objects += 1

        if removed_layers == 0:
            self.report({'WARNING'}, "No extra UV maps found on selected meshes.")
            return {'CANCELLED'}

        plural = "s" if affected_objects != 1 else ""
        self.report({'INFO'}, f"Removed {removed_layers} UV map slots across {affected_objects} object{plural}.")
        return {'FINISHED'}
