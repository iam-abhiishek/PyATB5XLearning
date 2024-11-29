from Nov.ex_26112024_Dict.Lab115_Dict_Multiple2 import student_infor1


class PyATB:
    name = None
    age = None
    gender = None
    height = None
    weight = None

    def __init__(self, name, age, gender, height, weight):
        print("PC: student info is")
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


    def student_info1(self):
        print("student1 is " + self.name)

    def student_info2(self):
        print("student2")

    def student_info3(self):
        print("student3")

obj1_ref = PyATB("abhishek",34, "M", 5.5, 60)
print(obj1_ref.name)
print(obj1_ref.age)
print(obj1_ref.gender)
print(obj1_ref.height)
print(obj1_ref.weight)

obj1_ref.student_info1()


