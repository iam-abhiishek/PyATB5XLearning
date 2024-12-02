class Sports:

    def __init__(self):
        self.batsman = "VK"
        self.__coach = "gauti"

    def ipl(self):
        print(self.batsman)
        print(self.__coach)


obj_ref = Sports()
obj_ref.ipl()
print(obj_ref.batsman)
