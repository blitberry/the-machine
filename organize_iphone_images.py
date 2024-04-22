"""
Script Name: Organize iphone-images
Description: 
This script automates the organization of images and folders within the 'iphone-images' 
directory. It performs the following tasks:
- Recursively inspects all folders and subfolders.
- Moves all files from subfolders to the main 'iphone-images' directory.
- Deletes any empty subfolders after moving files.
- Deletes any empty folders or folders containing only a `.DS_Store` file.
- Renames folders based on a dominant variable (placeholder function included).
- Renames files based on their content type and creation date, where feasible (placeholder for actual content analysis).
Usage: 
Run this script from the command line with the path to the 'iphone-images' directory as an argument.
"""

import os
from pathlib import Path
import datetime
import shutil

def is_folder_empty(folder_path):
    # Checks if a folder is empty
    return not any(folder_path.iterdir())

def move_files_to_main_directory(main_folder_path):
    # Moves all files from subfolders to the main directory
    main_folder_path = Path(main_folder_path)
    for subfolder in main_folder_path.iterdir():
        if subfolder.is_dir():
            for file in subfolder.iterdir():
                if file.is_file():
                    new_location = main_folder_path.joinpath(file.name)
                    if not new_location.exists():  # Prevent overwriting files
                        shutil.move(str(file), str(new_location))
                        print(f"Moved {file} to {new_location}")
                    else:
                        print(f"File {file.name} already exists in {main_folder_path}, not moved.")

            # After moving files, check if subfolder is empty and delete it
            if is_folder_empty(subfolder):
                subfolder.rmdir()
                print(f"Deleted empty subfolder: {subfolder}")

def clean_empty_directories(path):
    # Deletes any empty folders
    path = Path(path)
    for folder in path.rglob('*'):
        if folder.is_dir() and is_folder_empty(folder):
            folder.rmdir()
            print(f"Deleted empty folder: {folder}")

# Placeholder functions for future functionality
def get_dominant_variable(folder):
    # Placeholder logic to determine the dominant variable of the folder
    return "dominant_variable"

def rename_folders_based_on_dominant_variable(path):
    # Renames folders based on a dominant variable
    path = Path(path)
    for folder in path.iterdir():
        if folder.is_dir() and not is_folder_empty(folder):
            dominant_variable = get_dominant_variable(folder)
            new_folder_name = f"{dominant_variable}_{datetime.datetime.now().strftime('%Y%m%d')}"
            folder.rename(Path(folder.parent, new_folder_name))
            print(f"Renamed folder {folder} to {new_folder_name}")

def rename_files_based_on_date(path):
    # Renames files based on the creation date
    path = Path(path)
    for file in path.rglob('*'):
        if file.is_file():
            date_created = datetime.datetime.fromtimestamp(file.stat().st_ctime).strftime('%Y%m%d')
            new_file_name = f"{date_created}_{file.stem}{file.suffix}"
            file.rename(Path(file.parent, new_file_name))
            print(f"Renamed file {file} to {new_file_name}")

# Replace 'path_to_your_folder' with the actual path to your 'iphone-images' folder
base_path = 'iphone-images'

# Run the organized workflow
move_files_to_main_directory(base_path)
clean_empty_directories(base_path)
rename_folders_based_on_dominant_variable(base_path)
rename_files_based_on_date(base_path)
