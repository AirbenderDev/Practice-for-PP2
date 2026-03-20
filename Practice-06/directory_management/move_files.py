# ============================================================
# move_files.py
# Topic: Moving and Renaming Files/Directories in Python
# Source: https://www.w3schools.com/python/module_shutil.asp
#         https://www.w3schools.com/python/module_os.asp
# ============================================================
# According to W3Schools:
#   - shutil.move(src, dst) moves a file or directory
#   - os.rename(src, dst)   renames a file or directory
# Both can be used to relocate files within the filesystem.
# ============================================================

import os
import shutil

# Helper
def make_file(path, text="content"):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w") as f:
        f.write(text)

# ------------------------------------------------------------
# Example 1: Rename a file using os.rename()
# Source: https://www.w3schools.com/python/module_os.asp
# os.rename(old_name, new_name) renames the file.
# ------------------------------------------------------------
print("=== Example 1: os.rename() — rename a file ===")
make_file("old_name.txt", "Renaming demo.")
os.rename("old_name.txt", "new_name.txt")
print("old_name.txt exists:", os.path.exists("old_name.txt"))
print("new_name.txt exists:", os.path.exists("new_name.txt"))

# ------------------------------------------------------------
# Example 2: Move a file to another directory using shutil.move()
# Source: https://www.w3schools.com/python/module_shutil.asp
# shutil.move(src, dst) moves src to the dst location.
# ------------------------------------------------------------
print("\n=== Example 2: shutil.move() — move file to another folder ===")
os.makedirs("destination_folder", exist_ok=True)
make_file("file_to_move.txt", "Moving me!")
shutil.move("file_to_move.txt", "destination_folder/file_to_move.txt")
print("Original exists:", os.path.exists("file_to_move.txt"))
print("Moved file exists:", os.path.exists("destination_folder/file_to_move.txt"))

# ------------------------------------------------------------
# Example 3: Move AND rename a file in one step with shutil.move()
# Source: https://www.w3schools.com/python/module_shutil.asp
# Provide a new filename in the destination path to rename while moving.
# ------------------------------------------------------------
print("\n=== Example 3: Move + rename in one step ===")
make_file("report.txt", "Annual report.")
shutil.move("report.txt", "destination_folder/report_2024.txt")
print("New location exists:", os.path.exists("destination_folder/report_2024.txt"))

# ------------------------------------------------------------
# Example 4: Rename a directory with os.rename()
# Source: https://www.w3schools.com/python/module_os.asp
# os.rename() works on directories just like files.
# ------------------------------------------------------------
print("\n=== Example 4: Rename a directory ===")
os.makedirs("old_folder", exist_ok=True)
os.rename("old_folder", "renamed_folder")
print("old_folder exists:", os.path.exists("old_folder"))
print("renamed_folder exists:", os.path.exists("renamed_folder"))

# ------------------------------------------------------------
# Example 5: Move an entire directory using shutil.move()
# Source: https://www.w3schools.com/python/module_shutil.asp
# shutil.move() can relocate whole directories, not just files.
# ------------------------------------------------------------
print("\n=== Example 5: Move an entire directory ===")
os.makedirs("source_dir/data", exist_ok=True)
make_file("source_dir/info.txt", "dir content")
os.makedirs("archive", exist_ok=True)
shutil.move("source_dir", "archive/source_dir")
print("source_dir at root:", os.path.exists("source_dir"))
print("source_dir in archive:", os.path.exists("archive/source_dir"))

# Cleanup
for path in ["new_name.txt", "destination_folder", "renamed_folder", "archive"]:
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)
