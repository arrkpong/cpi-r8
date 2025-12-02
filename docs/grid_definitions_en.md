# Data Dictionary: 251125_R8_ABCD_Grid Definitions - Grid Lines.csv

This file contains **Grid Line** data for each building zone, used for positional reference and rendering on the floor plan.

## Columns

| Header             | Description    | Unit       | Example Data                     | Additional Notes                                                         |
| :----------------- | :------------- | :--------- | :------------------------------- | :----------------------------------------------------------------------- |
| **Name**           | **Zone Name**  | -          | `GA`, `GB`, `GC`                 | Building Zone Code (GA=Zone A, GB=Zone B, GC=Zone C)                     |
| **Grid Line Type** | **Grid Type**  | -          | `X (Cartesian)`, `Y (Cartesian)` | Axis of the grid line (X = Vertical Line, Y = Horizontal Line)           |
| **ID**             | **Grid Label** | -          | `R8.A`, `1`, `A1`                | The label/name of the grid line                                          |
| **Ordinate**       | **Coordinate** | Meters (m) | `0`, `4.05`, `11.8`              | Position of the grid line (Local Coordinate starting at 0 for each zone) |

## Notes

1.  **Coordinates:**

    - The `Ordinate` value is a **Local Coordinate** for each zone.
    - To align this with column/wall data (`floorData`) which uses **Global Coordinates**, you must apply the following **Offsets**:
      - **Zone A (GA):** +10.0 m
      - **Zone B (GB):** -45.2 m
      - **Zone C (GC):** -120.8 m

2.  **Usage:**
    - Used for drawing reference lines on the screen.
    - Data is parsed into `window.gridData` in `data.js` by the script `tools/process_grid_data.py`.
