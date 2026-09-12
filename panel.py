import bpy
from . import custom_icons

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Japa Tools"
    bl_label = "Japa Tools"

    def draw(self, context):
        layout = self.layout
        icons = custom_icons["main"]

        # --- Selection Tools (Collapsible) ---
        box = layout.box()
        row = box.row(align=True)
        row.prop(context.scene, "show_selection_tools", 
                text="Selection Tools", 
                icon_value=icons["SELECTION_TOOLS"].icon_id,
                emboss=False)
        
        if context.scene.show_selection_tools:
            col = box.column()
            col.operator("object.select_empty_meshes")
            col.operator("object.select_heavy_meshes")
            col.operator("mesh.select_sharp_edge_verts")

        # --- Renaming Tools (Collapsible) ---
        box = layout.box()
        row = box.row(align=True)
        row.prop(context.scene, "show_renaming_tools", 
                text="Renaming Tools", 
                icon_value=icons["RENAME_TOOLS"].icon_id,
                emboss=False)
        
        if context.scene.show_renaming_tools:
            col = box.column()
            col.operator("object.rename_with_material")
            col.operator("object.rename_data_blocks")
            col.prop(context.scene, "uv_rename_name", text="UV Name")
            col.operator("object.uv_rename", text="Rename UV Map")
            col.operator("object.uv_delete_inactive", text="Delete Other UV Maps")
            
            # --- Prefix Tools ---
            col.separator()
            col.label(text="Prefix Tools")
            
            # Create 3x3 grid of prefix buttons with icons
            prefixes = [
                [("FL", "FL"), ("HOOD", "HOOD"), ("FR", "FR")],
                [("DOOR", "DOOR"), ("ROOF", "ROOF"), ("AERO", "AERO")],
                [("RL", "RL"), ("TRUNK", "TRUNK"), ("RR", "RR")]
            ]
            
            for row_prefixes in prefixes:
                row_layout = col.row()
                for prefix_text, icon_key in row_prefixes:
                    op = row_layout.operator("object.add_prefix", text=prefix_text, icon_value=icons[icon_key].icon_id)
                    op.prefix = prefix_text
            
            # Erase Prefix button
            col.operator("object.erase_prefix", text="Erase Prefix")
            
            # Create Collections button
            col.operator("object.create_prefix_collections", text="Create Collections")

        # --- Data Transfer Tools (Collapsible) ---
        box = layout.box()
        row = box.row(align=True)
        row.prop(context.scene, "show_data_transfer_tools", 
                text="Data Transfer Tools", 
                icon_value=icons["DATA_TRANSFER_TOOLS"].icon_id,
                emboss=False)
        
        if context.scene.show_data_transfer_tools:
            col = box.column()
            col.prop(context.scene, "source_object")
            col.prop(context.scene, "apply_first_vertex_group", text="Apply First Vertex Group")
            col.operator("object.add_data_transfer_modifier")

        # --- Beta Utilities (Collapsible) ---
        box = layout.box()
        row = box.row(align=True)
        row.prop(context.scene, "show_beta_utilities", 
                text="(Beta) Utilities", 
                icon_value=icons["BETA_TOOLS"].icon_id,
                emboss=False)
        
        if context.scene.show_beta_utilities:
            col = box.column()
            col.operator("object.join_by_material")
            col.operator("object.gap_finder")
            col.prop(context.scene, "gap_threshold")
