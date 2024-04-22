
import subprocess

def get_installed_packages():
    """Use pip freeze to get a list of installed packages."""
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').splitlines()

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

def merge_requirements(existing_lines, new_packages):
    """Merge new packages into existing requirements, preserving formatting."""
    updated_lines = []
    for line in existing_lines:
        if '==' in line:
            package, _ = line.strip().split('==')
            if package in new_packages:
                # Update version if it has changed
                line = f"{package}=={new_packages[package]}\n"
        updated_lines.append(line)
    
    # Add new packages not already in requirements.txt
    existing_packages = set(parse_requirements(existing_lines))
    for package, version in new_packages.items():
        if package not in existing_packages:
            updated_lines.append(f"{package}=={version}\n")
    
    return updated_lines

def main(requirements_path):
    existing_lines = read_requirements(requirements_path)
    installed_packages = parse_requirements(get_installed_packages())
    updated_lines = merge_requirements(existing_lines, installed_packages)
    
    # Write updated requirements back to file
    with open(requirements_path, 'w') as file:
        file.writelines(updated_lines)

if __name__ == "__main__":
    requirements_path = '/Users/melissaespinoza/env/requirements.txt'  # Update to your requirements.txt path
    main(requirements_path)
