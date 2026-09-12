bl_info = {
    "name": "Japa Tools",
    "author": "Gustavo (Japa) Franco",
    "version": (0, 1, 8),
    "blender": (4, 5, 5),
    "location": "3D Viewport > Sidebar > Japa Tools",
    "description": "A simple interface that groups together small python scripts that I think are great for speeding up tasks, I hope you like it",
    "category": "Development",
}

import bpy
import os
custom_icons = {}
from . import properties
from . import panel
from .operators import (
    rename_data_blocks,
    rename_with_material,
    rename_uv_map,
    select_sharp_edge_verts,
    select_empty_meshes,
    select_heavy_meshes,
    add_data_transfer_modifier,
    gap_finder,
    join_by_material,
    add_prefix,
    erase_prefix,
    create_prefix_collections,
)

def load_custom_icons():
    """Loads custom icons from the 'icons' subfolder."""
    global custom_icons
    
    script_file = os.path.realpath(__file__)
    addon_dir = os.path.dirname(script_file)
    icons_dir = os.path.join(addon_dir, "icons")
    
    if not os.path.isdir(icons_dir):
        print(f"Japa Tools: Icons directory not found at {icons_dir}")
        return

    custom_icons["main"] = bpy.utils.previews.new()
    load_icon = custom_icons["main"].load
    
    # Load the four required icons
    load_icon("SELECTION_TOOLS", os.path.join(icons_dir, "icon_selection_tools.png"), 'IMAGE')
    load_icon("RENAME_TOOLS", os.path.join(icons_dir, "icon_rename_tools.png"), 'IMAGE')
    load_icon("DATA_TRANSFER_TOOLS", os.path.join(icons_dir, "icon_data_transfer_tools.png"), 'IMAGE')
    load_icon("BETA_TOOLS", os.path.join(icons_dir, "icon_beta_tools.png"), 'IMAGE')
    
    # Load prefix icons
    load_icon("FL", os.path.join(icons_dir, "icon_FL.png"), 'IMAGE')
    load_icon("HOOD", os.path.join(icons_dir, "icon_hood.png"), 'IMAGE')
    load_icon("FR", os.path.join(icons_dir, "icon_FR.png"), 'IMAGE')
    load_icon("DOOR", os.path.join(icons_dir, "icon_door.png"), 'IMAGE')
    load_icon("ROOF", os.path.join(icons_dir, "icon_roof.png"), 'IMAGE')
    load_icon("AERO", os.path.join(icons_dir, "icon_spoiler.png"), 'IMAGE')
    load_icon("RL", os.path.join(icons_dir, "icon_RL.png"), 'IMAGE')
    load_icon("TRUNK", os.path.join(icons_dir, "icon_trunk.png"), 'IMAGE')
    load_icon("RR", os.path.join(icons_dir, "icon_RR.png"), 'IMAGE')

def unload_custom_icons():
    """Removes the custom icon collection when the addon is disabled."""
    global custom_icons
    if "main" in custom_icons:
        bpy.utils.previews.remove(custom_icons["main"])
    custom_icons = {}

classes = (
    rename_data_blocks.OBJECT_OT_rename_data_blocks,
    rename_with_material.OBJECT_OT_rename_object_with_material,
    rename_uv_map.OBJECT_OT_uv_rename,
    rename_uv_map.OBJECT_OT_uv_delete_inactive,
    select_sharp_edge_verts.MESH_OT_select_sharp_edge_verts,
    select_empty_meshes.OBJECT_OT_select_empty_meshes,
    select_heavy_meshes.OBJECT_OT_select_heavy_meshes,
    add_data_transfer_modifier.OBJECT_OT_add_data_transfer_modifier,
    gap_finder.OBJECT_OT_gap_finder,
    join_by_material.OBJECT_OT_join_by_material,
    add_prefix.OBJECT_OT_add_prefix,
    erase_prefix.OBJECT_OT_erase_prefix,
    create_prefix_collections.OBJECT_OT_create_prefix_collections,
    panel.VIEW3D_PT_my_custom_panel,
)

def register():
    load_custom_icons()
    properties.add_scene_properties()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    properties.remove_scene_properties()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    unload_custom_icons()

if __name__ == "__main__":
    register()
