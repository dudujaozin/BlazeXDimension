class Soldier:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def attack(self):
        return f'{self.name} is attacking!'

class GiantAlien:
    def __init__(self, species):
        self.species = species

    def invade(self):
        return f'The {self.species} alien is invading!'

class BendyDemon:
    def __init__(self, power):
        self.power = power

    def scare(self):
        return f'The Bendy demon with power {self.power} is scaring people!'
