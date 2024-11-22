def outer_function():
    var1 = 10  # for outer it is a local variable and for inner it is a global variable

    def inner_function1():
        var2 = 20
        print(var1)
        print(var2)

    def inner_function2():
        print(var1)


    inner_function1()
    inner_function2()
    # print(var2) not allowed

outer_function()