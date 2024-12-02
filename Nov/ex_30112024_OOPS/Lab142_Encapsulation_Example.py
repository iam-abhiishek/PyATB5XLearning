class Home:

    def __init__(self):
        self.public_var = "Father"
        self.__private_var = "Child"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("wife")

obj_ref = Home()
obj_ref.mom()
print(obj_ref.public_var)
# print(obj_ref.__private_var)  # no accessible as it is private