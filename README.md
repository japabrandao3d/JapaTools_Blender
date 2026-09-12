# Japa Tools — Blender

> Personal toolkit by Gustavo **(Japa) Franco** to speed up 3D modeling — with a strong focus on **automotive assets**.

A Blender add-on that gathers useful scripts into one panel: selection, renaming, car-part prefixes, data transfer, and cleanup utilities. Fewer repetitive clicks, more time modeling.

**Version:** `0.1.8` · **Blender:** `4.5.5+` · **Panel:** `3D Viewport → Sidebar → Japa Tools`

---

## What it does

| Group | Purpose |
| --- | --- |
| **Selection Tools** | Find empty meshes, heavy meshes (>10k tris), and sharp-edge vertices |
| **Renaming Tools** | Rename by material, sync data blocks, and manage UV maps |
| **Prefix Tools** | Tag car parts (DOOR, HOOD, FL/FR…) and organize them into collections |
| **Data Transfer** | Batch-apply a Data Transfer Modifier from a source object |
| **(Beta) Utilities** | Join by Material and Gap Finder for mesh cleanup / QA |

---

## Installation

1. Download this repository (ZIP or clone).
2. In Blender: **Edit → Preferences → Add-ons → Install…**
3. Select the add-on folder/ZIP and enable **Japa Tools**.
4. Open the **N-Panel** in the 3D Viewport and go to the **Japa Tools** tab.

> Compatible with the modern extension format (`blender_manifest.toml`). Requires Blender **4.5.5** or newer.

---

## Tools in detail

### Selection Tools
- **Select Empty Meshes** — selects meshes with no vertices (great after boolean / cleanup).
- **Select Meshes with > 10k** — highlights heavy parts for optimization.
- **Select Sharp Edge Verts** — selects vertices connected to sharp edges (Edit Mode).

### Renaming Tools
- **Rename Object with Material** — renames objects using the active material name.
- **Rename Object Data** — syncs the data-block name with the object name.
- **Rename UV Map / Delete Other UV Maps** — standardizes UVs and removes extra maps.

### Prefix Tools (automotive workflow)
Icon buttons to prefix selected objects:

| Prefix | Typical use |
| --- | --- |
| `FL` / `FR` / `RL` / `RR` | Wheels / corners (Front/Rear × Left/Right) |
| `HOOD` | Hood |
| `DOOR` | Doors |
| `ROOF` | Roof |
| `TRUNK` | Trunk |
| `AERO` | Spoiler, diffuser, and aero parts |

Prefixes are **stackable**. Example: object `Black` → click `DOOR` then `RR` → `DOOR_RR_Black`.

- **Erase Prefix** — removes everything before the first `_`.
- **Create Collections** — groups objects by prefix (before the first `_`) into collections.

### Data Transfer Tools
- Pick a **Source Object**, optionally use the first vertex group, and apply the modifier to the selection.

### (Beta) Utilities
- **Join by Material** — joins meshes that share the same material.
- **Gap Finder** — selects vertices that are very close together (configurable threshold).

---

## Suggested car workflow

1. Clean the scene with **Empty / Heavy meshes**.
2. Organize names with **material** renaming and **prefixes** (DOOR, HOOD…).
3. Generate **collections** automatically.
4. Transfer normals / data between similar parts.
5. Finish with Gap Finder / Join by Material if needed.

---

## Project structure

```
JapaTools_Blender/
├── __init__.py              # add-on registration
├── blender_manifest.toml    # manifest / version
├── panel.py                 # N-Panel UI
├── properties.py            # scene properties
├── operators/               # one module per tool
└── icons/                   # panel and prefix icons
```

---

## License

GPL-3.0-or-later — see the add-on manifest.

---

## Author

**Gustavo (Japa) Franco**  
Built from a real production 3D workflow — if something can be faster, feedback is welcome.

Sister repo: [JapaTools_RobloxStudio](https://github.com/japabrandao3d/JapaTools_RobloxStudio)
