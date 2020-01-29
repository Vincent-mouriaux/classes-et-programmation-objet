def set_age(self, value):
    if value < 1 or value >= self.life_esperance:
        raise Exception("Erreur, age incorrect : GFY DUMMY !")
    else:
        self._age = value