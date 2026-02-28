import datetime


# 1 edxample
x = datetime.datetime.now()

print("── Current Date & Time ──")
print(x)


# 2 example
print("\n── Date Attributes ──")
print("Year  :", x.year)
print("Month :", x.month)
print("Day   :", x.day)
print("Hour  :", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)


# 3 example
print("\n── Specific Date Object ──")
x = datetime.datetime(2020, 5, 17)
print(x)


# 4 example
print("\n── strftime() Formatting ──")
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))          # Full month name  - June
print(x.strftime("%Y"))          # 4-digit year     - 2018
print(x.strftime("%d"))          # Day of month     - 01
print(x.strftime("%A"))          # Weekday name     - Friday
print(x.strftime("%H:%M:%S"))    # Time             - 00:00:00


# 5 example
print("\n── More Format Codes ──")
now = datetime.datetime.now()

print("Full date     :", now.strftime("%x"))          # 04/15/24 (locale)
print("12-hour clock :", now.strftime("%I:%M %p"))    # 02:30 PM
print("Week number   :", now.strftime("%W"))
