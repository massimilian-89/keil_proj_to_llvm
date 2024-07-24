import os
import shutil
from xml.etree import ElementTree as ET

def copy_e2studio_folder_to_projects(source_folder, project_path):
    if not os.path.isdir(source_folder):
        print(f"The source folder {source_folder} does not exist.")
        return
    
    for root, dirs, files in os.walk(project_path):
        if 'Keil_5' in dirs and 'src' in dirs:
            # Avoid copying to the source folder itself
            if root == os.path.dirname(source_folder):
                continue
            target_e2studio_path = os.path.join(root, 'e2studio')
            try:
                if os.path.exists(target_e2studio_path):
                    shutil.rmtree(target_e2studio_path)
                shutil.copytree(source_folder, target_e2studio_path)
                print(f"Copied {source_folder} to {target_e2studio_path}")
            except Exception as e:
                print(f"Failed to copy {source_folder} to {target_e2studio_path}: {e}")

def edit_project_name(project_path):
    for root, dirs, files in os.walk(project_path):
        if 'Keil_5' in dirs and 'src' in dirs:
            project_name = os.path.basename(root)
            e2studio_path = os.path.join(root, 'e2studio')
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
            else:
                print(f"No .project file found in {e2studio_path}")
