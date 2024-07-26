import os
import sys
import subprocess

def install_dependencies(requirements_file):
    if not os.path.isfile(requirements_file):
        print(f"File '{requirements_file}' does not exist.")
        sys.exit(1)

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
        sys.exit(1)

def list_dependencies(requirements_file):
    if not os.path.isfile(requirements_file):
        print(f"File '{requirements_file}' does not exist.")
        sys.exit(1)

    with open(requirements_file, "r") as file:
        dependencies = file.readlines()
        print("Dependencies:")
        for dep in dependencies:
            print(f" - {dep.strip()}")

def add_dependency(requirements_file, package):
    with open(requirements_file, "a") as file:
        file.write(f"\n{package}")
    print(f"Added '{package}' to '{requirements_file}'.")

def remove_dependency(requirements_file, package):
    if not os.path.isfile(requirements_file):
        print(f"File '{requirements_file}' does not exist.")
        sys.exit(1)

    with open(requirements_file, "r") as file:
        dependencies = file.readlines()

    with open(requirements_file, "w") as file:
        for dep in dependencies:
            if dep.strip() != package:
                file.write(dep)
            else:
                print(f"Removed '{package}' from '{requirements_file}'.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python dependency_manager.py <command> <requirements_file> [package]")
        sys.exit(1)

    command = sys.argv[1]
    requirements_file = sys.argv[2]
    package = sys.argv[3] if len(sys.argv) > 3 else None

    if command == "install":
        install_dependencies(requirements_file)
    elif command == "list":
        list_dependencies(requirements_file)
    elif command == "add" and package:
        add_dependency(requirements_file, package)
    elif command == "remove" and package:
        remove_dependency(requirements_file, package)
    else:
        print("Invalid command or missing package name.")
        sys.exit(1)

if __name__ == "__main__":
    main()
