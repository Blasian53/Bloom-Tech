import random


class Product:
    def __init__(self, name, price=10, weight=20,
                 flammability=.5, identifier=0):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
        
    def stealability(self):
        x = self.price / self.weight

        if x < .5:
            return "Not so stealable..."
        elif (x >= .5) and (x < 1.0):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        x = self.flammability * self.weight

        if x < 10:
            return "...fizzle."
        elif (x >= 10) and (x < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=.5):
        super().__init__(name, price)
        self.weight = weight
        self.flammability = flammability

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif (self.weight >= 5) and (self.weight < 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
