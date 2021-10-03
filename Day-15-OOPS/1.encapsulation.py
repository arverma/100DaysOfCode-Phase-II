class Computer:

    def __init__(self):
        self.__max_price = 900
        self._min_price = 0

    def sell(self):
        print("Max Price: {}, Min Price: {}".format(self.__max_price, self._min_price))

    def set_price(self, price):
        self.__max_price = price


c = Computer()
c.sell()

# change the price
c._Computer__max_price = 1000  # Method 1
c.sell()
c.set_price(800)  # Method 2
c.sell()
c._min_price = 200  # Method 3
c.sell()

# Method that doesn't work
c.__max_price = 1000
c.sell()

print(dir(c))
