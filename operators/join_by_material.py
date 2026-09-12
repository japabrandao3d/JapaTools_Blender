import bpy

class OBJECT_OT_join_by_material(bpy.types.Operator):
    bl_idname = "object.join_by_material"
    bl_label = "Join by Material"
    bl_description = "Join selected mesh objects with the same material"

    def execute(self, context):
        mat_groups = {}
        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.active_material:
                mat = obj.active_material.name
                mat_groups.setdefault(mat, []).append(obj)

        for group in mat_groups.values():
            if len(group) > 1:
                bpy.ops.object.select_all(action='DESELECT')
                for obj in group:
                    obj.select_set(True)
                context.view_layer.objects.active = group[0]
                bpy.ops.object.join()

        self.report({'INFO'}, "Objects joined by material.")
        return {'FINISHED'}
