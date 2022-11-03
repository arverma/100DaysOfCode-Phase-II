class Man:
    def __init__(self):
        self.speed = 20

    def run(self):
        print("RUNNING>>>{} KM/Hr".format(self.speed))


class Dog:
    def __init__(self):
        self.speed = 25

    def run(self):
        print("RUNNING>>>{} KM/Hr".format(self.speed))


class MobilityTest:
    def __init__(self):
        self.iteration = 3

    def do_mobility_test(self, obj):
        for i in range(self.iteration):
            obj.run()


test1 = MobilityTest()
test1.do_mobility_test(Man())
# RUNNING>>>20 KM/Hr
# RUNNING>>>20 KM/Hr
# RUNNING>>>20 KM/Hr
test1.do_mobility_test(Dog())
# RUNNING>>>25 KM/Hr
# RUNNING>>>25 KM/Hr
# RUNNING>>>25 KM/Hr