from abc import ABC, abstractmethod


class PC:

    def __init__(self, name):
        self.name = name

class MotherBoard(ABC):

    @abstractmethod
    def start_motherboard(self):
        pass

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    def start_processor(self):
        pass

class Storage(Processor):
    def start_motherboard(self):
        print("motherboard is starting")

    def start_ram(self):
        print("ram is starting")

    def start_processor(self):
        print("processor is starting")

    def storage_data(self):
        self.start_motherboard()
        self.start_ram()
        self.start_processor()

    @staticmethod
    def loadOS():
        print("is loading")
        print("storage is 1024gb and RAM is 32gb")

    def startMouse(self):
        print("mouse is ready")

    def useHeadphone(self):
        print("headphone connected")

obj_ref = Storage()
obj_ref.storage_data()
print(Storage.loadOS())





