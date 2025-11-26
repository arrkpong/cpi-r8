import csv
import json
import os

def convert_csv_to_json(csv_file_path, json_file_path):
    data = []
    
    try:
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
            # Skip the first line (metadata)
            next(csv_file)
            
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                # Clean up keys if necessary (sometimes there are spaces)
                # Based on the file view: SN,Bld,FD,VC,Xvc,Yvc,Pvc
                
                if not row['VC']: # Skip empty rows if any
                    continue
                    
                item = {
                    "id": row['SN'],
                    "zone": row['Bld'],
                    "foundation": row['FD'],
                    "label": row['VC'],
                    "x": float(row['Xvc']) if row['Xvc'] else 0.0,
                    "y": float(row['Yvc']) if row['Yvc'] else 0.0,
                    "load": float(row['Pvc']) if row['Pvc'] else 0.0
                }
                data.append(item)
                
        # Export as JS file to avoid CORS issues with local file:// protocol
        js_file_path = json_file_path.replace('.json', '.js')
        with open(js_file_path, mode='w', encoding='utf-8') as js_file:
            json_str = json.dumps(data, indent=4)
            js_file.write(f"window.floorData = {json_str};")
            
        print(f"Successfully converted {len(data)} records to {js_file_path}")
        
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")

if __name__ == "__main__":
    # Use absolute paths or relative to the script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming the script is in the root or we navigate to it. 
    # The user has the file in d:\code\github\
    
    # We will assume this script is run from d:\code\github\ or we can just hardcode the filename
    # and expect it to be in the same directory.
    
    csv_filename = "251124_R8_FDN_Load_CG_Calc_V01.csv"
    json_filename = "floor_plan_data.json"
    
    convert_csv_to_json(csv_filename, json_filename)
