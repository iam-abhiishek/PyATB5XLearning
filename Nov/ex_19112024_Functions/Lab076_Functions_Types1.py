# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
from Nov.ex_07112024_keywords_idebtifier_variables.Lab014_Math_Functions import result


# 1. The can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print('hi')

greet()

# 2. # No Return Type and with Argument/ Param

def greet_by_name(name):
    print('hi', name)

greet_by_name('abhishek')

# 3. No Return Type and with Default Argument ( # positional argument)

def say_hello_default_arg(name = 'Abhishek'):
    print('hi', name.upper())

say_hello_default_arg()
say_hello_default_arg('Kumar')

def multiple_arg(name1 = 'A', name2 = 'B'):
    print('hi', name1, name2)

multiple_arg()
multiple_arg('school')
multiple_arg('dance', 'sing')
multiple_arg(name2='cool')

# 4. Argument + return Type

def sum_of_two(a, b):
    return a + b

result = sum_of_two(10, 20)
print(result)

def sum_of_two_number_with_default(a= 100, b= 200):
    return a + b

result = sum_of_two_number_with_default()
print(result)
result = sum_of_two_number_with_default(13, 12)
print(result)