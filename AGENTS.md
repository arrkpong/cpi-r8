# AGENTS.md

## Project Overview

**Floorplan R8** is a web-based viewer for structural engineering floor plans. It visualizes columns, walls, shear walls, and grid lines, allowing users to interact with the data (zoom, pan, filter zones/types) and export it.

## Tech Stack

- **Core**: HTML5, Vanilla JavaScript
- **Styling**: Tailwind CSS (via CDN)
- **Icons**: Lucide Icons (via CDN)
- **Data Export**: SheetJS (via CDN)
- **Data Source**: `floor_plan_data.js` (Global variables `window.floorData` and `window.floorData`)

## Project Structure

- `index.html`: Main application entry point. Contains all UI structure, styling (custom CSS + Tailwind classes), and application logic (JS).
- `floor_plan_data.js`: Contains the data payload.
  - `window.floorData`: Array of objects representing columns, walls, and shear walls.
  - `window.gridData`: Object defining grid lines for Zones A, B, and C.
- `data/`: Source CSV files for the floor plan data.
- `tools/`: Python scripts for data processing and verification.
  - `process_grid_data.py`: Parses grid CSV and updates `floor_plan_data.js`.
  - `verify_grid.py`: Checks alignment between `floorData` and `gridData`.
  - `find_grid_offsets.py`: Calculates coordinate offsets between data sources.

## Conventions & Guidelines

### Data Handling

- **Global Variables**: Data is loaded into global scope (`window.floorData`, `window.gridData`) from `floor_plan_data.js`.
- **Coordinate Systems**:
  - `floorData` uses **Global Coordinates**.
  - `gridData` uses **Local Coordinates**.
  - **Offsets**: When rendering grids, apply the following X-offsets to align with `floorData`:
    - Zone A: `+10.0`
    - Zone B: `-45.2`
    - Zone C: `-120.8`

### UI/UX

- **Dark Mode**: The application uses a dark blueprint theme (`bg-slate-900`, `text-slate-300`).
- **Responsiveness**: Sidebar + Main Content layout.
- **Interactivity**:
  - Zoom/Pan using CSS transforms on SVG groups (`#content-layer`, `#grid-layer`).
  - Callouts for item details.

### Development Workflow

1.  **Modify `index.html`** for UI/Logic changes.
2.  **Modify `tools/` scripts** if data processing logic changes.
3.  **Run `python tools/<script>.py`** to regenerate data if needed.
4.  **Verify** changes by opening `index.html` in a browser.

## Dos and Don'ts

- **DO** use absolute paths when referencing files.
- **DO** maintain the "Blueprint" aesthetic.
- **DO** check for `window.floorData` existence before rendering.
- **DON'T** overwrite `floor_plan_data.js` manually if it can be regenerated via scripts (unless adding new data types).
- **DON'T** remove the CDN links for Tailwind, Lucide, or SheetJS.

## Useful Commands

- **Process Grid Data**: `python tools/process_grid_data.py`
- **Verify Grid Alignment**: `python tools/verify_grid.py`
