#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');

// Define the available commands
const commands = {
    analyze: () => {
        console.log('Running code analyzer...');
        execSync('python scripts/code_analyzer.py', { stdio: 'inherit' });
    },
    deps: () => {
        console.log('Managing dependencies...');
        execSync('pip install -r requirements.txt', { stdio: 'inherit' });
    },
    build: () => {
        console.log('Building project...');
        execSync('python scripts/build_automation.py', { stdio: 'inherit' });
    },
    test: () => {
        console.log('Running tests...');
        execSync('pytest', { stdio: 'inherit' });
    },
    package: () => {
        console.log('Packaging project...');
        execSync('python scripts/deploy_package.py', { stdio: 'inherit' });
    },
    deploy: () => {
        const args = process.argv.slice(3);
        if (args.length !== 4) {
            console.error('Usage: deb-toolkit deploy <package_path> <server_ip> <username> <password>');
            process.exit(1);
        }
        const [packagePath, serverIp, username, password] = args;
        console.log('Deploying package...');
        execSync(`python scripts/deploy_to_server.py ${packagePath} ${serverIp} ${username} ${password}`, { stdio: 'inherit' });
    },
    docs: () => {
        console.log('Generating documentation...');
        execSync('sphinx-build -b html docs/source docs/build', { stdio: 'inherit' });
    }
};

// Parse command-line arguments
const [,, command, ...args] = process.argv;

if (commands[command]) {
    commands[command]();
} else {
    console.error(`Unknown command: ${command}`);
    console.log('Available commands: analyze, deps, build, test, package, deploy, docs');
    process.exit(1);
}
