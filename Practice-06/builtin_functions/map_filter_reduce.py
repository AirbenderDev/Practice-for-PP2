# ============================================================
# map_filter_reduce.py
# Topic: map(), filter(), and reduce() Built-in Functions
# Source: https://www.w3schools.com/python/ref_func_map.asp
#         https://www.w3schools.com/python/ref_func_filter.asp
#         https://www.w3schools.com/python/ref_func_reduce.asp
# ============================================================
# According to W3Schools:
#   map(func, iterable)    — applies func to every element
#   filter(func, iterable) — keeps elements where func returns True
#   reduce(func, iterable) — accumulates elements into a single value
#                            (must import from functools)
# ============================================================

from functools import reduce

# ============================================================
#  MAP — 5 Examples
# ============================================================
print("=" * 50)
print("MAP EXAMPLES")
print("=" * 50)

# Map Example 1: Square all numbers in a list
# Source: https://www.w3schools.com/python/ref_func_map.asp
print("\n-- Map Ex 1: Square each number --")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Input:  {numbers}")
print(f"Output: {squared}")

# Map Example 2: Convert a list of strings to uppercase
# Source: https://www.w3schools.com/python/ref_func_map.asp
print("\n-- Map Ex 2: Strings to uppercase --")
words = ["hello", "world", "python", "map", "function"]
uppercased = list(map(str.upper, words))
print(f"Input:  {words}")
print(f"Output: {uppercased}")

# Map Example 3: Convert Celsius to Fahrenheit
# Source: https://www.w3schools.com/python/ref_func_map.asp
print("\n-- Map Ex 3: Celsius → Fahrenheit --")
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(f"Celsius:    {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Map Example 4: Get the length of each string
# Source: https://www.w3schools.com/python/ref_func_map.asp
print("\n-- Map Ex 4: Length of each string --")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
lengths = list(map(len, fruits))
print(f"Fruits:  {fruits}")
print(f"Lengths: {lengths}")

# Map Example 5: Add corresponding elements from two lists
# Source: https://www.w3schools.com/python/ref_func_map.asp
print("\n-- Map Ex 5: Add elements from two lists --")
list_a = [10, 20, 30, 40, 50]
list_b = [1, 2, 3, 4, 5]
added = list(map(lambda a, b: a + b, list_a, list_b))
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Sums:   {added}")


# ============================================================
#  FILTER — 5 Examples
# ============================================================
print("\n" + "=" * 50)
print("FILTER EXAMPLES")
print("=" * 50)

# Filter Example 1: Keep only even numbers
# Source: https://www.w3schools.com/python/ref_func_filter.asp
print("\n-- Filter Ex 1: Keep even numbers --")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Input:  {nums}")
print(f"Evens:  {evens}")

# Filter Example 2: Keep only positive numbers
# Source: https://www.w3schools.com/python/ref_func_filter.asp
print("\n-- Filter Ex 2: Keep positive numbers --")
mixed = [-5, -3, 0, 2, 4, 7, -1, 9]
positives = list(filter(lambda x: x > 0, mixed))
print(f"Input:     {mixed}")
print(f"Positives: {positives}")

# Filter Example 3: Filter strings longer than 4 characters
# Source: https://www.w3schools.com/python/ref_func_filter.asp
print("\n-- Filter Ex 3: Strings longer than 4 chars --")
animals = ["cat", "elephant", "dog", "tiger", "ox", "kangaroo"]
long_names = list(filter(lambda s: len(s) > 4, animals))
print(f"Input:  {animals}")
print(f"Output: {long_names}")

# Filter Example 4: Remove None / falsy values from a list
# Source: https://www.w3schools.com/python/ref_func_filter.asp
print("\n-- Filter Ex 4: Remove falsy values (None, 0, '') --")
data = [1, None, "hello", 0, False, 42, "", "Python"]
clean = list(filter(None, data))
print(f"Input:  {data}")
print(f"Output: {clean}")

# Filter Example 5: Keep words that start with a vowel
# Source: https://www.w3schools.com/python/ref_func_filter.asp
print("\n-- Filter Ex 5: Words starting with a vowel --")
sentence = ["apple", "banana", "orange", "umbrella", "grape", "ice"]
vowel_words = list(filter(lambda w: w[0].lower() in "aeiou", sentence))
print(f"Input:  {sentence}")
print(f"Output: {vowel_words}")


# ============================================================
#  REDUCE — 5 Examples
# ============================================================
print("\n" + "=" * 50)
print("REDUCE EXAMPLES")
print("=" * 50)

# Reduce Example 1: Sum all numbers in a list
# Source: https://www.w3schools.com/python/ref_func_reduce.asp
print("\n-- Reduce Ex 1: Sum all numbers --")
nums = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, nums)
print(f"Input: {nums}")
print(f"Sum:   {total}")

# Reduce Example 2: Find the maximum value
# Source: https://www.w3schools.com/python/ref_func_reduce.asp
print("\n-- Reduce Ex 2: Find maximum value --")
values = [3, 7, 2, 9, 1, 5]
maximum = reduce(lambda a, b: a if a > b else b, values)
print(f"Input:   {values}")
print(f"Maximum: {maximum}")

# Reduce Example 3: Multiply all numbers (factorial-style)
# Source: https://www.w3schools.com/python/ref_func_reduce.asp
print("\n-- Reduce Ex 3: Product of all numbers --")
factors = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, factors)
print(f"Input:   {factors}")
print(f"Product: {product}")

# Reduce Example 4: Flatten a list of strings into one sentence
# Source: https://www.w3schools.com/python/ref_func_reduce.asp
print("\n-- Reduce Ex 4: Concatenate strings --")
words = ["Python", "is", "really", "powerful"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(f"Input:  {words}")
print(f"Output: {sentence}")

# Reduce Example 5: Count total characters across all strings
# Source: https://www.w3schools.com/python/ref_func_reduce.asp
print("\n-- Reduce Ex 5: Total character count --")
names = ["Alice", "Bob", "Charlie", "Diana"]
total_chars = reduce(lambda acc, name: acc + len(name), names, 0)
print(f"Input:       {names}")
print(f"Total chars: {total_chars}")
