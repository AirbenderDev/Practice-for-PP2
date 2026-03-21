# Move and Rename Files in Python

import os
import shutil

# Example 1: rename a file
with open("old.txt", "w") as f: f.write("hi")
os.rename("old.txt", "new.txt")
print("renamed:", os.path.exists("new.txt"))

# Example 2: move a file to another folder
os.makedirs("folder", exist_ok=True)
shutil.move("new.txt", "folder/new.txt")
print("moved:", os.path.exists("folder/new.txt"))

# Example 3: move and rename at the same time
with open("report.txt", "w") as f: f.write("data")
shutil.move("report.txt", "folder/report_2024.txt")
print("move+rename:", os.path.exists("folder/report_2024.txt"))

# Example 4: rename a folder
os.makedirs("old_folder", exist_ok=True)
os.rename("old_folder", "new_folder")
print("folder renamed:", os.path.exists("new_folder"))

# Example 5: move entire folder
os.makedirs("archive", exist_ok=True)
shutil.move("new_folder", "archive/new_folder")
print("folder moved:", os.path.exists("archive/new_folder"))

shutil.rmtree("folder")
shutil.rmtree("archive")
