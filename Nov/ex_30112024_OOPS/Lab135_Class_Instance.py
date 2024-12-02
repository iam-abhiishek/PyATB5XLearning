from tkinter.font import names


class Person:

    def __init__(self, name):
        self.name = name
        print(name)

    def walk(self):
        return self.name

obj_ref1 = Person("abhishek")
obj_ref2 = Person("rahul")

print("who is walking", obj_ref1.walk())
print("who is walking", obj_ref2.walk())