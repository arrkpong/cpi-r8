# RVR Project R8 - Floor Plan Viewer

Web-based interactive viewer for structural foundation and column plans.

## 🌟 Features

- **Interactive Map**: Zoom, Pan, and Reset view controls.
- **Real-Scale Rendering**: Visualizes columns and walls using actual dimensions (Width, Depth) and Rotation from engineering data.
- **Layer Control**: Toggle visibility for Zones (A, B, C), Labels, and Detail Callouts.
- **Data Inspection**: Click on any element to see detailed engineering data (Foundation ID, Load, Coordinates).
- **Responsive Design**: Works on desktop and tablet sizes.

## 📂 Project Structure

```
floorplan_r8/
├── data/               # Source engineering data (CSV/XLSX)
├── docs/               # Data dictionaries and documentation
├── tools/              # Python scripts for data processing
├── FloorPlan.html      # Main Application (Open in Browser)
└── floor_plan_data.js  # Generated data file (Do not edit manually)
```

## 🚀 How to Use

1.  **Open Viewer**: Simply open `FloorPlan.html` in any modern web browser (Chrome, Edge, Firefox).
2.  **Update Data**:
    - Place updated CSV files in the `data/` folder.
    - Run the merge script:
      ```bash
      cd tools
      python merge_data.py
      ```
    - Refresh the browser.

## 🛠️ Tech Stack

- **Frontend**: HTML5, SVG, Tailwind CSS, Lucide Icons
- **Data Processing**: Python (Pandas/CSV)

## 📄 Documentation

- [Base Data Structure (Load & Location)](docs/data_structure_251124.md)
- [Dimension Data Structure](docs/data_structure_251125.md)
