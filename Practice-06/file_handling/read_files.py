# Read Files in Python

import os

# create a test file
with open("test.txt", "w") as f:
    f.write("Hello\nWorld\nPython\nIs\nCool")

# Example 1: read entire file
f = open("test.txt", "r")
print(f.read())
f.close()

# Example 2: read first 5 characters
f = open("test.txt", "r")
print(f.read(5))
f.close()

# Example 3: read one line
f = open("test.txt", "r")
print(f.readline())
f.close()

# Example 4: read all lines as a list
f = open("test.txt", "r")
print(f.readlines())
f.close()

# Example 5: read with 'with' (auto closes file)
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

os.remove("test.txt")
