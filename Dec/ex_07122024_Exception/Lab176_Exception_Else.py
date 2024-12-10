try:
    num1 = int(input("enter a number1\n"))
    num2 = int(input("enter a number2\n"))
    result = num1 / num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("output is", result)
finally:
    print("very good")