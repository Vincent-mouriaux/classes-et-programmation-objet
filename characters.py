from random import randint

class Wizard:

    max_health = 20
    health = max_health
    magic_dice_max = 12
    bow_dice_max = 10
    sword_dice_max = 8

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{} the {}".format(self.name, self.__class__.__name__.lower())

    def attack(self):
        magic_dice = randint(1, self.magic_dice_max)
        sword_dice = randint(1, self.sword_dice_max)
        bow_dice = randint(1, self.bow_dice_max)

        dices = sorted([
            ['magic', magic_dice],
            ['sword', sword_dice],
            ['bow', bow_dice]
        ], key=lambda x: x[1], reverse=True)
        equipped_weapon = dices[0][0]
        attack_points = dices[0][1]
        return equipped_weapon, attack_points

    def defend(self, weapon, attack_points):
        if weapon == 'magic':
            defense_roll = randint(1, self.magic_dice_max)
        elif weapon == 'bow':
            defense_roll = randint(1, self.bow_dice_max)
        else:
            defense_roll = randint(1, self.sword_dice_max)
        if attack_points >= defense_roll:
            self.health = self.health - (attack_points - defense_roll)
        return defense_roll, self.health

"""
hero = Wizard("Merlin")
print(hero)
"""