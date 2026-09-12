import bpy

class OBJECT_OT_gap_finder(bpy.types.Operator):
    bl_idname = "object.gap_finder"
    bl_label = "Gap Finder"
    bl_description = "Find and select vertices that are close to each other (potential gaps)"

    def execute(self, context):
        # Ensure the operator is executed in Object Mode
        if context.object.mode != 'OBJECT':
            self.report({'ERROR'}, "You must be in Object Mode to use this operator.")
            return {'CANCELLED'}

        threshold = context.scene.gap_threshold
        all_verts = []

        # Store vertices of all selected objects
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for v in obj.data.vertices:
                    all_verts.append((obj, v.index, obj.matrix_world @ v.co))

        close_map = {}
        for i, (obj_i, idx_i, pos_i) in enumerate(all_verts):
            for j in range(i + 1, len(all_verts)):
                obj_j, idx_j, pos_j = all_verts[j]
                if (pos_i - pos_j).length <= threshold:
                    close_map.setdefault(obj_i, set()).add(idx_i)
                    close_map.setdefault(obj_j, set()).add(idx_j)

        # Deselect all objects to avoid issues with selection
        bpy.ops.object.select_all(action='DESELECT')

        # Enter Edit Mode with multiple objects selected (ensure multiple objects can be edited together)
        bpy.ops.object.select_all(action='SELECT')  # Select all objects
        bpy.ops.object.mode_set(mode='EDIT')  # Enter Edit Mode

        # Now process the objects and their vertices
        for obj, indices in close_map.items():
            # Make sure the object is selected
            obj.select_set(True)

            # Deselect all vertices in Edit mode
            bpy.ops.mesh.select_all(action='DESELECT')

            # Select the close vertices for the current object
            for idx in indices:
                obj.data.vertices[idx].select = True

        # Return to Object Mode to preserve the selection across objects
        bpy.ops.object.mode_set(mode='OBJECT')

        # Report how many vertices were found
        self.report({'INFO'}, f"Found {sum(len(v) for v in close_map.values())} close vertices.")
        return {'FINISHED'}
