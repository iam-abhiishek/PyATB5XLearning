from abc import abstractmethod


class Father:

    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("loan paid")

obj_ref = Son()
obj_ref.loan()
