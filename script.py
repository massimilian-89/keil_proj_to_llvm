
import os
import shutil
from xml.etree import ElementTree as ET

"""
Step zero backup restore

"""
def backup_original_e2studio(target_paths, backup_path):
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
    for target_base_path in target_paths:
        for dir_name in os.listdir(target_base_path):
            dir_path = os.path.join(target_base_path, dir_name)
            if os.path.isdir(dir_path):
                e2studio_path = os.path.join(dir_path, 'e2studio')
                backup_e2studio_path = os.path.join(backup_path, f"{dir_name}_e2studio")
                if os.path.exists(e2studio_path):
                    if os.path.exists(backup_e2studio_path):
                        shutil.rmtree(backup_e2studio_path)
                    shutil.copytree(e2studio_path, backup_e2studio_path)
                    print(f"Backed up {e2studio_path} to {backup_e2studio_path}")

def restore_original_e2studio(target_paths, backup_path):
    for target_base_path in target_paths:
        for dir_name in os.listdir(target_base_path):
            dir_path = os.path.join(target_base_path, dir_name)
            if os.path.isdir(dir_path):
                e2studio_path = os.path.join(dir_path, 'e2studio')
                backup_e2studio_path = os.path.join(backup_path, f"{dir_name}_e2studio")
                if os.path.exists(backup_e2studio_path):
                    if os.path.exists(e2studio_path):
                        shutil.rmtree(e2studio_path)
                    shutil.copytree(backup_e2studio_path, e2studio_path)
                    print(f"Restored {e2studio_path} from {backup_e2studio_path}")


def undo_copy_e2studio_folder(target_paths):
    backup_path = "e2studio_backup"
    restore_original_e2studio(target_paths, backup_path)



"""
The first step creating a e2 studio folder in each example and copying the e2studio project from pxp reporter to this folder

"""
import os
import shutil



def copy_e2studio_folder_to_targets(source_folder, target_paths):
    # Check if source folder exists
    if not os.path.isdir(source_folder):
        print(f"The source folder {source_folder} does not exist.")
        return

    
    backup_original_e2studio(target_paths, backup_path)
    
    # Iterate over each target path
    for target_base_path in target_paths:
        for dir_name in os.listdir(target_base_path):
            dir_path = os.path.join(target_base_path, dir_name)
            if os.path.isdir(dir_path):
                target_e2studio_path = os.path.join(dir_path, 'e2studio')
                
                # Copy the e2studio folder
                try:
                    if os.path.exists(target_e2studio_path):
                        shutil.rmtree(target_e2studio_path)
                    shutil.copytree(source_folder, target_e2studio_path)
                    print(f"Copied {source_folder} to {target_e2studio_path}")
                except Exception as e:
                    print(f"Failed to copy {source_folder} to {target_e2studio_path}: {e}")




# Copy the e2studio folder
#copy_e2studio_folder_to_targets(source_folder, target_paths)

# Uncomment the following line to undo the copy and restore the original e2studio folders
# undo_copy_e2studio_folder(target_paths)


"""
Second step , edit the name from prox_reporter to project name in .project xml file
"""


def edit_project_name(target_paths):
    for target_base_path in target_paths:
        for dir_name in os.listdir(target_base_path):
            dir_path = os.path.join(target_base_path, dir_name)
            if os.path.isdir(dir_path):
                project_name = dir_name
                e2studio_path = os.path.join(dir_path, 'e2studio')
                project_file = os.path.join(e2studio_path, '.project')
                
                if os.path.isfile(project_file):
                    try:
                        tree = ET.parse(project_file)
                        root = tree.getroot()
                        name_element = root.find('name')
                        if name_element is not None:
                            name_element.text = project_name
                            tree.write(project_file, encoding='utf-8', xml_declaration=True)
                            print(f"Edited project name in {project_file} to {project_name}")
                        else:
                            print(f"No <name> element found in {project_file}")
                    except Exception as e:
                        print(f"Failed to edit {project_file}: {e}")


# Example usage
source_folder = r"C:\work\DA145xx_SDK\llvm\6.0.22.1401\projects\target_apps\ble_examples\prox_reporter\e2studio"
backup_path = "e2studio_backup"
target_paths = [
    r"C:\work\DA145xx_SDK\llvm\6.0.22.1401\projects\BLE_SDK6_examples\connectivity",
    r"C:\work\DA145xx_SDK\llvm\6.0.22.1401\projects\BLE_SDK6_examples\features",
    r"C:\work\DA145xx_SDK\llvm\6.0.22.1401\projects\BLE_SDK6_examples\interfaces",
    r"C:\work\DA145xx_SDK\llvm\6.0.22.1401\projects\BLE_SDK6_examples\helpers"
]

# Copy the e2studio folder
#copy_e2studio_folder_to_targets(source_folder, target_paths)

# Edit the project name in the .project files
edit_project_name(target_paths)

# Uncomment the following line to undo the copy and restore the original e2studio folders
# undo_copy_e2studio_folder(target_paths)

#backup_original_e2studio(target_paths, backup_path)