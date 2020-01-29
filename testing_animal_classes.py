import animals_classes as zoo

felix = zoo.Cat("Felix", 8, "greyish", 2)
toto = zoo.Snail("Toto l'escargot", 200, "ugly", 2)
solid = zoo.Snake("Solid", 25, 'even worse than the greyish snail, to say the least..', 2)
input("TAPER ENTREE POUR COMMENCER")

print(felix)
felix.talk()
diet = felix.get_diet()
if not diet:
    print("Le bilan carbone de {} est exemplaire, iel ne mange rien".format(felix.name))
else:
    print("{} mange :".format(felix.name))
    for food in diet:
        print("{}".format(food))
felix.eat('milk')
felix.eat('banana')
input("")

print(toto)
toto.talk()
toto.get_diet()
toto.eat('salad')
toto.eat('banana')
input("")

print(solid)
solid.talk()
solid.get_diet()
solid.eat('egg')
solid.eat('banana')