import csv
import json
import os

csv_path = r'd:\code\floorplan_r8\data\251125_R8_ABCD_Grid Definitions - Grid Lines.csv'
js_path = r'd:\code\floorplan_r8\floor_plan_data.js'

grid_data = {
    "A": {"x": [], "y": []},
    "B": {"x": [], "y": []},
    "C": {"x": [], "y": []}
}

zone_map = {"GA": "A", "GB": "B", "GC": "C"}
type_map = {"X (Cartesian)": "x", "Y (Cartesian)": "y"}

print(f"Reading CSV from: {csv_path}")

try:
    with open(csv_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            g_type = row['Grid Line Type']
            label = row['ID']
            ordinate = float(row['Ordinate'])

            if name in zone_map and g_type in type_map:
                zone = zone_map[name]
                axis = type_map[g_type]
                
                grid_data[zone][axis].append({
                    "label": label,
                    "coord": ordinate
                })

    # Sort data by coordinate just in case
    for zone in grid_data:
        for axis in grid_data[zone]:
            grid_data[zone][axis].sort(key=lambda k: k['coord'])

    js_content = f"\n\nwindow.gridData = {json.dumps(grid_data, indent=4)};\n"

    print(f"Appending to JS file: {js_path}")
    with open(js_path, mode='a', encoding='utf-8') as jsfile:
        jsfile.write(js_content)

    print("Successfully appended grid data.")

except Exception as e:
    print(f"Error: {e}")
