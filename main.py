import os
import shutil
import time
from tqdm import tqdm

chemin = input("Give the desired directory to sort out")

# Specify your download directory
download_directory = chemin

# Dictionary mapping file extensions to corresponding subdirectories
file_type_mapping = {
    'pdf': 'pdf',
    'jpg': 'images/JPEG',
    'jpeg': 'images/JPEG',
    'png': 'images',
    'mp4': 'videos',
    'docx': 'Documents',
    'xlsx': 'Documents',
    'pptx': 'Powerpoints',
    'stl': '3D_models',
    '3mf': '3D_models',
    'f3d': '3D_models',
    'stp': '3D_models/STEP',
    'step': '3D_models/STEP',
    'exe': 'Executables'
    # Add more file types and corresponding subdirectories as needed
}

def organize_files():
    files_to_sort = []

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

            pbar.update(1)

    print("Sorting complete.")

if __name__ == "__main__":
    organize_files()
