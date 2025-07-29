import os
import shutil
from filetypes import FILE_TYPES

def move_file(file_path, target_folder):
    base = os.path.basename(file_path)
    target_path = os.path.join(target_folder, base)

    # Avoid overwriting
    count = 1
    while os.path.exists(target_path):
        name, ext = os.path.splitext(base)
        new_name = f"{name}_{count}{ext}"
        target_path = os.path.join(target_folder, new_name)
        count += 1

    shutil.move(file_path, target_path)

def categorize_and_move(file_path, base_dir):
    _, ext = os.path.splitext(file_path)
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            folder = os.path.join(base_dir, category)
            os.makedirs(folder, exist_ok=True)
            move_file(file_path, folder)
            print(f"Moved {file_path} to {folder}")
            return
