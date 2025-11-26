import csv

def analyze_labels(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            
        # Find header line
        header_index = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("SN,"):
                header_index = i
                break
        
        if header_index == -1:
            print("Could not find header row starting with 'SN,'")
            return

        print(f"Header found at line {header_index + 1}")
        
        # Parse data
        reader = csv.DictReader(lines[header_index:])
        prefixes = set()
        
        for row in reader:
            if row['VC']:
                label = row['VC']
                # Extract prefix (e.g., "C" from "C_01", "CW" from "CW_01")
                # Logic: Take characters before the first underscore, or first 2 chars if no underscore
                if '_' in label:
                    prefix = label.split('_')[0]
                    # If prefix is just Zone (e.g. A_C17), we want the part after zone?
                    # Wait, A_C19 -> Zone A, Label C19. 
                    # The VC column is "A_C19".
                    # So the "Type" is likely the first letter of the second part.
                    parts = label.split('_')
                    if len(parts) > 1:
                        # Check if first part is Zone (A, B, C)
                        if parts[0] in ['A', 'B', 'C', 'D']:
                            # Then the type is in the second part
                            sub = parts[1]
                            # Extract letters from start of sub
                            type_code = ""
                            for char in sub:
                                if char.isalpha():
                                    type_code += char
                                else:
                                    break
                            prefixes.add(type_code)
                        else:
                            prefixes.add(parts[0])
                else:
                    prefixes.add(label[:2])
                    
        print("Found prefixes:", sorted(list(prefixes)))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_labels("251124_R8_FDN_Load_CG_Calc_V01.csv")
