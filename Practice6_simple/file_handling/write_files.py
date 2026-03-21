# Write Files in Python

import os

# Example 1: write to a file (creates it if not exists)
f = open("test.txt", "w")
f.write("Hello World")
f.close()

# Example 2: overwrite existing content
f = open("test.txt", "w")
f.write("New content only")
f.close()

# Example 3: append to a file
f = open("test.txt", "a")
f.write("\nThis line is added")
f.close()

# Example 4: write multiple lines at once
lines = ["line 1\n", "line 2\n", "line 3\n"]
with open("test.txt", "w") as f:
    f.writelines(lines)

# Example 5: create a new file with "x" (fails if file exists)
if os.path.exists("new.txt"):
    os.remove("new.txt")
with open("new.txt", "x") as f:
    f.write("brand new file")

print("Done!")

os.remove("test.txt")
os.remove("new.txt")
