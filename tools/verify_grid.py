import json
import re

js_path = r'd:\code\floorplan_r8\data.js'

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    floor_match = re.search(r'window\.floorData\s*=\s*(\[.*?\]);', content, re.DOTALL)
    grid_match = re.search(r'window\.gridData\s*=\s*(\{.*?\});', content, re.DOTALL)
    
    if not floor_match or not grid_match:
        return None, None
        
    return json.loads(floor_match.group(1)), json.loads(grid_match.group(1))

def verify_alignment(floor_data, grid_data, tolerance=0.01):
    stats = {
        "total": 0,
        "aligned_both": 0,
        "aligned_x_only": 0,
        "aligned_y_only": 0,
        "aligned_neither": 0
    }
    
    # To check if it's just a constant offset, let's collect all diffs
    x_diffs = []
    y_diffs = []

    for item in floor_data:
        zone = item['zone']
        if zone not in grid_data:
            continue
            
        stats["total"] += 1
        g_data = grid_data[zone]
        
        # Offsets
        offsets = {
            'A': 10.0,
            'B': -45.2,
            'C': -120.8
        }
        x_offset = offsets.get(zone, 0)

        # Check X
        on_x = False
        min_dx = float('inf')
        if 'x' in g_data:
            for grid in g_data['x']:
                # Global Grid X = Grid Coord + Offset
                global_grid_x = grid['coord'] + x_offset
                dx = item['x'] - global_grid_x
                if abs(dx) < abs(min_dx):
                    min_dx = dx
                if abs(dx) <= tolerance:
                    on_x = True
                    break
        x_diffs.append(min_dx)

        # Check Y
        on_y = False
        min_dy = float('inf')
        if 'y' in g_data:
            for grid in g_data['y']:
                dy = item['y'] - grid['coord']
                if abs(dy) < abs(min_dy):
                    min_dy = dy
                if abs(dy) <= tolerance:
                    on_y = True
                    break
        y_diffs.append(min_dy)

        if on_x and on_y:
            stats["aligned_both"] += 1
        elif on_x:
            stats["aligned_x_only"] += 1
        elif on_y:
            stats["aligned_y_only"] += 1
        else:
            stats["aligned_neither"] += 1

    return stats, x_diffs, y_diffs

floor_data, grid_data = load_data(js_path)
if floor_data and grid_data:
    stats, x_diffs, y_diffs = verify_alignment(floor_data, grid_data)
    
    print("Alignment Report:")
    print(f"Total Items Checked: {stats['total']}")
    print(f"Aligned Both X & Y: {stats['aligned_both']}")
    print(f"Aligned X Only:     {stats['aligned_x_only']}")
    print(f"Aligned Y Only:     {stats['aligned_y_only']}")
    print(f"Aligned Neither:    {stats['aligned_neither']}")
    
    # Analyze offsets for unaligned items
    # Filter out "aligned" (diff ~ 0) to see if there's a common offset
    significant_x = [d for d in x_diffs if abs(d) > 0.01]
    significant_y = [d for d in y_diffs if abs(d) > 0.01]
    
    if significant_x:
        avg_x = sum(significant_x) / len(significant_x)
        print(f"\nAvg X Offset (for unaligned): {avg_x:.4f}")
    if significant_y:
        avg_y = sum(significant_y) / len(significant_y)
        print(f"Avg Y Offset (for unaligned): {avg_y:.4f}")
