import os
import xml.etree.ElementTree as ET
import argparse

def get_project_name(project_path):
    return os.path.basename(project_path)

def modify_project_name(file_path, project_name):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find the <name> tag and update its value
    name_tag = root.find('name')
    if name_tag is not None:
        old_name = name_tag.text
        name_tag.text = project_name
        print(f"Changed project name from '{old_name}' to '{project_name}'")
    else:
        print("<name> tag not found in the XML file")
    
    # Write the changes back to the file
    tree.write(file_path)
    print(f"Project name changes have been saved to {file_path}")

def remove_user_proxr(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find the <link> element with <name>user_app/user_proxr.c</name>
    linked_resources = root.find('linkedResources')
    if linked_resources is not None:
        for link in linked_resources.findall('link'):
            name_tag = link.find('name')
            if name_tag is not None and name_tag.text == 'user_app/user_proxr.c':
                linked_resources.remove(link)
                print("Removed <link> element with <name>user_app/user_proxr.c</name>")
                break
        else:
            print("<link> element with <name>user_app/user_proxr.c</name> not found")
    
    # Write the changes back to the file
    tree.write(file_path)
    print(f"Changes have been saved to {file_path}")

def remove_user_periph_setup(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find the <link> element with <name>user_app/user_periph_setup.c</name>
    linked_resources = root.find('linkedResources')
    if linked_resources is not None:
        for link in linked_resources.findall('link'):
            name_tag = link.find('name')
            if name_tag is not None and name_tag.text == 'user_app/user_periph_setup.c':
                linked_resources.remove(link)
                print("Removed <link> element with <name>user_app/user_periph_setup.c</name>")
                break
        else:
            print("<link> element with <name>user_app/user_periph_setup.c</name> not found")
    
    # Write the changes back to the file
    tree.write(file_path)
    print(f"Changes have been saved to {file_path}")

def add_src_files(file_path, source_dir, project_root):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find the linkedResources section
    linked_resources = root.find('linkedResources')
    if linked_resources is None:
        linked_resources = ET.SubElement(root, 'linkedResources')
    
    # Add user_custom_profile folder and specific files within it
    custom_files_to_add = [
        ('user_custom_profile/user_custs1_def.c', 'src/custom_profile/user_custs1_def.c'),
        ('user_custom_profile/user_custs_config.c', 'src/custom_profile/user_custs_config.c')
    ]
    for c_file, relative_path in custom_files_to_add:
        link = ET.SubElement(linked_resources, 'link')
        name = ET.SubElement(link, 'name')
        name.text = c_file
        type_tag = ET.SubElement(link, 'type')
        type_tag.text = '1'
        location = ET.SubElement(link, 'locationURI')
        location.text = f'PARENT-1-PROJECT_LOC/{relative_path}'
        print(f"Added link for {c_file} with locationURI {location.text}")

    # Add user_periph_setup.c to user_platform folder
    platform_file = 'user_platform/user_periph_setup.c'
    platform_path = 'src/platform/user_periph_setup.c'
    link = ET.SubElement(linked_resources, 'link')
    name = ET.SubElement(link, 'name')
    name.text = platform_file
    type_tag = ET.SubElement(link, 'type')
    type_tag.text = '1'
    location = ET.SubElement(link, 'locationURI')
    location.text = f'PARENT-1-PROJECT_LOC/{platform_path}'
    print(f'Added link for {platform_file} with locationURI {location.text}')

    # Add app_customs.c and app_customs_task.c to sdk_app folder
    sdk_app_files_to_add = [
        ('sdk_app/app_customs.c', 'sdk/app_modules/src/app_custs/app_customs.c'),
        ('sdk_app/app_customs_task.c', 'sdk/app_modules/src/app_custs/app_customs_task.c')
    ]
    for c_file, relative_path in sdk_app_files_to_add:
        link = ET.SubElement(linked_resources, 'link')
        name = ET.SubElement(link, 'name')
        name.text = c_file
        type_tag = ET.SubElement(link, 'type')
        type_tag.text = '1'
        location = ET.SubElement(link, 'locationURI')
        location.text = f'PARENT-5-PROJECT_LOC/{relative_path}'
        print(f'Added link for {c_file} with locationURI {location.text}')

    # Add additional files to sdk_profiles folder
    sdk_profiles_files_to_add = [
        ('sdk_profiles/attm_db_128.c', 'sdk/ble_stack/host/att/attm/attm_db_128.c'),
        ('sdk_profiles/custom_common.c', 'sdk/ble_stack/profiles/custom/custom_common.c'),
        ('sdk_profiles/custs1.c', 'sdk/ble_stack/profiles/custom/custs/src/custs1.c'),
        ('sdk_profiles/custs1_task.c', 'sdk/ble_stack/profiles/custom/custs/src/custs1_task.c')
    ]
    for c_file, relative_path in sdk_profiles_files_to_add:
        link = ET.SubElement(linked_resources, 'link')
        name = ET.SubElement(link, 'name')
        name.text = c_file
        type_tag = ET.SubElement(link, 'type')
        type_tag.text = '1'
        location = ET.SubElement(link, 'locationURI')
        location.text = f'PARENT-5-PROJECT_LOC/{relative_path}'
        print(f'Added link for {c_file} with locationURI {location.text}')

    # Add timer0.c to sdk_driver folder
    sdk_driver_file = 'sdk_driver/timer0.c'
    sdk_driver_path = 'sdk/platform/driver/timer/timer0.c'
    link = ET.SubElement(linked_resources, 'link')
    name = ET.SubElement(link, 'name')
    name.text = sdk_driver_file
    type_tag = ET.SubElement(link, 'type')
    type_tag.text = '1'
    location = ET.SubElement(link, 'locationURI')
    location.text = f'PARENT-5-PROJECT_LOC/{sdk_driver_path}'
    print(f'Added link for {sdk_driver_file} with locationURI {location.text}')

    # Add all other .c files in the src directory to user_app folder
    for root_dir, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.c') and file not in ['user_custs1_def.c', 'user_custs_config.c', 'user_periph_setup.c']:
                relative_path = os.path.relpath(os.path.join(root_dir, file), project_root)
                if 'src' in relative_path:
                    link = ET.SubElement(linked_resources, 'link')
                    name = ET.SubElement(link, 'name')
                    name.text = f'user_app/{file}'
                    type_tag = ET.SubElement(link, 'type')
                    type_tag.text = '1'
                    location = ET.SubElement(link, 'locationURI')
                    location.text = f'PARENT-1-PROJECT_LOC/{relative_path.replace("\\", "/")}'
                    print(f'Added link for {file} with locationURI {location.text}')

    # Write the changes back to the file
    tree.write(file_path)
    print(f'Source file links have been added to {file_path}')

def process_projects(base_path):
    processed_projects = []
    
    for root_dir, dirs, files in os.walk(base_path):
        if 'e2studio' in dirs:
            project_name = get_project_name(root_dir)
            
            # Skip the 'prox_reporter' project
            if project_name == 'prox_reporter':
                print(f'Skipping project: {project_name}')
                continue
            
            e2studio_path = os.path.join(root_dir, 'e2studio')
            project_file = os.path.join(e2studio_path, '.project')
            
            if os.path.exists(project_file):
                print(f'Processing project: {project_name}')
                
                modify_project_name(project_file, project_name)
                remove_user_proxr(project_file)
                remove_user_periph_setup(project_file)
                
                # Adding source files from 'src' directory
                source_dir = os.path.join(root_dir, 'src')
                add_src_files(project_file, source_dir, root_dir)
                
                processed_projects.append(project_name)
    
    print('\nSummary of processed projects:')
    for project in processed_projects:
        print(f'- {project}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process projects in target_apps directory.')
    parser.add_argument('base_path', type=str, help='Base path to the target_apps directory')

    args = parser.parse_args()
    
    process_projects(args.base_path)
