class Overloading:

    def sum(self, *args):
        for i in args:
            print(i)


obj = Overloading()
obj.sum(1)
print("------")
obj.sum(1, 2, 3)