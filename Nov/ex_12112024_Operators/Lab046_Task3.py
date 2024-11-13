#Task 3
#Problem to find the max between two ( 3,4) → 4

x = 3
y = 4
print("x is greater" if x > y else "y is greater",y)

num1 = int(input("pls enter num1\n"))
num2 = int(input("pls enter num2\n"))

if(num1 > num2):
    print(f"num1 is greater:{num1}")
else:
    print(f"num2 is greater:{num2}")

print("-------")

print(f"num1 is greater:{num1}" if num1 > num2 else f"num2 is greater:{num2}")


