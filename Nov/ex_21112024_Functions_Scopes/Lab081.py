pb_global_b = 10

def my_function():
    pb_a = 20   # local variable, within the function
    print(pb_a)
    print(pb_global_b)


#print(pb_a) // name 'pb_a' is not defined
print(pb_global_b)
my_function()