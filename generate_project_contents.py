import os
import logging
import argparse

#How to run
#python generate_project_contents.py "C:\Users\asalaheldin\Projects\selfhealingframework\selfhealingframework" "project_content.txt" --ignore .html .class


# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Process Java project files.')
    parser.add_argument('project_path', type=str, help='Path to the project directory')
    parser.add_argument('output_file', type=str, help='Path to the output text file')
    parser.add_argument('--ignore', type=str, nargs='*', default=['.html'], help='File extensions to ignore')
    return parser.parse_args()

def is_readable_file(file_path):
    """Check if a file is readable by trying to open it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except (UnicodeDecodeError, IOError):
        logging.warning(f"Skipped unreadable or encoding issue file: {file_path}")
        return False

def should_ignore_file(file_name, extensions_to_ignore):
    """Check if the file should be ignored based on the extension."""
    return any(file_name.endswith(ext) for ext in extensions_to_ignore)

def process_file(file_path, file_name, output):
    """Process large files in chunks to prevent memory issues."""
    output.write(f"File Name: {file_name}\n")
    output.write(f"File Path: {file_path}\n")
    output.write("File Content:\n")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(1024)  # Read in 1KB chunks
                if not chunk:
                    break
                output.write(chunk)
    except UnicodeDecodeError:
        logging.warning(f"Encoding issue with file: {file_path}")
    
    output.write("\n" + "="*80 + "\n")

def process_project_directory(project_path, output_file, extensions_to_ignore):
    """Walk through project directory, process each file, and write details to output."""
    if not os.path.exists(project_path):
        logging.error(f"Error: The provided path {project_path} does not exist.")
        return

    with open(output_file, 'w', encoding='utf-8') as output:
        for root, _, files in os.walk(project_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                
                if should_ignore_file(file_name, extensions_to_ignore):
                    logging.info(f"Skipped file due to extension: {file_path}")
                    continue
                
                if is_readable_file(file_path):
                    process_file(file_path, file_name, output)
                else:
                    logging.warning(f"Skipped unreadable file: {file_path}")

    logging.info(f"Project content has been written to {output_file}")

# Main execution
if __name__ == "__main__":
    args = parse_arguments()
    process_project_directory(args.project_path, args.output_file, args.ignore)
