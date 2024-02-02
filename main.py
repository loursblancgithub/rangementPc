import os
import shutil
import time
from tqdm import tqdm

def clean_path(path):
    # Remove surrounding quotes
    path = path.strip('"')

    # Replace backslashes with forward slashes
    path = path.replace('\\', '/')

    return path

# Prompt the user for the download directory
download_directory = input("Enter the path to the download directory: ")
download_directory = clean_path(download_directory)

# Dictionary mapping file extensions to corresponding subdirectories
file_type_mapping = {
    'pdf': 'pdf',
    'jpg': 'images',
    'jpeg': 'images',
    'png': 'images',
    'mp4': 'videos',
    'docx': 'Documents',
    'xlsx': 'Documents',
    'pptx': 'Documents',
    'odp': 'Documents',
    'txt': 'text_files',
    'md': 'text_files',
    'log': 'text_files',
    'zip': 'archives',
    'rar': 'archives',
    'gz': 'archives',
    'csv': 'spreadsheets',
    'json': 'data_files',
    'xml': 'data_files',
    'html': 'web_pages',
    'exe': 'executables',
    'py': 'code_files',
    'java': 'code_files',
    'cpp': 'code_files',
    'js': 'code_files',
    'bat': 'scripts',
    'sh': 'scripts',
    'iso': 'disk_images',
    'img': 'disk_images',
    'bak': 'backup_files',
    'dll': 'dynamic_libraries',
    'psd': 'design_files',
    'ai': 'design_files',
    'mp3': 'audio_files',
    'wav': 'audio_files',
    'avi': 'videos',
    'mov': 'videos',
    'flv': 'videos',
    'svg': 'vector_graphics',
    'ics': 'calendar_files',
    'dxf': 'CAD_files',
    'webp': 'images',
    'tex': 'LaTeX_files',
    'deb': 'system_packages',
    'rpm': 'system_packages',
    'tgz': 'compressed_packages',
    'bz2': 'compressed_packages',
    'jar': 'java_archives',
    # Add more file types and corresponding subdirectories as needed
}

def organize_files():
    files_to_sort = []
    unclassified_files = []

    for filename in os.listdir(download_directory):
        file_path = os.path.join(download_directory, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            files_to_sort.append(file_path)

    total_files = len(files_to_sort)

    with tqdm(total=total_files, desc="Sorting Files", unit="file") as pbar:
        for file_path in files_to_sort:
            # Get the file extension
            _, file_extension = os.path.splitext(file_path)
            file_extension = file_extension.lower()[1:]  # Remove the dot and convert to lowercase

            # Check if the file type is in the mapping
            if file_extension in file_type_mapping:
                destination_folder = file_type_mapping[file_extension]
                destination_path = os.path.join(download_directory, destination_folder)

                # Create the subdirectory if it doesn't exist
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                # Move the file to the corresponding subdirectory
                shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))

            else:
                # If the file extension is not in the mapping, move it to the 'bulk' directory
                unclassified_files.append(file_path)

        # Create the 'bulk' directory if it doesn't exist
        bulk_directory = os.path.join(download_directory, 'bulk')
        if not os.path.exists(bulk_directory):
            os.makedirs(bulk_directory)

        # Move unclassified files to the 'bulk' directory
        for file_path in unclassified_files:
            shutil.move(file_path, os.path.join(bulk_directory, os.path.basename(file_path)))

            pbar.update(1)

    print("Sorting complete.")

if __name__ == "__main__":
    organize_files()
