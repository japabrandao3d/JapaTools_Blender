import bpy, bmesh

class MESH_OT_select_sharp_edge_verts(bpy.types.Operator):
    bl_idname = "mesh.select_sharp_edge_verts"
    bl_label = "Select Sharp Edge Verts"
    bl_description = "Selects vertices connected to edges marked as sharp in Edit Mode"

    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        obj = context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()

        for v in bm.verts:
            v.select = False
        for e in bm.edges:
            if not e.smooth:
                for v in e.verts:
                    v.select = True

        bmesh.update_edit_mesh(obj.data, loop_triangles=False, destructive=False)
        self.report({'INFO'}, "Sharp edge vertices selected.")
        return {'FINISHED'}
