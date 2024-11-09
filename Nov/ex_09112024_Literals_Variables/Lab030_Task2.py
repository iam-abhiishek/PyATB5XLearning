# Task for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("enter number 1\n"))
num2 = int(input("enter number 2\n"))

quotient = int(num1/num2)
#quotient = num1/num2
remainder = num1%num2

print("quotient of num1 and num2 is", quotient)
print(type(quotient))
print("remainder of num1 and num2 is", remainder)
print(type(remainder))