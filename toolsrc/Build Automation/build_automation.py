import os
import shutil
import subprocess
import sys

def clean(build_dir):
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        print(f"Cleaned build directory '{build_dir}'")
    else:
        print(f"Build directory '{build_dir}' does not exist.")

def compile_source(source_dir, build_dir):
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    # Assuming this is a Python project, we will compile Python files to bytecode
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".py"):
                source_file = os.path.join(root, file)
                destination_file = os.path.join(build_dir, file + 'c')
                subprocess.run([sys.executable, '-m', 'py_compile', source_file, destination_file])
                print(f"Compiled {source_file} to {destination_file}")

def package(build_dir, dist_dir, package_name):
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    package_file = os.path.join(dist_dir, f"{package_name}.zip")
    shutil.make_archive(package_file.replace('.zip', ''), 'zip', build_dir)
    print(f"Packaged build into {package_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python build_automation.py <command> [options]")
        sys.exit(1)

    command = sys.argv[1]
    build_dir = "build"
    dist_dir = "dist"
    source_dir = "src"
    package_name = "deb_toolkit"

    if command == "clean":
        clean(build_dir)
    elif command == "compile":
        compile_source(source_dir, build_dir)
    elif command == "package":
        package(build_dir, dist_dir, package_name)
    else:
        print("Invalid command.")
        sys.exit(1)

if __name__ == "__main__":
    main()
