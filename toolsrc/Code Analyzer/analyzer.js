#!/usr/bin/env node

const { exec } = require('child_process');
const path = require('path');

const command = process.argv[2];
const filePath = process.argv[3];

if (command === 'analyze' && filePath) {
    const scriptPath = path.join(__dirname, 'code_analyzer.py');
    exec(`python ${scriptPath} ${filePath}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            process.exit(1);
        } else {
            console.log(stdout);
        }
    });
} else {
    console.log("Usage: deb-toolkit analyze <file_path>");
}
