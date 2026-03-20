# ============================================================
# enumerate_zip_examples.py
# Topic: enumerate() and zip() Built-in Functions
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
#         https://www.w3schools.com/python/ref_func_zip.asp
# ============================================================
# According to W3Schools:
#   enumerate(iterable, start=0)
#     — adds a counter to an iterable and returns it as an
#       enumerate object (pairs of index, value)
#   zip(*iterables)
#     — aggregates elements from multiple iterables into tuples.
#       Stops at the shortest iterable.
# ============================================================

# ============================================================
#  ENUMERATE — 5 Examples
# ============================================================
print("=" * 50)
print("ENUMERATE EXAMPLES")
print("=" * 50)

# Enumerate Example 1: Basic index + value loop
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
print("\n-- Enumerate Ex 1: Basic index and value --")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Enumerate Example 2: Start counter from a custom number
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
# The optional 'start' parameter sets the beginning index.
print("\n-- Enumerate Ex 2: Start counter from 1 --")
tasks = ["Design UI", "Write backend", "Test APIs", "Deploy", "Monitor"]
for num, task in enumerate(tasks, start=1):
    print(f"  Task {num}: {task}")

# Enumerate Example 3: Number lines while reading a list
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
print("\n-- Enumerate Ex 3: Numbered lines (like a file reader) --")
lines = [
    "First line of the document.",
    "Second line goes here.",
    "Third line ends the section.",
    "Fourth line wraps up.",
    "Fifth and final line.",
]
for lineno, text in enumerate(lines, start=1):
    print(f"  Line {lineno:02d}: {text}")

# Enumerate Example 4: Find the index of a specific item
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
print("\n-- Enumerate Ex 4: Find index of a specific value --")
scores = [85, 92, 78, 95, 88]
target = 95
for i, score in enumerate(scores):
    if score == target:
        print(f"  Score {target} found at index {i}")

# Enumerate Example 5: Create a numbered dictionary from a list
# Source: https://www.w3schools.com/python/ref_func_enumerate.asp
print("\n-- Enumerate Ex 5: Build a numbered dictionary --")
colors = ["red", "green", "blue", "yellow", "purple"]
color_dict = {i: color for i, color in enumerate(colors, start=1)}
print(f"  {color_dict}")


# ============================================================
#  ZIP — 5 Examples
# ============================================================
print("\n" + "=" * 50)
print("ZIP EXAMPLES")
print("=" * 50)

# Zip Example 1: Pair two lists together
# Source: https://www.w3schools.com/python/ref_func_zip.asp
print("\n-- Zip Ex 1: Pair names with scores --")
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 95, 72, 90, 85]
paired = list(zip(names, scores))
for name, score in paired:
    print(f"  {name}: {score}")

# Zip Example 2: Zip three lists at once
# Source: https://www.w3schools.com/python/ref_func_zip.asp
print("\n-- Zip Ex 2: Zip three lists together --")
subjects = ["Math", "Science", "English", "History", "Art"]
teachers = ["Mr. A", "Ms. B", "Mr. C", "Ms. D", "Mr. E"]
rooms    = [101, 202, 303, 404, 505]
for subject, teacher, room in zip(subjects, teachers, rooms):
    print(f"  {subject} — {teacher} — Room {room}")

# Zip Example 3: Create a dictionary from two lists using zip()
# Source: https://www.w3schools.com/python/ref_func_zip.asp
print("\n-- Zip Ex 3: Build a dictionary from two lists --")
keys = ["name", "age", "city", "job", "hobby"]
values = ["Jordan", 28, "Almaty", "Developer", "Cycling"]
profile = dict(zip(keys, values))
print(f"  {profile}")

# Zip Example 4: Compute element-wise sum of two lists
# Source: https://www.w3schools.com/python/ref_func_zip.asp
print("\n-- Zip Ex 4: Element-wise addition of two lists --")
prices    = [10.0, 25.5, 8.0, 15.0, 5.5]
discounts = [1.0,  2.5,  0.5, 3.0,  0.5]
final_prices = [p - d for p, d in zip(prices, discounts)]
print(f"  Prices:       {prices}")
print(f"  Discounts:    {discounts}")
print(f"  Final prices: {final_prices}")

# Zip Example 5: Unzip (transpose) a list of tuples using zip(*...)
# Source: https://www.w3schools.com/python/ref_func_zip.asp
# zip(*zipped) reverses the zipping and separates the columns.
print("\n-- Zip Ex 5: Unzip (transpose) pairs back into separate lists --")
coordinates = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
x_vals, y_vals = zip(*coordinates)
print(f"  Zipped:  {coordinates}")
print(f"  X values: {list(x_vals)}")
print(f"  Y values: {list(y_vals)}")
