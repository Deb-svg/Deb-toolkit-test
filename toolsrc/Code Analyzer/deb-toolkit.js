#!/usr/bin/env node

const { exec } = require('child_process');
const path = require('path');

const command = process.argv[2];
const subcommand = process.argv[3];
const filePath = process.argv[4];
const package = process.argv[5];

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
} else if (command === 'deps') {
    const scriptPath = path.join(__dirname, 'dependency_manager.py');
    let execCommand = `python ${scriptPath} ${subcommand} ${filePath}`;
    if (package) {
        execCommand += ` ${package}`;
    }
    exec(execCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            process.exit(1);
        } else {
            console.log(stdout);
        }
    });
} else if (command === 'build') {
    const scriptPath = path.join(__dirname, 'build_automation.py');
    let execCommand = `python ${scriptPath} ${subcommand}`;
    exec(execCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${stderr}`);
            process.exit(1);
        } else {
            console.log(stdout);
        }
    });
} else {
    console.log("Usage: deb-toolkit <command> <subcommand> [options]");
    console.log("Commands:");
    console.log("  analyze <file_path>        Analyze the code.");
    console.log("  deps install <file_path>   Install dependencies.");
    console.log("  deps list <file_path>      List dependencies.");
    console.log("  deps add <file_path> <package>    Add a dependency.");
    console.log("  deps remove <file_path> <package> Remove a dependency.");
    console.log("  build clean                Clean the build directory.");
    console.log("  build compile              Compile the source code.");
    console.log("  build package              Package the build output.");
}
