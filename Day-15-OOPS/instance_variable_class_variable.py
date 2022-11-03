class Animal:
    # Class Variable
    leg = 4

    def __init__(self, name, color, sound):
        # Instance Variable
        self.color = color
        self.name = name
        self.sound = sound

    def speak(self):
        print("{} of {} color with {} leg is SPEAKING: {}".format(self.name, self.color, self.leg, self.sound))


cow = Animal("Cow", "White", "MOOWW")
cat = Animal("Cat", "Black", "Mewww")
dog = Animal("Dog", "Brown", "Bhoww")

cow.speak()
cat.speak()
dog.speak()
# Cow of White color with 4 leg is SPEAKING: MOOWW
# Cat of Black color with 4 leg is SPEAKING: Mewww
# Dog of Brown color with 4 leg is SPEAKING: Bhoww

Animal.leg = 5
cow.speak()
cat.speak()
dog.speak()
# Cow of White color with 5 leg is SPEAKING: MOOWW
# Cat of Black color with 5 leg is SPEAKING: Mewww
# Dog of Brown color with 5 leg is SPEAKING: Bhoww

# Once you assign a value to a class variable it becomes the instance variable
cow.leg = 2
cow.speak()
cat.speak()
dog.speak()
# Cow of White color with 2 leg is SPEAKING: MOOWW
# Cat of Black color with 5 leg is SPEAKING: Mewww
# Dog of Brown color with 5 leg is SPEAKING: Bhoww

Animal.leg = 3
cow.speak()
cat.speak()
dog.speak()
# Cow of White color with 2 leg is SPEAKING: MOOWW
# Cat of Black color with 3 leg is SPEAKING: Mewww
# Dog of Brown color with 3 leg is SPEAKING: Bhoww


