class MathUtils:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c=1):
        return a + b + c

obj_math = MathUtils()
x = obj_math.add(10,20)
y = obj_math.add(1,2,3)
print(x)
print(y)