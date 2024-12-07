class Father:

    def BHK1(self):
        print("1BHK")

class A1(Father):
    def BHK2(self):
        print("2BHK")

class A2(Father):
    def BHK3(self):
        print("3BHK")

class A3(Father):
    def no_house(self):
        print("empty")

# father_obj = Father()
# father_obj.BHK1()

a1_obj = A1()
a1_obj.BHK1()
a1_obj.BHK2()

a2_obj = A2()
a2_obj.BHK1()
a2_obj.BHK3()

a3_obj = A3()
a3_obj.BHK1()
a3_obj.no_house()