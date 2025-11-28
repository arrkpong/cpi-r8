import json
import re
from collections import Counter

js_path = r'd:\code\floorplan_r8\floor_plan_data.js'

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    floor_match = re.search(r'window\.floorData\s*=\s*(\[.*?\]);', content, re.DOTALL)
    grid_match = re.search(r'window\.gridData\s*=\s*(\{.*?\});', content, re.DOTALL)
    
    if not floor_match or not grid_match:
        return None, None
        
    return json.loads(floor_match.group(1)), json.loads(grid_match.group(1))

def find_offsets(floor_data, grid_data):
    offsets = {}
    
    for zone in grid_data:
        if zone not in grid_data: 
            continue
            
        # Get all floor X for this zone
        floor_xs = [item['x'] for item in floor_data if item['zone'] == zone]
        
        # Get all grid X for this zone
        if 'x' not in grid_data[zone]:
            continue
        grid_xs = [g['coord'] for g in grid_data[zone]['x']]
        
        if not floor_xs or not grid_xs:
            continue
            
        # Calculate all possible differences
        diffs = []
        for fx in floor_xs:
            for gx in grid_xs:
                diff = fx - gx
                # Round to 1 decimal place to group similar offsets
                diffs.append(round(diff, 1))
                
        # Find the most common difference
        if diffs:
            most_common = Counter(diffs).most_common(1)
            offsets[zone] = most_common[0][0]
            print(f"Zone {zone}: Most common X offset = {most_common[0][0]} (Count: {most_common[0][1]})")
        else:
            offsets[zone] = 0

    return offsets

floor_data, grid_data = load_data(js_path)
if floor_data and grid_data:
    print("Calculating X Offsets...")
    offsets = find_offsets(floor_data, grid_data)
    print("\nRecommended Offsets:")
    print(json.dumps(offsets, indent=4))
