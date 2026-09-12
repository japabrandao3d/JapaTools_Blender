import bpy

def add_scene_properties():
    bpy.types.Scene.source_object = bpy.props.PointerProperty(
        name="Source Object",
        type=bpy.types.Object,
        description="Object from which data will be transferred"
    )

    bpy.types.Scene.uv_rename_name = bpy.props.StringProperty(
        name="UV Name",
        default="UVMap",
        description="Name that will overwrite the active UV map on selected objects"
    )

    bpy.types.Scene.gap_threshold = bpy.props.FloatProperty(
        name="Gap Threshold",
        default=0.01,
        min=0.0,
        description="Distance threshold to detect gaps between vertices"
    )

    bpy.types.Scene.apply_first_vertex_group = bpy.props.BoolProperty(
        name="Apply First Vertex Group",
        default=False,
        description="Use the first vertex group of each object for the Data Transfer modifier"
    )
    
    # Collapsible section properties
    bpy.types.Scene.show_selection_tools = bpy.props.BoolProperty(
        name="Show Selection Tools",
        default=True,
        description="Show/hide Selection Tools section"
    )
    
    bpy.types.Scene.show_renaming_tools = bpy.props.BoolProperty(
        name="Show Renaming Tools",
        default=True,
        description="Show/hide Renaming Tools section"
    )
    
    bpy.types.Scene.show_data_transfer_tools = bpy.props.BoolProperty(
        name="Show Data Transfer Tools",
        default=True,
        description="Show/hide Data Transfer Tools section"
    )
    
    bpy.types.Scene.show_beta_utilities = bpy.props.BoolProperty(
        name="Show Beta Utilities",
        default=False,
        description="Show/hide Beta Utilities section"
    )

def remove_scene_properties():
    del bpy.types.Scene.source_object
    # REMOVED: del bpy.types.Scene.heavy_mesh_threshold
    del bpy.types.Scene.uv_rename_name
    del bpy.types.Scene.gap_threshold
    del bpy.types.Scene.apply_first_vertex_group
    del bpy.types.Scene.show_selection_tools
    del bpy.types.Scene.show_renaming_tools
    del bpy.types.Scene.show_data_transfer_tools
    del bpy.types.Scene.show_beta_utilities
