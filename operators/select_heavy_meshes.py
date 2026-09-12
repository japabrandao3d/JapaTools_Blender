import bpy

class OBJECT_OT_select_heavy_meshes(bpy.types.Operator):
    bl_idname = "object.select_heavy_meshes"
    bl_label = "Select Meshes with > 10k" 
    bl_description = "Selects mesh objects with more than 10,000 triangles"
    TRI_THRESHOLD = 10000

    @classmethod
    def poll(cls, context):
        """Allows the operator to run only in Object Mode."""
        return context.mode == 'OBJECT'

    def execute(self, context):
        threshold = self.TRI_THRESHOLD 

        bpy.ops.object.select_all(action='DESELECT')
        selected_count = 0

        for obj in context.scene.objects:
            if obj.type == 'MESH':
                depsgraph = context.evaluated_depsgraph_get()
                object_eval = obj.evaluated_get(depsgraph)
                
                # Use loop_triangles to get actual triangle count
                # This accounts for quads (2 tris) and n-gons (n-2 tris)
                if hasattr(object_eval.data, 'loop_triangles') and object_eval.data.loop_triangles:
                    triangle_count = len(object_eval.data.loop_triangles)
                else:
                    # Fallback: calculate from polygons
                    # Each polygon with n vertices = n-2 triangles
                    triangle_count = 0
                    for poly in object_eval.data.polygons:
                        triangle_count += len(poly.vertices) - 2
                
                if triangle_count > threshold:
                    obj.select_set(True)
                    selected_count += 1

        if selected_count > 0:
            self.report({'INFO'}, f"{selected_count} mesh(es) selected (>10,000 tris).")
        else:
            self.report({'INFO'}, "No meshes found with more than 10,000 triangles.")
            
        return {'FINISHED'}
