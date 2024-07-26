# scripts/deploy_package.py

import os
import shutil
import sys

def package_project():
    try:
        # Define the source and destination directories
        src_dir = 'deb-toolkit/'
        dist_dir = 'dist/'

        # Ensure the destination directory exists
        os.makedirs(dist_dir, exist_ok=True)

        # Define the name of the package
        package_name = 'deb-toolkit-package.tar.gz'

        # Create a tar.gz archive of the source directory
        shutil.make_archive(os.path.join(dist_dir, 'deb-toolkit-package'), 'gztar', src_dir)
        print(f'Package created: {os.path.join(dist_dir, package_name)}')
    except Exception as e:
        print(f'Error during packaging: {e}')
        sys.exit(1)

if __name__ == '__main__':
    package_project()
