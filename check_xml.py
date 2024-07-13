import xml.etree.ElementTree as ET
import difflib
import os

def xml_to_string(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return ET.tostring(root, encoding='unicode')

def compare_xml_files(file1, file2, output_file):
    xml_string1 = xml_to_string(file1)
    xml_string2 = xml_to_string(file2)

    diff = difflib.unified_diff(
        xml_string1.splitlines(keepends=True),
        xml_string2.splitlines(keepends=True),
        fromfile=file1,
        tofile=file2
    )

    with open(output_file, 'w') as f:
        f.writelines(diff)

    print(f"Differences have been written to {output_file}")

# Example usage
xml_file1 = 'file1.xml'
xml_file2 = 'file2.xml'
output_diff_file = 'differences.txt'

compare_xml_files(xml_file1, xml_file2, output_diff_file)
