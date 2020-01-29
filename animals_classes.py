from random import randint

class Animal:

    hair_type = None
    life_esperance = None
    sound = None
    diet = []

    def __init__(self, name, weight, color, age):
        self.age = age
        self.name = name
        self.weight = weight
        self.color = color

    def __repr__(self):
        return "I am {} the {} (age : {}, color : {}) ".format(self.name, self.__class__.__name__.lower(), self.age, self.color)

    def talk(self):
        if not self.sound:
            print("{} n'émet pas de son.".format(self.name))
        else:
            print("{} émet le son suivant : {}".format(self.name, self.sound))

    def get_diet(self):
        return self.diet

    def eat(self, food):
        if not food in self.diet:
            print("{} ne fait pas partie de l'alimentation de {}, iel ne le mange donc pas.".format(food, self.name))
            return False
        else:
            print("{} a mangé {} car c'est dans son alimentation et a fatté salement car iel ne connaît pas la modération "
                  "et que sa race va s'éteindre mais iel n'en a cure..\nSon poids est donc passé de {} "
                  "à {} !..".format(self.name, food, self.weight, self.weight * 1.05))
            self.weight = self.weight * 1.05
            return True

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 1 or value >= self.life_esperance:
            raise Exception("Erreur, age incorrect : GFY DUMMY !")
        else:
            self._age = value

    age = property(get_age, set_age)



class Cat(Animal):

    hair_type = 'Furry'
    life_esperance = 15
    sound = 'Myaaaarrrr'
    diet = ['mouse', 'cat food', 'milk', 'fish', 'meat']

class Snail(Animal):

    hair_type = 'Shell'
    life_esperance = 7
    sound = 'No sound'
#    diet = ['salad', 'live plant', 'fungi', 'mushroom', 'algae']

class Snake(Animal):

    hair_type = 'Snakeskin'
    life_esperance = 30
    sound = 'Hiss'
    diet = ['rodent', 'rabbit', 'bird', 'amphibian', 'egg']