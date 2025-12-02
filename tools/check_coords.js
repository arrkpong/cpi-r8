const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, '../data/sandee/251128_R8_FDN_XY_ABC.csv');
const content = fs.readFileSync(filePath, 'utf-8');
const lines = content.split(/\r?\n/);

const logStream = fs.createWriteStream('debug_output.txt', { flags: 'w' });

function log(msg) {
    logStream.write(msg + '\n');
    console.log(msg);
}

lines.forEach((line, index) => {
    if (index < 2) return; // Skip headers
    const cols = line.split(',');
    
    // Zone A
    if (cols[0] && cols[0].includes('FG01')) {
        log(`Found A_FG01 at line ${index}`);
        log(`Line content: ${line}`);
        log(`Zone A: ${cols[0]} X=${cols[1]} Y=${cols[2]}`);
        log(`Zone B (Col 8): ${cols[8]} X=${cols[9]} Y=${cols[10]}`);
        log(`Zone C (Col 16): ${cols[16]} X=${cols[17]} Y=${cols[18]}`);
    }
});

log('Checking Piles...');
const pilePath = path.join(__dirname, '../data/sandee/251127_R8_BP_XY_ABC.csv');
if (fs.existsSync(pilePath)) {
    const pileContent = fs.readFileSync(pilePath, 'utf-8');
    const pileLines = pileContent.split(/\r?\n/);
    pileLines.forEach((line, index) => {
        if (index < 20 && line.includes('FG01')) {
             log(`Pile Line: ${line}`);
        }
    });
}
logStream.end();
