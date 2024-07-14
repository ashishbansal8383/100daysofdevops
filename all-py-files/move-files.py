import os
import shutil

def move_python_files(current_path):
    target_folder = os.path.join(current_path, 'all-py-files')

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # List all files in the current directory
    for file in os.listdir(current_path):
        if file.endswith('.py'):
            # Construct full file path
            file_path = os.path.join(current_path, file)
            # Move file to target folder
            shutil.move(file_path, target_folder)
            print(f'Moved: {file_path} to {target_folder}')

if __name__ == '__main__':
    # Use '.' for current directory
    current_path = '.'
    move_python_files(current_path)