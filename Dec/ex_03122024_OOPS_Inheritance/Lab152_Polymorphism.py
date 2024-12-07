class Dog:

    def bark(self):
        print("dog is barking")

    def bark(self, breed):
        print(f"dog {breed} is barking ")

obj = Dog()
obj.bark("sam")