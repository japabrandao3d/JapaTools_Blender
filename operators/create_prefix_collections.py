import bpy

class OBJECT_OT_create_prefix_collections(bpy.types.Operator):
    bl_idname = "object.create_prefix_collections"
    bl_label = "Create Collections"
    bl_description = "Groups objects by their prefix (everything before the first underscore) into collections"
    
    def execute(self, context):
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        # Dictionary to store prefix -> list of objects
        prefix_groups = {}
        
        # Group objects by prefix
        for obj in context.selected_objects:
            if '_' in obj.name:
                # Split by underscores
                parts = obj.name.split('_')
                
                # Determine collection name based on number of parts
                # If there are 3+ parts (2+ underscores), use first two (e.g., "Door_RR_Black" -> "Door_RR")
                # If there are only 2 parts (1 underscore), use first part (e.g., "RR_Wheel" -> "RR")
                if len(parts) >= 3:
                    # Use first two parts for collection name
                    collection_name = f"{parts[0]}_{parts[1]}"
                elif len(parts) == 2:
                    # Use first part only
                    collection_name = parts[0]
                else:
                    # Fallback: use first part only
                    collection_name = parts[0]
                
                if collection_name not in prefix_groups:
                    prefix_groups[collection_name] = []
                prefix_groups[collection_name].append(obj)
        
        if not prefix_groups:
            self.report({'WARNING'}, "No objects with prefixes found")
            return {'CANCELLED'}
        
        # Create collections and move objects
        collections_created = 0
        for collection_name, objects in prefix_groups.items():
            # Check if collection already exists
            collection = bpy.data.collections.get(collection_name)
            
            if collection is None:
                # Create new collection
                collection = bpy.data.collections.new(collection_name)
                context.scene.collection.children.link(collection)
                collections_created += 1
            
            # Move objects to collection
            for obj in objects:
                # Remove from current collections
                for coll in obj.users_collection:
                    coll.objects.unlink(obj)
                # Add to new collection
                collection.objects.link(obj)
        
        self.report({'INFO'}, f"Created {collections_created} collection(s) and grouped {len(context.selected_objects)} object(s)")
        return {'FINISHED'}

