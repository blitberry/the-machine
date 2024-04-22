"""
Script Name: Organize iphone-images
Description: 
This script automates the organization of images and folders within the 'iphone-images' 
directory. It performs the following tasks:
- Moves all files from any subfolders into the main 'iphone-images' directory.
- Deletes any empty subfolders after moving files.
- Deletes any '.DS_Store' files found in the main directory.
Usage: 
Run this script from the command line with the path to the 'iphone-images' directory as an argument.
"""

import os
from pathlib import Path
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

def clean_directory_of_ds_store(main_folder_path):
    # Deletes any '.DS_Store' files from the main directory
    main_folder_path = Path(main_folder_path)
    ds_store_files = main_folder_path.glob('.DS_Store')
    for ds_file in ds_store_files:
        ds_file.unlink()
        print(f"Deleted {ds_file}")

def clean_empty_directories(path):
    # Deletes any empty folders
    path = Path(path)
    for folder in path.rglob('*'):
        if folder.is_dir() and is_folder_empty(folder):
            folder.rmdir()
            print(f"Deleted empty folder: {folder}")

# Replace 'path_to_your_folder' with the actual path to your 'iphone-images' folder
base_path = 'iphone-images'

# Run the organized workflow
move_files_to_main_directory(base_path)
clean_directory_of_ds_store(base_path)
clean_empty_directories(base_path)
