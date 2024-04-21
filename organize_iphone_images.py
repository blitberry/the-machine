"""
Script Name: Organize iPhone Images
Description: This script automates the organization of images and folders within the 'Iphone Images 1' directory. It performs the following tasks:
- Recursively inspects all folders and subfolders.
- Deletes any empty folders or folders containing only a `.DS_Store` file.
- Renames folders based on a dominant variable (like the most common file type or the earliest/latest date among contained files).
- Renames files based on their content type and creation date, where feasible.
Usage: Run this script from the command line with the path to the 'Iphone Images 1' directory as an argument.
"""

import os
from pathlib import Path
import datetime

# Your code follows...
import os
from pathlib import Path
import datetime

def clean_directory(path):
    path = Path(path)
    for folder in path.rglob('*'):  # Recursively goes through all folders
        if folder.is_dir():  # Check if it is a directory
            contents = list(folder.iterdir())
            ds_store_files = [f for f in contents if f.name == '.DS_Store']
            
            # Remove folder if it's empty or contains only .DS_Store
            if not contents or (len(ds_store_files) == len(contents)):
                for f in ds_store_files:
                    f.unlink()  # Delete .DS_Store file
                folder.rmdir()  # Remove the directory
                print(f"Deleted {folder}")
            else:
                # Here you could add renaming logic based on folder contents
                pass

def rename_folders_based_on_content(path):
    path = Path(path)
    for folder in path.rglob('*'):
        if folder.is_dir() and any(folder.iterdir()):
            # Example: Rename folder based on the most common file type
            file_types = [f.suffix for f in folder.iterdir() if f.is_file()]
            if file_types:
                most_common_type = max(set(file_types), key=file_types.count)
                new_folder_name = f"{folder.parent}/{most_common_type.replace('.', '')}_files_{datetime.datetime.now().strftime('%Y%m%d')}"
                os.rename(folder, new_folder_name)
                print(f"Renamed {folder} to {new_folder_name}")

def rename_files_based_on_date(path):
    path = Path(path)
    for file in path.rglob('*'):
        if file.is_file() and not file.name.startswith('.'):
            creation_time = datetime.datetime.fromtimestamp(file.stat().st_mtime).strftime('%Y%m%d')
            new_file_name = f"{file.parent}/{creation_time}_{file.stem}{file.suffix}"
            os.rename(file, new_file_name)
            print(f"Renamed {file} to {new_file_name}")

# Example usage:
base_path = '/path/to/Iphone Images 1'
clean_directory(base_path)
rename_folders_based_on_content(base_path)
rename_files_based_on_date(base_path)
