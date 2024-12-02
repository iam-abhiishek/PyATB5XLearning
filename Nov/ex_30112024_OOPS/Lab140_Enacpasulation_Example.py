class Car:

    def __init__(self):
        self.password = "123"  # public instance variable
        self.__password_secure = "pass123"   # private instance variable

    def change_password(self):
        print(self.__password_secure)
        print(self.password)

obj_ref = Car()
# print(obj_ref.__password_secure)  #AttributeError: 'Car' object has no attribute '__password_secure'. Did you mean: '_Car__password_secure'?
obj_ref.change_password()