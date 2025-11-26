# Data Dictionary: 251125_R8_ABCD_VC_Location_Dimension_V01.csv

This file contains **Dimension** and **Location** data for Columns and Shear Walls.

## Data Structure (Columns)

| Header        | Description        | Unit      | Example            | Additional Notes                                                 |
| :------------ | :----------------- | :-------- | :----------------- | :--------------------------------------------------------------- |
| **Pier**      | **Component ID**   | -         | `C_C01`, `A_SW1P3` | Used to join with the Base Data file.                            |
| **AxisAngle** | **Rotation Angle** | Degree    | `90.00`, `0.00`    | Rotation angle relative to the X-axis.                           |
| **Len.**      | **Length**         | Meter (m) | `0.40`, `19.65`    | Cross-section width (Used as **Width** in visualization).        |
| **Thick.**    | **Thickness**      | Meter (m) | `0.35`, `0.11`     | Cross-section depth (Used as **Depth/Height** in visualization). |
| **CG_X**      | **X Coordinate**   | Meter (m) | `-120.75`          | Center of Gravity position along X-axis.                         |
| **CG_Y**      | **Y Coordinate**   | Meter (m) | `13.35`            | Center of Gravity position along Y-axis.                         |

## Notes

1.  **Data Types:**

    - **Columns:** IDs starting with `C_` (e.g., `C_C01`).
    - **Shear Walls:** IDs starting with `SW` (e.g., `A_SW1P3`).

2.  **Usage in Visualization:**

    - **Shape:** Rendered as a Rectangle.
    - **Size:** Width = `Len.`, Height = `Thick.`
    - **Rotation:** Rotated by `AxisAngle`.
    - **Position:** Placed at `(CG_X, CG_Y)`.

3.  **Missing Data:**
    - Data for General Walls (IDs starting with `CW`) is **missing** from this file.
