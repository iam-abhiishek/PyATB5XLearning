from abc import abstractmethod


class GearBox:

    @abstractmethod
    def set_gear(self):
        pass

class Engine:
    @abstractmethod
    def start(self):
        print("starting")

    def set_gear(self):
        print("gearbox is ready")

    def stop(self):
        print("stopping")

class Car(Engine):

    def drive(self):
        self.start()
        self.set_gear()
        self.stop()


obj_ref = Car()
obj_ref.drive()

