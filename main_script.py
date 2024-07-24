import os
import argparse
import update_xml
import port_llvm_script

def main():
    parser = argparse.ArgumentParser(description='Run update_xml and port_llvm_script functions.')
    parser.add_argument('target_path', type=str, help='Path to the target base directory')
    parser.add_argument('--update-xml', action='store_true', help='Update XML files')
    parser.add_argument('--port-llvm', action='store_true', help='Port LLVM projects')

    args = parser.parse_args()

    project_base_path = os.path.abspath(args.target_path)
    # Define the source folder path
    source_folder = os.path.join(project_base_path, 'target_apps', 'ble_examples', 'prox_reporter', 'e2studio')

    if not os.path.isdir(source_folder):
        print(f"The source folder {source_folder} does not exist.")
        return

    if args.port_llvm or args.update_xml:
        if args.port_llvm:
            print("Running LLVM porting...")
            
            # Ignore the host_apps folder if it exists
            subdirs = [os.path.join(project_base_path, d) for d in os.listdir(project_base_path) if os.path.isdir(os.path.join(project_base_path, d)) and d != 'host_apps']

            project_count = 0
            for subdir in subdirs:
                for root, dirs, files in os.walk(subdir):
                    if 'Keil_5' in dirs and 'src' in dirs:
                        project_count += 1
                        port_llvm_script.copy_e2studio_folder_to_projects(source_folder, root)
                        port_llvm_script.edit_project_name(root)

            print(f"Found {project_count} projects containing 'Keil_5' and 'src' directories")
        
        if args.update_xml:
            print("Running XML update...")
            update_xml.process_projects(args.target_path)
    else:
        print("Please specify at least one of the options: --update-xml or --port-llvm")

if __name__ == "__main__":
    main()
