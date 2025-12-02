const fs = require('fs');
const path = require('path');

// Paths
const foundationPath = path.join(__dirname, '../data/sandee/251128_R8_FDN_XY_ABC.csv');
const pilePath = path.join(__dirname, '../data/sandee/251127_R8_BP_XY_ABC.csv');
const existingDataPath = path.join(__dirname, '../data.js');

// Helper to parse CSV line
function parseCSVLine(line) {
    return line.split(',').map(s => s.trim());
}

try {
    // Read existing data
    let existingDataContent = fs.readFileSync(existingDataPath, 'utf-8');
    
    // Extract floorData
    // Extract floorData
    const floorDataStartMarker = 'window.floorData =';
    const foundationDataStartMarker = 'window.foundationData =';
    const gridDataStartMarker = 'window.gridData =';
    
    const startIdx = existingDataContent.indexOf(floorDataStartMarker);
    let endIdx = existingDataContent.indexOf(foundationDataStartMarker);
    
    if (endIdx === -1) {
        endIdx = existingDataContent.indexOf(gridDataStartMarker);
    }

    if (startIdx === -1 || endIdx === -1) throw new Error("Could not find data markers");

    let floorDataString = existingDataContent.substring(startIdx, endIdx);
    const jsonStart = floorDataString.indexOf('[');
    const jsonEnd = floorDataString.lastIndexOf(']');
    
    if (jsonStart === -1 || jsonEnd === -1) throw new Error("Could not find JSON array");

    const existingFloorData = JSON.parse(floorDataString.substring(jsonStart, jsonEnd + 1));

    // Build Reference Map
    const referenceMap = new Map(); // Zone -> Map<FoundationName, Array<{x, y}>>

    existingFloorData.forEach(item => {
        if (!item.foundation) return;
        
        // Normalize keys
        const zone = item.zone ? item.zone.trim() : 'Unknown';
        const foundation = String(item.foundation).trim();

        if (!referenceMap.has(zone)) {
            referenceMap.set(zone, new Map());
        }
        const zoneMap = referenceMap.get(zone);
        
        if (!zoneMap.has(foundation)) {
            zoneMap.set(foundation, []);
        }
        zoneMap.get(foundation).push({ x: item.x, y: item.y });
    });

    console.log(`Reference Map Zones: ${Array.from(referenceMap.keys()).join(', ')}`);
    if (referenceMap.has('B')) {
        console.log(`Zone B has ${referenceMap.get('B').size} foundations.`);
    }

    // Process Foundations
    const fdnContent = fs.readFileSync(foundationPath, 'utf-8');
    const fdnLines = fdnContent.split(/\r?\n/);
    const foundations = [];
    const zoneOffsets = {
        'A': { dx: 0, dy: 0, count: 0 },
        'B': { dx: 0, dy: 0, count: 0 },
        'C': { dx: 0, dy: 0, count: 0 }
    };

    fdnLines.forEach((line, index) => {
        if (index < 2) return;
        const cols = parseCSVLine(line);
        
        if (cols[0]) processFoundation('A', cols[0], cols[1], cols[2]);
        // CSV layout: [A_FD, A_X, A_Y, '', '', '', '', B_FD, B_X, B_Y, '', '', '', '', C_FD, C_X, C_Y]
        if (cols[7]) processFoundation('B', cols[7], cols[8], cols[9]);
        if (cols[14]) processFoundation('C', cols[14], cols[15], cols[16]);
    });

    function processFoundation(zone, name, xStr, yStr) {
        if (!name) return;
        const x = parseFloat(xStr);
        const y = parseFloat(yStr);
        if (isNaN(x) || isNaN(y)) return;

        const cleanName = name.trim();

        foundations.push({
            zone: zone,
            name: cleanName,
            rawX: x,
            rawY: y
        });

        // Calculate Offset
        if (referenceMap.has(zone)) {
            const zoneMap = referenceMap.get(zone);
            if (zoneMap.has(cleanName)) {
                const cols = zoneMap.get(cleanName);
                let avgColX = 0, avgColY = 0;
                cols.forEach(c => { avgColX += c.x; avgColY += c.y; });
                avgColX /= cols.length;
                avgColY /= cols.length;

                zoneOffsets[zone].dx += (avgColX - x);
                zoneOffsets[zone].dy += (avgColY - y);
                zoneOffsets[zone].count++;
            }
        }
    }

    // Finalize Offsets
    Object.keys(zoneOffsets).forEach(zone => {
        if (zoneOffsets[zone].count > 0) {
            zoneOffsets[zone].dx /= zoneOffsets[zone].count;
            zoneOffsets[zone].dy /= zoneOffsets[zone].count;
            console.log(`Zone ${zone} Offset: DX=${zoneOffsets[zone].dx.toFixed(4)}, DY=${zoneOffsets[zone].dy.toFixed(4)}`);
        } else {
            console.log(`Zone ${zone}: No matches found for offset calculation.`);
        }
    });

    // Apply Offsets
    const processedFoundations = foundations.map(f => ({
        zone: f.zone,
        label: f.name,
        x: parseFloat((f.rawX + zoneOffsets[f.zone].dx).toFixed(2)),
        y: parseFloat((f.rawY + zoneOffsets[f.zone].dy).toFixed(2)),
        width: 0, height: 0
    }));

    // Process Piles
    const pileContent = fs.readFileSync(pilePath, 'utf-8');
    const pileLines = pileContent.split(/\r?\n/);
    const piles = [];

    pileLines.forEach((line, index) => {
        if (index < 2) return;
        const cols = parseCSVLine(line);
        // CSV layout: [A_FD, A_Pile, A_X, A_Y, '', '', '', '', B_FD, B_Pile, B_X, B_Y, '', '', '', '', C_FD, C_Pile, C_X, C_Y]
        if (cols[0]) processPile('A', cols[0], cols[1], cols[2], cols[3]);
        if (cols[7]) processPile('B', cols[7], cols[8], cols[9], cols[10]);
        if (cols[14]) processPile('C', cols[14], cols[15], cols[16], cols[17]);
    });

    function processPile(zone, fdnName, pileName, xStr, yStr) {
        if (!fdnName || !pileName) return;
        const x = parseFloat(xStr);
        const y = parseFloat(yStr);
        if (isNaN(x) || isNaN(y)) return;

        piles.push({
            zone: zone,
            foundation: fdnName.trim(),
            label: pileName.trim(),
            x: parseFloat((x + zoneOffsets[zone].dx).toFixed(2)),
            y: parseFloat((y + zoneOffsets[zone].dy).toFixed(2))
        });
    }

    console.log(`Processed ${processedFoundations.length} foundations and ${piles.length} piles.`);

    // Write Output
    const gridDataStart = existingDataContent.indexOf('window.gridData =');
    let gridDataContent = '';
    if (gridDataStart !== -1) {
        gridDataContent = existingDataContent.substring(gridDataStart);
    }

    const newContent = `window.floorData = ${JSON.stringify(existingFloorData, null, 4)};

window.foundationData = ${JSON.stringify(processedFoundations, null, 4)};

window.pileData = ${JSON.stringify(piles, null, 4)};

${gridDataContent}
`;

    fs.writeFileSync(existingDataPath, newContent, 'utf-8');
    console.log('Updated data.js');

} catch (err) {
    console.error("Fatal Error:", err);
    process.exit(1);
}
