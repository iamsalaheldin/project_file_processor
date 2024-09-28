# Project File Processor

This repository contains a Python script, `project_file_processor.py`, designed to process all files in a specified project directory. The script reads each file's content, ignores certain file types (e.g., `.html`), and saves the details (file names, paths, and contents) into a single text file. The script also includes robust logging, error handling for file encodings, and flexible file filtering by extensions.

## Features

- **Processes all files** in a given directory, reads their contents, and outputs them into a text file.
- Supports ignoring certain file types based on extension (e.g., `.html`, `.class`, etc.).
- **Chunked reading for large files** to prevent memory overload.
- **Logs warnings and info messages** during execution, making it easier to monitor the script's progress.
- Customizable via **command-line arguments**, allowing users to specify project paths, output files, and extensions to ignore.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system. You can download it [here](https://www.python.org/downloads/).

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. Navigate to the directory:

    ```bash
    cd your-repo-name
    ```

## Usage

The script can be run via the command line. Below are the steps to use the script.

### Step 1: Basic Command

You can run the script by providing the path to the project you want to process and the path to the output file:

```bash
python scripts/project_file_processor.py <project_path> <output_file>
