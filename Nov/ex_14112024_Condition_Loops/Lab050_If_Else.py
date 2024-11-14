num1 = int(input("enter number 1\n"))
num2 = int(input("enter number 2\n"))
num3 = int(input("enter number 3\n"))

if num1 > num2 and num1 > num3:
    print("number 1 greater", num1)
elif num2 > num1 and num2 > num3:
    print("number 2 is greater", num2)
else:
    print("number 3 is greater", num3)