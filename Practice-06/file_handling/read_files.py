# ============================================================
# read_files.py
# Topic: Reading Files in Python
# Source: https://www.w3schools.com/python/python_file_open.asp
# ============================================================
# According to W3Schools, the key function for working with
# files in Python is the open() function.
# Syntax: open(filename, mode)
# Common read modes:
#   "r"  - Read (default) — error if file does not exist
#   "rb" - Read in binary mode
# ============================================================

import os

# Helper: create a temp file for demos
def create_sample_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

sample = "sample.txt"
create_sample_file(sample, "Hello, World!\nPython is awesome.\nLine three here.\nLine four.\nLine five.")

# ------------------------------------------------------------
# Example 1: Read the entire file using read()
# Source: https://www.w3schools.com/python/python_file_open.asp
# read() returns the whole file content as a single string.
# ------------------------------------------------------------
print("=== Example 1: read() — entire file ===")
f = open(sample, "r")
content = f.read()
print(content)
f.close()

# ------------------------------------------------------------
# Example 2: Read only a specific number of characters
# Source: https://www.w3schools.com/python/ref_file_read.asp
# read(n) returns the first n bytes/characters from the file.
# ------------------------------------------------------------
print("\n=== Example 2: read(n) — first 13 characters ===")
f = open(sample, "r")
partial = f.read(13)
print(partial)
f.close()

# ------------------------------------------------------------
# Example 3: Read one line at a time using readline()
# Source: https://www.w3schools.com/python/ref_file_readline.asp
# readline() returns one line from the file each time it is called.
# ------------------------------------------------------------
print("\n=== Example 3: readline() — one line at a time ===")
f = open(sample, "r")
print(f.readline())   # First line
print(f.readline())   # Second line
f.close()

# ------------------------------------------------------------
# Example 4: Read all lines into a list using readlines()
# Source: https://www.w3schools.com/python/python_file_open.asp
# readlines() returns a list where each element is a line.
# ------------------------------------------------------------
print("\n=== Example 4: readlines() — list of all lines ===")
f = open(sample, "r")
lines = f.readlines()
for line in lines:
    print(line.strip())
f.close()

# ------------------------------------------------------------
# Example 5: Read a file using 'with' statement (recommended)
# Source: https://www.w3schools.com/python/python_file_open.asp
# The 'with' block automatically closes the file when done.
# No need to call f.close() explicitly.
# ------------------------------------------------------------
print("\n=== Example 5: Using 'with' statement (best practice) ===")
with open(sample, "r") as f:
    for line in f:
        print(line.strip())

# Cleanup
os.remove(sample)
