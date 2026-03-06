# 1 example

import re
s1 = str(input())

print("Yes" if s1[0:5] == "Hello" else "No")

# 2 example


s1 = str(input())
s2 = str(input())

print("Yes" if s2 in s1 else "No")

# 3 example

s1 = str(input())
s2 = str(input())

count = 0
for i in s1:
    index = 0
    if s1[index:len(s2)] == s2:
        count += 1
    else:
        continue

print(count)


# 4 example

s = input()

d = re.findall(r"\d", s)
print(*d)

# 5 example


s = input()

if re.match(r'^[A-Za-z].*\d$', s):
    print("Yes")
else:
    print("No")

# 6 example

s = input()

match = re.search(r'\S+@\S+\.\S+', s)
if match:
    print(match.group())
else:
    print("No email")

# 7 example

s1 = input()
s2 = input()
s3 = input()

print(s1.replace(s2, s3))

# 8 example

s = input()
pattern = input()

parts = re.split(pattern, s)

print(','.join(parts))

# 9 example

s = input().split(" ")
count = 0
for i in s:
    if len(i) == 3:
        count += 1

print(count)

# 10 example

s = input()

if re.search(r"cat|dog", s):
    print("Yes")
else:
    print("No")

# 11 example

s = input()
count = 0
for i in s:
    if i.isupper():
        count += 1

print(count)

# 12 example

s = input()

d = re.findall(r'\d{2,}', s)
print(*d)

# 13 example

s = input()

d = re.findall(r'\w+', s)
print(len(d))

# 14 example

s = input()

if re.fullmatch(r'\d+', s):
    print("Match")
else:
    print("No match")

# 15 example

s = input()
my_list = []

for i in s:
    if i.isdigit():
        my_list.append(i)
        my_list.append(i)
    else:
        my_list.append(i)

print("".join(my_list))

# 16 example


s = input()

match = re.search(r'Name: (.+), Age: (.+)', s)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)

# 17 example

s = input()
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', s)

print(len(dates))


# 18 example

s = input()
pattern = input()
print(len([i for i in s if i == pattern]))


# 19 example

s = input()

d = re.findall(r'\w+', s)
print(len(d))
