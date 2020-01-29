
mylist = [54, 12 , 87, 2, 69, 8, 124, 46, 88, 42, 33]
minilist = [1, 2, 3]

while True:

    choice = input("(A)jouter\n(I)nsérer\n(N)ombre d'elements\n(Fusionner\n(T)rier\n(D)elete un element\n"
                   "(Y)a t il x?\n(P)op (enlever et vérifier)\n(S)lice\nAUTRE POUR AFFICHER LA LISTE")
    if choice.lower() == "a":
        element = int(input("element à rajouter : "))
        mylist.append(element)
    elif choice.lower() == "i":
        element = int(input("element à insérer : "))
        location = int(input("a quelle place de la liste dois je l'inserer ? "))
        mylist.insert(location, element)
    elif choice.lower() == "n":
        print("la liste comprend {} elements".format(len(mylist)))
    elif choice.lower() == "f":
        print(" je vais fusionner cette minilist {} à mylist {}".format(minilist, mylist))
        print(mylist.extend(minilist))
    elif choice.lower() == "t":
        print("le tri de {} donne : {}.".format(mylist, sorted(mylist)))
    elif choice.lower() == "d":
        element = int(input("element à supprimer ? "))
        mylist.remove(element)
        print("Voila ma liste délestée de {} : {}.".format(element, mylist))
    elif choice.lower() == "y":
        element = int(input("vérifier si la liste comprend ? "))
        if element in mylist:
            print("yep")
        else:
            print("nope")
    elif choice.lower() == "p":
        location = int(input("le combientième élément dois je supprimer ? "))
        print("J'enleve en mylist[{}] l'élément {} pour avoir au final mylist = {}.".format(location, mylist.pop(location), mylist))
    elif choice.lower() == "s":
        location = int(input("de quel element commencer ma tranche ? "))
        location2 = int(input("jusqu'a quel element ? "))
        print(mylist[location: location2+1])
    else:
        print("etat actuel de la liste {}".format(mylist))
