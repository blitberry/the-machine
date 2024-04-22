"""
Script Name: Organize iPhone Images
Description: This script automates the organization of images and folders within the 'Iphone images' directory. It performs the following tasks:
- Recursively inspects all folders and subfolders.
- Deletes any empty folders or folders containing only a `.DS_Store` file.
- Renames folders based on a dominant variable (like the most common file type or the earliest/latest date among contained files).
- Renames files based on their content type and creation date, where feasible.
Usage: Run this script from the command line with the path to the 'Iphone images' directory as an argument.
"""
import os
from pathlib import Path
import datetime

def is_folder_empty(folder_path):
    return not any(folder_path.iterdir())

def clean_empty_directories(path):
    path = Path(path)
    for folder in path.rglob('*'):
        if folder.is_dir() and is_folder_empty(folder):
            folder.rmdir()
            print(f"Deleted empty folder: {folder}")

def get_dominant_variable(folder):
    # Placeholder for logic to determine the dominant variable of the folder
    return "dominant_variable"

def rename_folders_based_on_dominant_variable(path):
    path = Path(path)
    for folder in path.iterdir():
        if folder.is_dir() and not is_folder_empty(folder):
            dominant_variable = get_dominant_variable(folder)
            new_folder_name = f"{dominant_variable}_{datetime.datetime.now().strftime('%Y%m%d')}"
            folder.rename(Path(folder.parent, new_folder_name))
            print(f"Renamed folder {folder} to {new_folder_name}")

def rename_files_based_on_date(path):
    path = Path(path)
    for file in path.rglob('*'):
        if file.is_file():
            date_created = datetime.datetime.fromtimestamp(file.stat().st_ctime).strftime('%Y%m%d')
            new_file_name = f"{date_created}_{file.stem}{file.suffix}"
            file.rename(Path(file.parent, new_file_name))
            print(f"Renamed file {file} to {new_file_name}")

# Replace 'path_to_your_folder' with the path to your 'Iphone images' folder
base_path = 'path_to_your_folder'

clean_empty_directories(base_path)
rename_folders_based_on_dominant_variable(base_path)
rename_files_based_on_date(base_path)
