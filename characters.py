from random import randint

class Character:

    max_health = 12
    magic_dice_max = 8
    bow_dice_max = 8
    sword_dice_max = 8

    def __init__(self, name):
        self.name = name
        self.health = self.max_health

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
        return dices[0]

    def defend(self, weapon, attack_points):
        if weapon == 'magic':
            defense_roll = randint(1, self.magic_dice_max)
        elif weapon == 'bow':
            defense_roll = randint(1, self.bow_dice_max)
        else:
            defense_roll = randint(1, self.sword_dice_max)
        if attack_points >= defense_roll:
            self.health = self.health - (attack_points - defense_roll)
            if self.health < 0:
                self.health = 0
        return defense_roll, self.health

class Wizard(Character):

    magic_dice_max = 12
    bow_dice_max = 10
    sword_dice_max = 8

    def attack(self):
        equipped_weapon, attack_points = super().attack()
        magic_dice = randint(1, self.magic_dice_max)
        if magic_dice > attack_points:
            equipped_weapon = 'magic'
            attack_points = magic_dice
        return equipped_weapon, attack_points

class Archer(Character):

    magic_dice_max = 10
    bow_dice_max = 12
    sword_dice_max = 8

    def attack(self):
        equipped_weapon, attack_points = super().attack()
        if equipped_weapon == 'magic' or equipped_weapon == 'sword':
            attack_points = attack_points + 1
        return equipped_weapon, attack_points

class Warrior(Character):

    max_health = 16
    magic_dice_max = 8
    bow_dice_max = 10
    sword_dice_max = 12

