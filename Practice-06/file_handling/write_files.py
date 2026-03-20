# ============================================================
# write_files.py
# Topic: Writing / Creating Files in Python
# Source: https://www.w3schools.com/python/python_file_write.asp
# ============================================================
# According to W3Schools, to write to an existing file you must
# add a mode parameter to the open() function:
#   "w"  - Write — overwrites existing content; creates file if absent
#   "a"  - Append — adds to the end; creates file if absent
#   "x"  - Create — creates a new file; error if file already exists
# ============================================================

import os

# ------------------------------------------------------------
# Example 1: Write to a file with "w" mode (overwrite)
# Source: https://www.w3schools.com/python/python_file_write.asp
# "w" will OVERWRITE the file if it already exists.
# ------------------------------------------------------------
print("=== Example 1: write() with 'w' mode ===")
with open("demo1.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("This is the first write.\n")

with open("demo1.txt", "r") as f:
    print(f.read())

# ------------------------------------------------------------
# Example 2: Append to a file with "a" mode
# Source: https://www.w3schools.com/python/python_file_write.asp
# "a" adds text at the END without deleting the existing content.
# ------------------------------------------------------------
print("=== Example 2: write() with 'a' (append) mode ===")
with open("demo1.txt", "a") as f:
    f.write("This line was appended.\n")

with open("demo1.txt", "r") as f:
    print(f.read())

# ------------------------------------------------------------
# Example 3: Create a brand new file with "x" mode
# Source: https://www.w3schools.com/python/python_file_write.asp
# "x" creates the file — raises FileExistsError if it exists.
# ------------------------------------------------------------
print("=== Example 3: Create new file with 'x' mode ===")
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")

with open("new_file.txt", "x") as f:
    f.write("Brand new file created with 'x' mode!\n")

with open("new_file.txt", "r") as f:
    print(f.read())

# ------------------------------------------------------------
# Example 4: Write multiple lines using writelines()
# Source: https://www.w3schools.com/python/ref_file_writelines.asp
# writelines() writes a list of strings to the file at once.
# ------------------------------------------------------------
print("=== Example 4: writelines() — write a list of lines ===")
lines = ["First line\n", "Second line\n", "Third line\n", "Fourth line\n", "Fifth line\n"]
with open("demo2.txt", "w") as f:
    f.writelines(lines)

with open("demo2.txt", "r") as f:
    print(f.read())

# ------------------------------------------------------------
# Example 5: Overwrite an existing file to update its content
# Source: https://www.w3schools.com/python/python_file_write.asp
# Opening with "w" again completely replaces the old content.
# ------------------------------------------------------------
print("=== Example 5: Overwrite existing file content ===")
with open("demo2.txt", "w") as f:
    f.write("File has been completely overwritten.\n")

with open("demo2.txt", "r") as f:
    print(f.read())

# Cleanup
for fname in ["demo1.txt", "new_file.txt", "demo2.txt"]:
    if os.path.exists(fname):
        os.remove(fname)
