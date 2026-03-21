# Copy and Delete Files in Python

import os
import shutil

# Example 1: delete a file
with open("a.txt", "w") as f: f.write("hi")
os.remove("a.txt")
print("deleted")

# Example 2: check before deleting (safe delete)
if os.path.exists("a.txt"):
    os.remove("a.txt")
else:
    print("file not found")

# Example 3: copy a file
with open("original.txt", "w") as f: f.write("hello")
shutil.copy("original.txt", "copy.txt")
print("copied:", os.path.exists("copy.txt"))

# Example 4: copy and rename
shutil.copy("original.txt", "renamed_copy.txt")
print("renamed copy exists:", os.path.exists("renamed_copy.txt"))

# Example 5: copy then delete original
shutil.copy("original.txt", "moved.txt")
os.remove("original.txt")
print("original gone:", not os.path.exists("original.txt"))

os.remove("copy.txt")
os.remove("renamed_copy.txt")
os.remove("moved.txt")
