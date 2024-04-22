import subprocess
import re

def get_installed_packages():
    """Use pip freeze to get a list of installed packages."""
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def read_requirements(file_path):
    """Read the existing requirements file, preserving structure and comments."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_requirements(lines):
    """Parse installed packages from requirements.txt"""
    installed = {}
    for line in lines:
        if '==' in line:
            package, version = line.strip().split('==')
            installed[package] = version
    return installed

def merge_requirements(existing, new_packages):
    """Merge new packages into existing categories in the requirements file."""
    updated_lines = []
    added_packages = set(new_packages.keys()) - set(existing.keys())
    
    for line in existing:
        if line.strip() and '==' in line:
            package, version = line.strip().split('==')
            # Update version if it has changed
            if package in new_packages and new_packages[package] != version:
                line = f"{package}=={new_packages[package]}\n"
        updated_lines.append(line)
    
    # Add new packages (basic implementation, improve this for categorization)
    if added_packages:
        updated_lines.append("\n# New Packages\n")
        for package in added_packages:
            updated_lines.append(f"{package}=={new_packages[package]}\n")
    
    return updated_lines

def main():
    # Absolute path to where the requirements.txt file is located
    requirements_path = '/Users/melissaespinoza/env/requirements.txt'  # Update with your actual path

    existing_lines = read_requirements(requirements_path)  # Use the absolute path
    existing_packages = parse_requirements(existing_lines)
    installed_packages = parse_requirements(get_installed_packages().splitlines())
    updated_lines = merge_requirements(existing_packages, installed_packages)
    
    # Write updated requirements back to file
    with open(requirements_path, 'w') as file:  # Use the same absolute path
        file.writelines(updated_lines)

if __name__ == "__main__":
    main()
    



