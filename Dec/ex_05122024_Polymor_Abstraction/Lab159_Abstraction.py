from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def makesound(self):
        pass

class Dog(Animal):
    def makesound(self):
        print(f"{self.name} is barking....")

obj_ref = Dog("sam")
obj_ref.makesound()