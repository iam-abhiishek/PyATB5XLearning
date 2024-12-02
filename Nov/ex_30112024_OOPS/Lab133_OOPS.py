a = 20   #global variable

class Person:

    b = 10  # instance variable - belong to class

    def print_info(self):
        c = 30   # Local variable
        # a = "Hello"
        # print(self.c)  # AttributeError: 'Person' object has no attribute 'c'
        print(c)
        print(self.b)
        # print(self.a)    # AttributeError: 'Person' object has no attribute 'a'
        # print(a) # Local variable has more preference over global variable
        global a
        print(a)


obj_ref = Person()
obj_ref.print_info()
