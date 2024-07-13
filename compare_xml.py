import xml.etree.ElementTree as ET
import difflib
import os
import sys
import shutil

def xml_to_string(xml_file):
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"The file {xml_file} does not exist.")
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return ET.tostring(root, encoding='unicode')

def compare_xml_files(file1, file2, output_file):
    try:
        xml_string1 = xml_to_string(file1)
        xml_string2 = xml_to_string(file2)
    except FileNotFoundError as e:
        print(e)
        return

    diff = difflib.unified_diff(
        xml_string1.splitlines(keepends=True),
        xml_string2.splitlines(keepends=True),
        fromfile=file1,
        tofile=file2
    )

    with open(output_file, 'w') as f:
        f.writelines(diff)

    print(f"Differences have been written to {output_file}")

def update_latest_version(latest_file, new_version):
    shutil.copyfile(new_version, latest_file)
    print(f"Updated latest version file to {latest_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python compare_xml.py <file1> <file2> <output_file>")
        sys.exit(1)

    # Define file paths
    default_file = sys.argv[1]
    project_file = sys.argv[2]
    output_diff_file = sys.argv[3]

    # Define the latest version tracking file
    latest_version_file = 'latest_version.xml'

    # Check if latest version file exists; if not, use the default file
    if not os.path.exists(latest_version_file):
        shutil.copyfile(default_file, latest_version_file)
        print(f"Initialized latest version file with {default_file}")

    # Compare the project file with the latest version
    compare_xml_files(latest_version_file, project_file, output_diff_file)

    # Update the latest version file
    update_latest_version(latest_version_file, project_file)
