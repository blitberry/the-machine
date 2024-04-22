# Here's an enhanced script that will preserve categories and comments in the requirements.txt file

# First, we will define a function to classify the new packages. For simplicity, in this example, we will
# just place them under a new category called "New Packages". This can be modified based on a set of
# rules or manual input later on.

"""def classify_package(package):
    # Placeholder for future package classification logic
    # For now, we just return "New Packages" category
    return "\n# New Packages\n"

# Here is the enhanced script with categorization
enhanced_script_content = """

import subprocess

def get_installed_packages():
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').splitlines()

def read_requirements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def parse_requirements(lines):
    packages = {}
    for line in lines:
        if '==' in line and not line.startswith('#'):
            package, version = line.strip().split('==')
            packages[package.lower()] = version
    return packages

def merge_requirements(existing_lines, installed_packages):
    updated_lines = []
    added_packages = {}
    existing_packages = parse_requirements(existing_lines)
    
    for package, version in installed_packages.items():
        if package.lower() not in existing_packages:
            added_packages[package] = version
    
    for line in existing_lines:
        if '==' in line and not line.startswith('#'):
            package, _ = line.strip().split('==')
            if package.lower() in installed_packages:
                line = f"{package}=={installed_packages[package.lower()]}\n"
        updated_lines.append(line)
    
    # Classify and add new packages at the end of the requirements file
    for package, version in added_packages.items():
        category = classify_package(package)
        if category not in updated_lines:
            updated_lines.append(category)
        updated_lines.append(f"{package}=={version}\n")
    
    return updated_lines

def main(requirements_path):
    existing_lines = read_requirements(requirements_path)
    installed_packages = parse_requirements(get_installed_packages())
    updated_lines = merge_requirements(existing_lines, installed_packages)
    
    with open(requirements_path, 'w') as file:
        file.writelines(updated_lines)

if __name__ == "__main__":
    requirements_path = '/Users/melissaespinoza/env/requirements.txt'  # Path to your requirements.txt file
    main(requirements_path)
