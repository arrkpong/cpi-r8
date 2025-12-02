# RVR Project R8 - Floor Plan Viewer

Web-based interactive viewer for structural foundation and column plans.

## Features

- **Interactive Map**: Zoom, pan, and reset view controls.
- **Real-Scale Rendering**: Uses actual dimensions (width, depth) and rotation from engineering data.
- **Layer Control**: Toggle visibility for Zones (A, B, C), labels, and detail callouts.
- **Data Inspection**: Click any element to see foundation ID, load, and coordinates.
- **Responsive Design**: Works on desktop and tablet sizes.

## Project Structure

```
floorplan_r8/
├── data/   # Source engineering data (CSV/XLSX)
├── docs/   # Data dictionaries and documentation
├── tools/  # Python scripts for data processing
├── index.html          # Main application (open in browser)
└── data.js  # Generated data file (do not edit manually)
```

## How to Use

1. **Open Viewer**: Open `index.html` in a modern web browser (Chrome, Edge, Firefox).
2. **Update Data**:
   - Place updated CSV files in the `data/` folder.
   - Run the merge script:
     ```bash
     cd tools
     python merge_data.py
     ```
   - Refresh the browser.

## Tech Stack

- **Frontend**: HTML5, SVG, Tailwind CSS, Lucide Icons
- **Data Processing**: Python (csv/pandas)

## Documentation

- [Base Data Structure (Load & Location) - TH](docs/base_data_structure.md) | [EN](docs/base_data_structure_en.md)
- [Dimension Data Structure - TH](docs/dimension_data_structure.md) | [EN](docs/dimension_data_structure_en.md)
