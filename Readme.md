SDK e2studio Project Automation

This repository contains scripts to automate the creation and management of e2studio project folders for the DA145xx SDK. 


Main Script
The main_script.py is the entry point for running the project automation tasks. It copies the e2studio folder from a source project to all target projects and updates project names in the e2studio .project files.

Arguments
source_folder: Path to the source e2studio folder to be copied.
target_path: Path to the base directory containing the target projects.


Example
To run the script:


python main_script.py path/to/projects --update-xml --port-llvm



