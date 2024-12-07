from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        print("PC initialized")

class MotherBoard:
    def start(self):
        print("MotherBoard started")

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):
    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def loadOS():
        print("Operating System loaded")

    def startMouse(self):
        print("Mouse started")

    def useHeadPhone(self):
        print("Headphones connected")