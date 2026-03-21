# Create and List Directories in Python

import os
import shutil

# Example 1: create a folder
os.mkdir("my_folder")
print("created:", os.path.exists("my_folder"))

# Example 2: create nested folders
os.makedirs("a/b/c", exist_ok=True)
print("nested created:", os.path.exists("a/b/c"))

# Example 3: list contents of a folder
with open("my_folder/file1.txt", "w") as f: f.write("")
with open("my_folder/file2.txt", "w") as f: f.write("")
print(os.listdir("my_folder"))

# Example 4: get current directory
print(os.getcwd())

# Example 5: list only files (skip folders)
os.makedirs("my_folder/sub", exist_ok=True)
entries = os.listdir("my_folder")
files_only = [e for e in entries if os.path.isfile(os.path.join("my_folder", e))]
print("files only:", files_only)

shutil.rmtree("my_folder")
shutil.rmtree("a")
