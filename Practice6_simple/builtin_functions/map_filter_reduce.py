# map(), filter(), reduce()

from functools import reduce

nums = [1, 2, 3, 4, 5]

# --- MAP ---

# Example 1: double each number
print(list(map(lambda x: x * 2, nums)))

# Example 2: square each number
print(list(map(lambda x: x ** 2, nums)))

# Example 3: convert to strings
print(list(map(str, nums)))

# Example 4: uppercase each word
words = ["hello", "world", "python"]
print(list(map(str.upper, words)))

# Example 5: add two lists together
a = [1, 2, 3]
b = [10, 20, 30]
print(list(map(lambda x, y: x + y, a, b)))


# --- FILTER ---

# Example 1: keep even numbers
print(list(filter(lambda x: x % 2 == 0, nums)))

# Example 2: keep numbers greater than 3
print(list(filter(lambda x: x > 3, nums)))

# Example 3: keep positive numbers
mixed = [-2, -1, 0, 1, 2]
print(list(filter(lambda x: x > 0, mixed)))

# Example 4: remove empty strings
items = ["apple", "", "banana", "", "cherry"]
print(list(filter(None, items)))

# Example 5: keep words longer than 4 letters
words = ["cat", "elephant", "dog", "tiger"]
print(list(filter(lambda w: len(w) > 4, words)))


# --- REDUCE ---

# Example 1: sum all numbers
print(reduce(lambda a, b: a + b, nums))

# Example 2: multiply all numbers
print(reduce(lambda a, b: a * b, nums))

# Example 3: find the max
print(reduce(lambda a, b: a if a > b else b, nums))

# Example 4: join strings
words = ["Hello", "World", "Python"]
print(reduce(lambda a, b: a + " " + b, words))

# Example 5: count total characters
names = ["Ali", "Bob", "Charlie"]
print(reduce(lambda acc, n: acc + len(n), names, 0))
