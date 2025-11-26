# Data Dictionary: 251124_R8_FDN_Load_CG_Calc_V01.csv

This file serves as the **Base Data** source, containing location coordinates and load data for foundations and column piers.

## Data Structure (Columns)

| Header  | Description               | Unit      | Example            | Additional Notes                                                |
| :------ | :------------------------ | :-------- | :----------------- | :-------------------------------------------------------------- |
| **SN**  | **Serial Number**         | -         | `1`, `2`           | Unique sequence ID for reference.                               |
| **Bld** | **Building Zone**         | -         | `A`, `B`, `C`      | Identifies the building zone.                                   |
| **FD**  | **Foundation ID**         | -         | `A_FG03`           | Unique identifier for the foundation.                           |
| **VC**  | **Vertical Component ID** | -         | `A_C19`, `A_SW1P3` | ID for Column or Wall (Used to join with Dimension file).       |
| **Xvc** | **X Coordinate**          | Meter (m) | `135.45`           | Position along the X-axis.                                      |
| **Yvc** | **Y Coordinate**          | Meter (m) | `16.472`           | Position along the Y-axis.                                      |
| **Pvc** | **Load**                  | Ton       | `-139.85`          | Vertical load on the foundation (Negative value = Compression). |

## Notes

1.  **Coverage:**

    - This file contains location data for **all components** (Columns `C`, Shear Walls `SW`, General Walls `CW`).
    - It is the primary source for determining the location of elements.

2.  **Relation:**
    - The `VC` column is used to link with the `Pier` column in `251125_R8_ABCD_VC_Location_Dimension_V01.csv` to retrieve actual dimensions for visualization.
