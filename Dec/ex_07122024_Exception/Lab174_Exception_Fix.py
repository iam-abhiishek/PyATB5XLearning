try:
    num1 = int(input("enter a number1\n"))
    num2 = int(input("enter a number2\n"))

    result = num1 / num2
    print(result)

except Exception as e:
    print(e)