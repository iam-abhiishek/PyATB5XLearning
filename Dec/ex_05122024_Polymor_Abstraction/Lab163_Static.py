class Static:

    @staticmethod
    def sum(a, b):
        return a + b

    def sum(self, a, b):
        return a + b

# print(Static.sum(1, 2))
obj = Static()
x = obj.sum(5,9)
print(x)