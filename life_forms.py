import random

"""I think this will be a collection classes for all lifeforms"""

class Lifeform:

    def __init__(self):
        self.energy = -1
        self.letter = "L"

    def __str__(self):

        if self.energy <= 999:
            energy_string = str(self.energy)
        else:
            energy_string = '999'

        return self.letter + "0"*(3-len(energy_string)) + energy_string


class Plant(Lifeform):

    def __init__(self, location):

        self.letter = "P"
        self.energy = random.randrange(3, 15)
        self.location = location

        self.growth_cost = 2 #joule/mm
        self.growth_rate = random.randrange(1,3) #mm per day
        self.height = random.randrange(1,6) #mm

    def be_grazed(self, graze_amount):

        if graze_amount >= self.energy:
            self.energy = 0
            return self.energy
        else:
            self.energy = self.energy - graze_amount
            return graze_amount

    def live_a_day(self, energy_from_sun):

        self.energy += energy_from_sun
        self.height = self.height + self.growth_rate
        self.energy -= self.growth_rate * self.growth_cost


    def report(self):

        print(f"This is a Plant that has {self.energy} energy. It is located at: {self.location}")

class Empty(Lifeform):

    def __init__(self):
        self.letter = "E"
        self.energy = int(0)



if __name__ == "__main__":

    p = Plant((1,1))
    print("first")
    p.report()
    print("second")
    p.be_grazed(3)
    p.report()

    print(p)