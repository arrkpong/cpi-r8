# Data Dictionary: 251128_R8_FDN_XY_ABC.csv

This file contains coordinate data for **Foundations (FDN)**, organized into three distinct zones (**Zone A**, **Zone B**, **Zone C**) laid out horizontally within the CSV file.

## Data Structure (Columns)

| Index  | Header | Description       | Unit      | Example   | Zone  | Additional Notes                       |
| :----- | :----- | :---------------- | :-------- | :-------- | :---- | :------------------------------------- |
| **1**  | **FD** | **Foundation ID** | -         | `A_FG01`  | **A** | Unique identifier for the foundation.  |
| **2**  | **X**  | **X Coordinate**  | Meter (m) | `134.850` | **A** | Easting position.                      |
| **3**  | **Y**  | **Y Coordinate**  | Meter (m) | `21.122`  | **A** | Northing position.                     |
| 4-8    | -      | _Separator_       | -         | -         | -     | Empty columns separating Zone A and B. |
| **9**  | **FD** | **Foundation ID** | -         | `B_FG01`  | **B** |                                        |
| **10** | **X**  | **X Coordinate**  | Meter (m) | -         | **B** |                                        |
| **11** | **Y**  | **Y Coordinate**  | Meter (m) | -         | **B** |                                        |
| 12-16  | -      | _Separator_       | -         | -         | -     | Empty columns separating Zone B and C. |
| **17** | **FD** | **Foundation ID** | -         | `C_FG01`  | **C** |                                        |
| **18** | **X**  | **X Coordinate**  | Meter (m) | `4.400`   | **C** |                                        |
| **19** | **Y**  | **Y Coordinate**  | Meter (m) | `20.822`  | **C** |                                        |

## Notes

1.  **Structure:**

    - The file is structured with three parallel blocks of data for Zones A, B, and C.
    - Data starts from the **3rd row** (Row 1: Zone Labels, Row 2: Headers).

2.  **Usage:**
    - When parsing, treat each zone's block independently or read them based on the column indices provided above.
    - **Offsets to align with `floorData` (Global Coordinates):** Add these to the raw X/Y when converting to the global system used in `data.js` (from the current run of `scripts/process_foundation_data.js`):
        - Zone A: DX = -125.2726, DY = -4.7188
        - Zone B: DX = -125.5453, DY = -5.6842
        - Zone C: DX = -118.1581, DY = -5.3942
      Recompute if source data or alignment reference changes.
