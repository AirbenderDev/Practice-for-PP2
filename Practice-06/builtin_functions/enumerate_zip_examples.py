# enumerate() and zip()

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
scores = [88, 95, 72, 90, 85]
names  = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# --- ENUMERATE ---

# Example 1: print index and value
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Example 2: start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# Example 3: find index of a specific item
for i, fruit in enumerate(fruits):
    if fruit == "cherry":
        print("cherry is at index", i)

# Example 4: number a list of tasks
tasks = ["Buy food", "Study", "Exercise"]
for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}")

# Example 5: make a dictionary from enumerated list
result = {i: fruit for i, fruit in enumerate(fruits, 1)}
print(result)


# --- ZIP ---

# Example 1: pair two lists
for name, score in zip(names, scores):
    print(name, score)

# Example 2: zip three lists
cities = ["NYC", "LA", "Chicago", "Houston", "Phoenix"]
for name, score, city in zip(names, scores, cities):
    print(name, score, city)

# Example 3: make a dictionary from two lists
d = dict(zip(names, scores))
print(d)

# Example 4: element-wise addition
a = [1, 2, 3]
b = [10, 20, 30]
print([x + y for x, y in zip(a, b)])

# Example 5: unzip a list of pairs
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(list(nums))
print(list(letters))
