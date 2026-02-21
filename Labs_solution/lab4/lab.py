# 1 example

num = int(input())

for i in range(1, num+1):
    print(i ** 2)


# 2 example

num = int(input())

if num == 1 or num == 0:
    print(0)
else:
    for i in range(0, num+1):
        if i % 2 == 0:
            if (i == num and num % 2 == 0) or (i == num - 1 and num % 2 != 0):
                print(i)
                break
            else:
                print(i, end=",")
        else:
            continue

# 3 example

num = int(input())

for i in range(0, num+1):
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")


# 4 example

a, b = map(int, input())

for i in range(a, b+1):
    print(i ** 2)

# 5 example

num = int(input())

if num == 0:
    print(0)
else:
    for i in range(num, -1, -1):
        print(i)

# 6 example
