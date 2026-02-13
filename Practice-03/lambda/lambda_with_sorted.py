# 1 example
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# 2 example
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# 3 example
numbers = [-5, 2, -8, 3, -1, 7]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(sorted_by_abs)


# 4 example
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_grade)


# 5 example
words = ["Python", "java", "C++", "ruby"]
sorted_case_insensitive = sorted(words, key=lambda x: x.lower())
print(sorted_case_insensitive)
