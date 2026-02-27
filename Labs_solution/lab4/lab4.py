
import importlib
import calendar
from datetime import datetime, timedelta, timezone, date
import math
import sys
from datetime import datetime, timedelta, timezone
import re
import json

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


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input())

if n > 0:
    print(",".join(str(x) for x in fibonacci(n)))

# 7 example


class Reverse:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        b = ''
        for i in range(len(self.string) - 1, -1, -1):
            b += self.string[i]
        return b


smth = input()
smth_word = Reverse(smth)
final = smth_word.reverse()
print(final)

# 8 example

num = int(input())


def primes(n):
    for i in range(2, n+1):
        isTrue = True
        for j in range(2, int(pow(i, 0.5))+1):
            if i % j == 0:
                isTrue = False
                break
        if isTrue:
            yield i


for i in primes(num):
    print(i, end=" ")

# 9 example

num = int(input())


def pows(n):
    for i in range(0, n+1):
        yield pow(n, i)


for i in pows(num):
    print(i, end=" ")

# 10 example


def powers(s: str, n: int):
    for _ in range(1, n+1):
        yield s


my_str = str(input())
my_int = int(input())

for i in powers(my_str, my_int):
    print(i, end=" ")


# 11 example


def apply_patch(source, patch):
    for key, pval in patch.items():
        if pval is None:
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(pval, dict):
            apply_patch(source[key], pval)
        else:
            source[key] = pval
    return source


source = json.loads(input())
patch = json.loads(input())

result = apply_patch(source, patch)
print(json.dumps(result, separators=(',', ':'), sort_keys=True))


# 12 example

def deep_diff(a, b, path="", diffs=None):
    if diffs is None:
        diffs = []

    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else k
            if k not in a:
                diffs.append((new_path, "<missing>", json.dumps(
                    b[k], separators=(',', ':'))))
            elif k not in b:
                diffs.append((new_path, json.dumps(
                    a[k], separators=(',', ':')), "<missing>"))
            else:
                deep_diff(a[k], b[k], new_path, diffs)
    else:
        if a != b:
            diffs.append((
                path,
                json.dumps(a, separators=(',', ':')),
                json.dumps(b, separators=(',', ':'))
            ))

    return diffs


obj1 = json.loads(input())
obj2 = json.loads(input())

diffs = deep_diff(obj1, obj2)

if not diffs:
    print("No differences")
else:
    for path, old, new in sorted(diffs):
        print(f"{path} : {old} -> {new}")

# 13 example


def resolve_query(data, query):
    parts = re.findall(r'\w+|\[\d+\]', query)
    current = data
    for part in parts:
        if part.startswith('[') and part.endswith(']'):
            if not isinstance(current, list):
                return "NOT_FOUND"
            idx = int(part[1:-1])
            if idx < 0 or idx >= len(current):
                return "NOT_FOUND"
            current = current[idx]
        else:
            if not isinstance(current, dict) or part not in current:
                return "NOT_FOUND"
            current = current[part]
    return json.dumps(current, separators=(',', ':')) if isinstance(current, (dict, list, str, bool, int, float)) or current is None else str(current)


data = json.loads(input())
q = int(input())
queries = [input().strip() for _ in range(q)]

for query in queries:
    print(resolve_query(data, query))

# 14 example


def parse_datetime(s):
    date_part, tz_part = s.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if tz_part[3] == '+' else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    dt = dt.replace(tzinfo=offset)
    return dt


dt1 = parse_datetime(sys.stdin.readline().strip())
dt2 = parse_datetime(sys.stdin.readline().strip())

delta = abs((dt1 - dt2).total_seconds())
days = int(delta // 86400)

print(days)

# 15 example


def parse_dt(s):
    s = s.strip()
    tz_part = s[11:]
    sign = 1 if '+' in tz_part else -1
    tz_str = tz_part.replace('UTC+', '').replace('UTC-', '')
    h, m = map(int, tz_str.split(':'))
    offset = timedelta(hours=h, minutes=m) * sign
    tz = timezone(offset)
    dt = datetime(int(s[0:4]), int(s[5:7]), int(s[8:10]), 0, 0, 0, tzinfo=tz)
    return dt


def make_birthday(year, month, day, tz):
    if month == 2 and day == 29 and not calendar.isleap(year):
        day = 28
    return datetime(year, month, day, 0, 0, 0, tzinfo=tz)


birth_dt = parse_dt(input())
curr_dt = parse_dt(input())

bday_month, bday_day = birth_dt.month, birth_dt.day
birth_tz = birth_dt.tzinfo

for year_offset in [0, 1]:
    year = curr_dt.year + year_offset
    candidate = make_birthday(year, bday_month, bday_day, birth_tz)
    if candidate >= curr_dt:
        diff_sec = (candidate - curr_dt).total_seconds()
        print(math.ceil(diff_sec / 86400))
        break

# 16 example


def parse_dt(s):
    s = s.strip()
    date_time = s[:19]
    tz_part = s[20:]
    sign = 1 if '+' in tz_part else -1
    tz_str = tz_part.replace('UTC+', '').replace('UTC-', '')
    h, m = map(int, tz_str.split(':'))
    offset = timedelta(hours=h, minutes=m) * sign
    tz = timezone(offset)
    dt = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz)
    return dt


start = parse_dt(input())
end = parse_dt(input())
print(int((end - start).total_seconds()))

# 17 example


r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - r*r

if a == 0:
    if c <= 0:
        print("0.0000000000")
    else:
        print("0.0000000000")
else:
    disc = b*b - 4*a*c
    if disc < 0:
        print("{:.10f}".format(0.0))
    else:
        sq = math.sqrt(max(0, disc))
        t1 = (-b - sq) / (2*a)
        t2 = (-b + sq) / (2*a)
        t1 = max(t1, 0.0)
        t2 = min(t2, 1.0)
        if t2 < t1:
            print("{:.10f}".format(0.0))
        else:
            length = (t2 - t1) * math.sqrt(a)
            print("{:.10f}".format(length))

# 18 example

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

t = y1 / (y1 + y2)
x = x1 + t*(x2 - x1)
print("{:.10f} {:.10f}".format(x, 0.0))

# 19 example


r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
a = dx*dx + dy*dy

if a == 0:
    print("{:.10f}".format(0.0))
else:
    t = -(x1*dx + y1*dy) / a
    t = max(0.0, min(1.0, t))
    px = x1 + t*dx
    py = y1 + t*dy
    dist_sq = px*px + py*py

    if dist_sq >= r*r - 1e-9:
        print("{:.10f}".format(math.sqrt(a)))
    else:
        d1 = math.sqrt(x1*x1 + y1*y1)
        d2 = math.sqrt(x2*x2 + y2*y2)
        tang1 = math.sqrt(max(0, d1*d1 - r*r))
        tang2 = math.sqrt(max(0, d2*d2 - r*r))
        a1 = math.atan2(y1, x1)
        a2 = math.atan2(y2, x2)
        alpha1 = math.acos(max(-1, min(1, r/d1)))
        alpha2 = math.acos(max(-1, min(1, r/d2)))

        best = float('inf')
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                tp1 = a1 + s1*alpha1
                tp2 = a2 + s2*alpha2
                arc_angle = abs(tp1 - tp2) % (2*math.pi)
                if arc_angle > math.pi:
                    arc_angle = 2*math.pi - arc_angle
                best = min(best, tang1 + r*arc_angle + tang2)

        print("{:.10f}".format(best))

# 20 example

n = int(input())
g = 0
outer_n = 0
for _ in range(n):
    parts = input().split()
    scope, val = parts[0], int(parts[1])
    if scope == 'global':
        g += val
    elif scope == 'nonlocal':
        outer_n += val
print(g, outer_n)

# 21 example


n = int(input())
for _ in range(n):
    parts = input().split()
    mod_path, attr = parts[0], parts[1]
    try:
        mod = importlib.import_module(mod_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
        continue
    val = getattr(mod, attr)
    if callable(val):
        print("CALLABLE")
    else:
        print("VALUE")
