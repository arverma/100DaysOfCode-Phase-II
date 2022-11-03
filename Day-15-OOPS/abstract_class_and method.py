from abc import ABC, abstractmethod


class Activity(ABC):
    @abstractmethod
    def run(self):
        pass


class Animal(Activity):
    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print("Runs short distance: Speed-{} KM/Hr".format(self.speed))


class Human(Activity):
    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print("Runs long distance: Speed-{} KM/Hr".format(self.speed))


cat = Animal(80)
cat.run()
# Runs short distance: Speed-80 KM/Hr
youth = Human(20)
youth.run()
# Runs long distance: Speed-20 KM/Hr
