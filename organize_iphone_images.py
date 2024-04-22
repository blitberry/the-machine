"""
Script Name: Organize iPhone Images
Description: 
This script automates the organization of images and folders within the 'iphone-images' 
directory. It performs the following tasks:
- Moves all files from any subfolders into the main 'iphone-images' directory.
- Deletes any empty subfolders after moving files.
Usage: 
Run this script from the command line with the path to the 'iphone-images' directory as an argument.
"""

import os
from pathlib import Path
import shutil
import time

def move_files_and_clean_empty_directories(main_folder_path):
    """ Move all files from subfolders to the main directory and delete empty subfolders """
    main_folder_path = Path(main_folder_path)
    for subfolder in main_folder_path.iterdir():
        if subfolder.is_dir():
            # Move all files from the subfolder to the main directory
            for file in subfolder.glob('*'):  # The glob('*') pattern will match all files and folders
                if file.is_file() and not file.name.startswith('.'):  # Skip hidden files
                    new_location = main_folder_path.joinpath(file.name)
                    if not new_location.exists():  # Prevent overwriting files
                        shutil.move(str(file), str(new_location))
                        print(f"Moved {file} to {new_location}")
                    else:
                        print(f"File {file.name} already exists in {main_folder_path}, not moved.")
                elif file.is_dir():
                    print(f"Subfolder {file} might not be empty or contains hidden files.")

            # Give some time for the filesystem to update
            time.sleep(1)

            # Check again if the subfolder is empty and delete it
            if not any(subfolder.iterdir()):
                try:
                    subfolder.rmdir()
                    print(f"Deleted empty subfolder: {subfolder}")
                except OSError as e:
                    print(f"Could not delete {subfolder}: {e}")

# Replace 'path_to_your_folder' with the actual path to your 'iphone-images' folder
base_path = 'iphone-images'  # Ensure this is the correct path to the folder

# Execute the file organization and cleaning process
move_files_and_clean_empty_directories(base_path)
