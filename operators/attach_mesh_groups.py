import bpy
import re

def get_base_name(obj_name):
    return re.sub(r'_\d+$', '', obj_name)

def has_animation(obj):
    return obj.animation_data is not None and obj.animation_data.action is not None

def apply_modifiers(obj):
    bpy.context.view_layer.objects.active = obj
    for mod in obj.modifiers:
        try:
            bpy.ops.object.modifier_apply(modifier=mod.name)
        except RuntimeError as e:
            print(f"Failed to apply modifier {mod.name} on {obj.name}: {e}")

def get_tris_count(obj):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    eval_obj = obj.evaluated_get(depsgraph)
    return sum(len(p.vertices) - 2 for p in eval_obj.data.polygons)

class OBJECT_OT_attach_mesh_groups(bpy.types.Operator):
    bl_idname = "object.attach_mesh_groups"
    bl_label = "Attach Mesh Groups"
    bl_description = "Attach mesh objects into groups of up to 10,000 triangles"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Ensure we're in Object Mode (if in Edit Mode)
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')

        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        grouped_objects = {}

        for obj in selected_objects:
            if has_animation(obj):
                continue

            base_name = get_base_name(obj.name)
            collection_name = obj.users_collection[0].name if obj.users_collection else None

            if collection_name:
                key = (base_name, collection_name)
                if key not in grouped_objects:
                    grouped_objects[key] = []
                grouped_objects[key].append(obj)

        for (base_name, collection_name), objects in grouped_objects.items():
            current_group = []
            current_tris = 0
            group_counter = 1

            for obj in objects:
                apply_modifiers(obj)
                tris = get_tris_count(obj)

                # Ensure we have valid values for tris
                if tris <= 0:
                    continue  # Skip invalid objects with no triangles

                if current_tris + tris > 10000:
                    if current_group:
                        bpy.ops.object.select_all(action='DESELECT')
                        valid_objs = [o for o in current_group if o and o.name in bpy.data.objects]
                        if not valid_objs:
                            current_group = []
                            current_tris = 0
                            continue
                        for o in valid_objs:
                            bpy.data.objects[o.name].select_set(True)
                        context.view_layer.objects.active = valid_objs[0]
                        bpy.ops.object.join()
                        # Check if context.object exists and is valid
                        if context.object:
                            context.object.name = f"{base_name}_{group_counter:03d}"
                        group_counter += 1
                        current_group = []
                        current_tris = 0

                current_group.append(obj)
                current_tris += tris

            if current_group:
                bpy.ops.object.select_all(action='DESELECT')
                valid_objs = [o for o in current_group if o and o.name in bpy.data.objects]
                if valid_objs:
                    for o in valid_objs:
                        bpy.data.objects[o.name].select_set(True)
                    context.view_layer.objects.active = valid_objs[0]
                    bpy.ops.object.join()
                    if context.object:
                        context.object.name = f"{base_name}_{group_counter:03d}"

        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_attach_mesh_groups)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_attach_mesh_groups)
