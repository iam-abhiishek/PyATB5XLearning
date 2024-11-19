# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300


num1 = int(input('enter ur number 1\n'))
num2 = int(input('enter ur number 2\n'))
num3 = int(input('enter ur number 3\n'))

def sum_of_three_number(n1 = 100, n2 = 200, n3 = 300):
    return n1 + n2 + n3

result = sum_of_three_number(num1, num2, num3)
print(result)

result1 = sum_of_three_number()
result2 = sum_of_three_number(10,20)
result3 = sum_of_three_number(10)

print(result1)
print(result2)
print(result3)