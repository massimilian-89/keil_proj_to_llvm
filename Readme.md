
# Project Automation Scripts

This repository contains scripts designed to automate the process of updating XML files and porting LLVM projects. The two main scripts provided are `update_xml` and `port_llvm_script`, which perform various tasks on projects located within a specified directory structure.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Running the Main Script](#running-the-main-script)
  - [update_xml Module](#update_xml-module)
  - [port_llvm_script Module](#port_llvm_script-module)
- [Script Descriptions](#script-descriptions)
  - [main.py](#mainpy)
  - [update_xml.py](#update_xmlpy)
  - [port_llvm_script.py](#port_llvm_scriptpy)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/project-automation-scripts.git
   cd project-automation-scripts
   ```

2. Ensure you have Python 3 installed. You can check your Python version by running:

   ```bash
   python --version
   ```

3. Install any required packages (if applicable):

   ```bash
   pip install -r requirements.txt
   ```


## Usage

### Running the Main Script

The main script is `main.py`, which acts as an entry point to trigger the `update_xml` and `port_llvm_script` functions.

```bash
python main.py <target_path> [--update-xml] [--port-llvm]
```

- `<target_path>`: Path to the base directory containing your projects.
- `--update-xml`: Flag to trigger XML updates using the `update_xml` module.
- `--port-llvm`: Flag to port LLVM projects using the `port_llvm_script` module.

### Example:

```bash
python main.py /path/to/projects --update-xml --port-llvm
```

### update_xml Module

The `update_xml.py` script processes XML files within projects to modify project names, remove certain linked resources, and add new source file links.

#### Command:

```bash
python update_xml.py <base_path>
```

- `<base_path>`: Path to the `target_apps` directory where projects are located.

### port_llvm_script Module

The `port_llvm_script.py` script copies the `e2studio` folder to all projects containing `Keil_5` and `src` directories and edits the project name within the `.project` file.

#### Command:

```bash
python port_llvm_script.py
```

This script does not require additional arguments when called directly, as it is typically invoked through the main script.

## Script Descriptions

### `main.py`

The `main.py` script combines the functionality of both `update_xml` and `port_llvm_script`. It accepts a target directory path and flags to determine which operations to perform. It handles directory traversal, checks for the existence of required directories, and invokes the appropriate functions based on user input.

### `update_xml.py`

This script handles modifications to the `.project` XML files within projects.


### `port_llvm_script.py`

This script copies the `e2studio` folder from a source location to projects containing specific directories (`Keil_5` and `src`). It also updates the project name within the `.project` XML file to match the directory name.

