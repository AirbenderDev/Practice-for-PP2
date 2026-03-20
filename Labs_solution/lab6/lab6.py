# 1 example
n = int(input())
lst = list((map(int, input().split())))
summ = 0

for i in lst:
    summ += i * i
print(summ)

# 2 example

n = int(input())
lst = list(map(int, input().split()))

some = list(filter(lambda x: x % 2 == 0, lst))
print(len(some))

# 3 example

n = int(input())
lst = input().split()

for i, h in enumerate(lst):
    print(f"{i}:{h}", end=" ")

# 4 example

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0

for i in range(n):
    count += a[i] * b[i]
print(count)

# 5 example

s = input()
some = "aeiouAEIOU"

if any(c in some for c in s):
    print("Yes")
else:
    print("No")

# 6 example
n = int(input())
my_list = list(map(int, input().split()))

if all(i >= 0 for i in my_list):
    print("Yes")
else:
    print("No")

# 7 example

n = int(input())
my_list = input().split()

mx = max(my_list, key=len)
print(mx)

# 8 example

n = int(input())
my_list = list(map(int, input().split()))

sorte = sorted(set(my_list))
print(*sorte)

# 9 example

n = int(input())
k = input().split()
v = input().split()

d = dict(zip(k, v))
q = input()

print(d.get(q, "Not found"))

# 10 example

n = int(input())
l = list(map(int, input().split()))

count = sum(map(bool, l))
print(count)
