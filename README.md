Project File Processor
This repository contains a Python script, project_file_processor.py, designed to process all files in a specified project directory. The script reads each file's content, ignores certain file types (e.g., .html), and saves the details (file names, paths, and contents) into a single text file. The script also includes robust logging, error handling for file encodings, and flexible file filtering by extensions.

Features
Processes all files in a given directory, reads their contents, and outputs them into a text file.
Supports ignoring certain file types based on extension (e.g., .html, .class, etc.).
Chunked reading for large files to prevent memory overload.
Logs warnings and info messages during execution, making it easier to monitor the script's progress.
Customizable via command-line arguments, allowing users to specify project paths, output files, and extensions to ignore.
Getting Started
Prerequisites
Python 3.x: Ensure you have Python installed on your system. You can download it here.
Installing
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
Navigate to the directory:

bash
Copy code
cd your-repo-name
Usage
The script can be run via the command line. Below are the steps to use the script.

Step 1: Basic Command
You can run the script by providing the path to the project you want to process and the path to the output file:

bash
Copy code
python scripts/project_file_processor.py <project_path> <output_file>
Example:
bash
Copy code
python scripts/project_file_processor.py "C:\Users\asalaheldin\Projects\selfhealingframework\selfhealingframework" "project_content.txt"
This command will process all readable files in the specified project directory and output the details to project_content.txt.

Step 2: Ignoring Specific File Extensions
To ignore files with specific extensions (e.g., .html, .class), use the --ignore option:

bash
Copy code
python scripts/project_file_processor.py <project_path> <output_file> --ignore .html .class
Example:
bash
Copy code
python scripts/project_file_processor.py "C:\Users\asalaheldin\Projects\selfhealingframework\selfhealingframework" "project_content.txt" --ignore .html .class
This command will process the project but skip any .html or .class files.

Command-Line Arguments
<project_path>: The path to the project directory you want to process.
<output_file>: The path to the output text file where file details will be saved.
--ignore: (Optional) Specify file extensions to ignore. You can pass multiple extensions like .html, .class.
Logging
The script logs important information to the console using the logging module. It logs:

Info messages for file processing and completion.
Warning messages for unreadable files or files with encoding issues.
Sample Output
Here’s an example of what the output text file might look like:

mathematica
Copy code
File Name: example_file.py
File Path: C:\path\to\example_file.py
File Content:
<Contents of example_file.py>

================================================================================
File Name: another_file.txt
File Path: C:\path\to\another_file.txt
File Content:
<Contents of another_file.txt>

================================================================================
Error Handling
If the provided project path is invalid, the script will log an error and terminate.
Files with encoding issues or that cannot be read will be skipped, and the error will be logged.
Contribution
Feel free to fork this repository, submit issues, and create pull requests.

