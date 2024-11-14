# ✅  Checking for a Leap Year , 2024 → Yes

# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

year = int(input("enter ur year\n"))

# leapyear = (year % 4)
# leapyear1 = (year % 400)
# print(leapyear1)
# if leapyear == 0 or leapyear1 == 0:
#     print("it is a leap year")
# else:
#     print("its not leap year")

if ((year % 4) == 0) and ((year % 400) == 0) and ((year % 100) == 0):
    print("it is a leap year")
elif ((year % 4) == 0) and ((year % 400) != 0) and ((year % 100) == 0):
    print("it is not a leap year")
elif ((year % 4) == 0) and ((year % 100) != 0):
    print("it is a leap year")
else:
    print("it is not a leap year")