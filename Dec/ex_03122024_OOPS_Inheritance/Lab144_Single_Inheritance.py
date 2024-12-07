class Father:
    key = "2BHK"

    def car(self):
        print("father has a car -> Alto")
        print(self.key)

class Son(Father):  #single inheritance
    key2 = "3BHK"

    def suv(self):
        print("son has a car -> MG Hector")
        print(self.key2)

father_obj = Father()
# (father_obj.car())

son_obj = Son()
son_obj.suv()
son_obj.car()
print(son_obj.key)
