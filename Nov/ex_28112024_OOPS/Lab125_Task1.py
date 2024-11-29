class PyATB:
    name = None
    age = None
    gender = None
    height = None
    weight = None

    def __init__(self, name, age, gender, height, weight):
        # print("PC: student info is")
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


    def student_info1(self):
        print("student1 is " + self.name)

    def student_info(self):
        print("student name is " + self.name)
        print("student age is " + str(self.age))
        print("student gender is " + self.gender)
        print("student height is " + str(self.height))
        print("student weight is " + str(self.weight))

    def student_info3(self):
        print("student3")

student1obj_ref = PyATB("abhishek",34, "M", 5.5, 60)
student2obj_ref = PyATB("ankit",35, "M", 5.8, 55)
student3obj_ref = PyATB("rahul",37, "M", 6, 65)
print("student 1 info is\n")
student1obj_ref.student_info()
print("student 2 info is\n")
student2obj_ref.student_info()
print("student 3 info is\n")
student3obj_ref.student_info()
print("-------")
student1obj_ref.student_info1()


