const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../data.js');
const content = fs.readFileSync(filePath, 'utf-8');

// Mock window
const window = {};
eval(content);

const floorData = window.floorData;
const foundationData = window.foundationData;

console.log('--- Checking B_FG01 ---');

const col = floorData.find(d => d.foundation === 'B_FG01');
if (col) {
    console.log(`Column B_FG01: X=${col.x}, Y=${col.y}, Zone=${col.zone}`);
} else {
    console.log('Column B_FG01 NOT FOUND in floorData');
}

const fdn = foundationData.find(d => d.label === 'B_FG01');
if (fdn) {
    console.log(`Foundation B_FG01: X=${fdn.x}, Y=${fdn.y}, Zone=${fdn.zone}`);
} else {
    console.log('Foundation B_FG01 NOT FOUND in foundationData');
}

// Check bounds
const xValues = floorData.map(d => d.x);
const minX = Math.min(...xValues);
const maxX = Math.max(...xValues);
console.log(`FloorData Bounds X: ${minX} to ${maxX}`);
