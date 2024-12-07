class Father:
    def home(self):
        print("father's home")

    def father_money(self):
        return 5

class Mother:
    def home(self):
        print("mother's home")

    def mother_money(self):
        return 10

# class Son(Father, Mother):
class Son(Mother, Father):  # Multiple In - FCFS
    def print_info(self):
        print("son")

son_ref = Son()
print(son_ref.father_money())
print(son_ref.mother_money())
son_ref.home()

