class Fruit:
    def __init__(self, radius):
        self.radius = radius

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        return False


apple = Fruit(5)
grapes = Fruit(0.5)
if apple > grapes:
    print("Apple is bigger than grapes")
else:
    print("Apple is bigger than grapes")


