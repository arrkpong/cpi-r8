# Data Dictionary: 251127_R8_BP_XY_ABC.csv

This file contains coordinate data for **Bored Piles (BP)**, organized into three distinct zones (**Zone A**, **Zone B**, **Zone C**) laid out horizontally within the CSV file.

## Data Structure (Columns)

| Index  | Header | Description       | Unit      | Example     | Zone  | Additional Notes                                   |
| :----- | :----- | :---------------- | :-------- | :---------- | :---- | :------------------------------------------------- |
| **1**  | **FD** | **Foundation ID** | -         | `A_FG01`    | **A** | Unique identifier for the foundation/pile cap.     |
| **2**  | **Pt** | **Pile Point ID** | -         | `A_FG01_01` | **A** | Specific identifier for the individual bored pile. |
| **3**  | **X**  | **X Coordinate**  | Meter (m) | `134.850`   | **A** | Easting position.                                  |
| **4**  | **Y**  | **Y Coordinate**  | Meter (m) | `15.873`    | **A** | Northing position.                                 |
| 5-7    | -      | _Separator_       | -         | -           | -     | Empty columns separating Zone A and B.             |
| **8**  | **FD** | **Foundation ID** | -         | `B_FG01`    | **B** |                                                    |
| **9**  | **Pt** | **Pile Point ID** | -         | `B_FG01_01` | **B** |                                                    |
| **10** | **X**  | **X Coordinate**  | Meter (m) | `85.488`    | **B** |                                                    |
| **11** | **Y**  | **Y Coordinate**  | Meter (m) | `15.922`    | **B** |                                                    |
| 12-14  | -      | _Separator_       | -         | -           | -     | Empty columns separating Zone B and C.             |
| **15** | **FD** | **Foundation ID** | -         | `C_FG02`    | **C** |                                                    |
| **16** | **Pt** | **Pile Point ID** | -         | `C_FG02_01` | **C** |                                                    |
| **17** | **X**  | **X Coordinate**  | Meter (m) | `9.250`     | **C** |                                                    |
| **18** | **Y**  | **Y Coordinate**  | Meter (m) | `14.472`    | **C** |                                                    |

## Notes

1.  **Structure:**

    - The file is structured with three parallel blocks of data for Zones A, B, and C.
    - Data starts from the **3rd row** (Row 1: Zone Labels, Row 2: Headers).

2.  **Usage:**
    - When parsing, treat each zone's block independently or read them based on the column indices provided above.
