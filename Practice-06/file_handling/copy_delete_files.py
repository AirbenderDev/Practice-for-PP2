# ============================================================
# copy_delete_files.py
# Topic: Copying and Deleting Files in Python
# Source: https://www.w3schools.com/python/python_file_remove.asp
#         https://www.w3schools.com/python/module_shutil.asp
# ============================================================
# According to W3Schools:
#   - Use the os module to delete files with os.remove()
#   - Use os.path.exists() to check if a file exists before deleting
#   - Use the shutil module to copy files
# ============================================================

import os
import shutil

# Helper
def make_file(name, text="Sample content.\n"):
    with open(name, "w") as f:
        f.write(text)

# ------------------------------------------------------------
# Example 1: Delete a file using os.remove()
# Source: https://www.w3schools.com/python/python_file_remove.asp
# os.remove() deletes the specified file.
# ------------------------------------------------------------
print("=== Example 1: os.remove() — delete a file ===")
make_file("delete_me.txt")
print("Before delete:", os.path.exists("delete_me.txt"))
os.remove("delete_me.txt")
print("After delete:", os.path.exists("delete_me.txt"))

# ------------------------------------------------------------
# Example 2: Check if file exists before deleting (safe delete)
# Source: https://www.w3schools.com/python/python_file_remove.asp
# To avoid errors, check with os.path.exists() first.
# ------------------------------------------------------------
print("\n=== Example 2: Safe delete with os.path.exists() ===")
filename = "maybe_exists.txt"
if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} was deleted.")
else:
    print(f"{filename} does not exist — nothing to delete.")

# ------------------------------------------------------------
# Example 3: Copy a file using shutil.copy()
# Source: https://www.w3schools.com/python/module_shutil.asp
# shutil.copy(src, dst) copies a file from src to dst.
# ------------------------------------------------------------
print("\n=== Example 3: shutil.copy() — copy a file ===")
make_file("original.txt", "This is the original file.\n")
shutil.copy("original.txt", "copy_of_original.txt")
print("Original exists:", os.path.exists("original.txt"))
print("Copy exists:", os.path.exists("copy_of_original.txt"))
with open("copy_of_original.txt", "r") as f:
    print("Copy content:", f.read())

# ------------------------------------------------------------
# Example 4: Copy and rename a file at the same time
# Source: https://www.w3schools.com/python/module_shutil.asp
# Simply pass a new name as the destination in shutil.copy().
# ------------------------------------------------------------
print("\n=== Example 4: Copy and rename simultaneously ===")
make_file("report.txt", "Annual report data.\n")
shutil.copy("report.txt", "report_backup_2024.txt")
print("Renamed copy exists:", os.path.exists("report_backup_2024.txt"))
with open("report_backup_2024.txt", "r") as f:
    print("Content:", f.read())

# ------------------------------------------------------------
# Example 5: Copy a file then delete the original (manual move)
# Source: https://www.w3schools.com/python/python_file_remove.asp
# Copy first, verify the copy, then remove the source.
# ------------------------------------------------------------
print("\n=== Example 5: Manual move (copy + delete original) ===")
make_file("source.txt", "Moving this file.\n")
shutil.copy("source.txt", "destination.txt")
if os.path.exists("destination.txt"):
    os.remove("source.txt")
    print("source.txt deleted after copy.")
    print("destination.txt exists:", os.path.exists("destination.txt"))

# Cleanup
for f in ["original.txt", "copy_of_original.txt", "report.txt",
          "report_backup_2024.txt", "destination.txt"]:
    if os.path.exists(f):
        os.remove(f)
