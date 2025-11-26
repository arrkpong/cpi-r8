import csv
import json
import os
import math

def merge_csv_data(base_csv_path, dim_csv_path, output_js_path):
    data = []
    dims = {}

    # 1. Read Dimensions Data
    try:
        with open(dim_csv_path, mode='r', encoding='utf-8-sig') as f:
            next(f) # Skip header
            reader = csv.DictReader(f)
            for row in reader:
                # Key: Pier
                # Columns: Pier, AxisAngle, Len., Thick., CG_X, CG_Y
                if not row['Pier']: continue
                
                dims[row['Pier']] = {
                    'rotation': float(row['AxisAngle']) if row['AxisAngle'] else 0.0,
                    'length': float(row['Len.']) if row['Len.'] else 0.3, # Default if missing
                    'thickness': float(row['Thick.']) if row['Thick.'] else 0.3
                }
        print(f"Loaded dimensions for {len(dims)} items.")
    except Exception as e:
        print(f"Error reading dimensions CSV: {e}")
        return

    # 2. Read Base Data and Merge
    try:
        with open(base_csv_path, mode='r', encoding='utf-8-sig') as f:
            next(f) # Skip header
            reader = csv.DictReader(f)
            
            for row in reader:
                # Columns: SN, Bld, FD, VC, Xvc, Yvc, Pvc
                if not row['VC']: continue

                label = row['VC']
                
                # Base Item
                item = {
                    "id": row['SN'],
                    "zone": row['Bld'],
                    "foundation": row['FD'],
                    "label": label,
                    "x": float(row['Xvc']) if row['Xvc'] else 0.0,
                    "y": float(row['Yvc']) if row['Yvc'] else 0.0,
                    "load": float(row['Pvc']) if row['Pvc'] else 0.0
                }

                # Merge Dimensions
                if label in dims:
                    d = dims[label]
                    item['rotation'] = d['rotation']
                    # We assume Length is the primary dimension (along local X) and Thickness is secondary (along local Y)
                    # This might need adjustment based on visual verification
                    item['width'] = d['length']
                    item['depth'] = d['thickness']
                    item['has_dim'] = True
                else:
                    # Defaults if no dimension data found
                    item['rotation'] = 0
                    item['width'] = 0.4
                    item['depth'] = 0.4
                    item['has_dim'] = False
                    print(f"Warning: No dimensions found for {label}")

                data.append(item)

        # 3. Export to JS
        with open(output_js_path, mode='w', encoding='utf-8') as f:
            json_str = json.dumps(data, indent=4)
            f.write(f"window.floorData = {json_str};")
            
        print(f"Successfully merged and exported {len(data)} records to {output_js_path}")

    except Exception as e:
        print(f"Error processing base CSV: {e}")

if __name__ == "__main__":
    # Paths relative to 'tools/' directory
    base_csv = "../data/251124_R8_FDN_Load_CG_Calc_V01.csv"
    dim_csv = "../data/251125_R8_ABCD_VC_Location_Dimension_V01.csv"
    output_js = "../floor_plan_data.js"
    
    # Ensure we are in the right directory or use absolute paths if needed
    # This assumes running from 'tools/' or root with adjustment
    # Better to use absolute paths based on script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_csv_path = os.path.join(script_dir, base_csv)
    dim_csv_path = os.path.join(script_dir, dim_csv)
    output_js_path = os.path.join(script_dir, output_js)

    merge_csv_data(base_csv_path, dim_csv_path, output_js_path)
