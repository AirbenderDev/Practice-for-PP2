# ============================================================
# create_list_dirs.py
# Topic: Creating and Listing Directories in Python
# Source: https://www.w3schools.com/python/module_os.asp
# ============================================================
# According to W3Schools, the os module provides functions for
# interacting with the operating system, including creating and
# listing directories.
# Key functions:
#   os.mkdir()    — create a single directory
#   os.makedirs() — create nested directories
#   os.listdir()  — list contents of a directory
#   os.getcwd()   — get current working directory
# ============================================================

import os
import shutil

# ------------------------------------------------------------
# Example 1: Create a single directory with os.mkdir()
# Source: https://www.w3schools.com/python/module_os.asp
# os.mkdir() creates one directory at the given path.
# ------------------------------------------------------------
print("=== Example 1: os.mkdir() — create one directory ===")
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
print("my_folder created:", os.path.exists("my_folder"))

# ------------------------------------------------------------
# Example 2: Create nested (multi-level) directories with os.makedirs()
# Source: https://www.w3schools.com/python/module_os.asp
# os.makedirs() creates all intermediate-level directories.
# ------------------------------------------------------------
print("\n=== Example 2: os.makedirs() — nested directories ===")
nested_path = "parent/child/grandchild"
os.makedirs(nested_path, exist_ok=True)
print("Nested path created:", os.path.exists(nested_path))

# ------------------------------------------------------------
# Example 3: List directory contents with os.listdir()
# Source: https://www.w3schools.com/python/module_os.asp
# os.listdir(path) returns a list of entries in the directory.
# ------------------------------------------------------------
print("\n=== Example 3: os.listdir() — list a directory ===")
# Add some files to list
with open("my_folder/file1.txt", "w") as f: f.write("a")
with open("my_folder/file2.txt", "w") as f: f.write("b")
contents = os.listdir("my_folder")
print("Contents of my_folder:", contents)

# ------------------------------------------------------------
# Example 4: Get the current working directory with os.getcwd()
# Source: https://www.w3schools.com/python/module_os.asp
# os.getcwd() returns the full path of the current directory.
# ------------------------------------------------------------
print("\n=== Example 4: os.getcwd() — current working directory ===")
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# ------------------------------------------------------------
# Example 5: List only files (not subdirectories) in a directory
# Source: https://www.w3schools.com/python/module_os.asp
# Combine os.listdir() with os.path.isfile() to filter results.
# ------------------------------------------------------------
print("\n=== Example 5: List only files inside a directory ===")
os.makedirs("mixed_folder/sub", exist_ok=True)
with open("mixed_folder/notes.txt", "w") as f: f.write("note")
with open("mixed_folder/data.csv", "w") as f: f.write("csv")

all_entries = os.listdir("mixed_folder")
only_files = [e for e in all_entries if os.path.isfile(os.path.join("mixed_folder", e))]
print("All entries:", all_entries)
print("Only files:", only_files)

# Cleanup
shutil.rmtree("my_folder", ignore_errors=True)
shutil.rmtree("parent", ignore_errors=True)
shutil.rmtree("mixed_folder", ignore_errors=True)
