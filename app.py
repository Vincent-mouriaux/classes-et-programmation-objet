import characters as chars

def creation_personnage ():
    classe = input("Bienvenu, choisissez votre classe :\n (M)agicien\n (A)rcher\n (G)uerrier\n")
    nom = input("Quel sera votre nom ? ")
    if classe.lower() == "m":
        player = chars.Wizard(nom)
    elif classe.lower() == "a":
        player = chars.Archer(nom)
    else:
        player = chars.Warrior(nom)
    return player

def main():

    player1 = creation_personnage()
    player2 = creation_personnage()

    print("Bienvenus dans l'arène, {} et {} vont maintenant s'affronter dans un combat sans merci !\n".format(player1, player2))
    input("")

    while player1.health > 0 and player2.health > 0:
        equipped_weapon, attack_points = player1.attack()
        print("{} ({}pv) attaque {} ({}pv) avec {} et tente de lui infliger {} points de dégâts !".format(player1, player1.health, player2, player2.health, equipped_weapon, attack_points))

        defense_roll, player2.health = player2.defend(equipped_weapon, attack_points)
        if defense_roll >= attack_points:
            print("{} se défend avec {} également à hauteur de {}, ce qui lui permet de parer l'attaque de {} !\n".format(player2, equipped_weapon, defense_roll, player1))
        else:
            print("{} se défend avec {} également à hauteur de {}, ce qui est insuffisant pour parer, ses PV tombent à {} sous les coups de {} !\n".format(
                player2, equipped_weapon, defense_roll, player2.health, player1))

        input("")

        if player1.health > 0 and player2.health > 0:
            equipped_weapon, attack_points = player2.attack()
            print("{} ({}pv) attaque {} ({}pv) avec {} et tente de lui infliger {} points de dégâts !".format(player2, player2.health, player1, player1.health, equipped_weapon, attack_points))

            defense_roll, player1.health = player1.defend(equipped_weapon, attack_points)
            if defense_roll >= attack_points:
                print("{} se défend avec {} également à hauteur de {}, ce qui lui permet de parer l'attaque de {} !\n".format(player1, equipped_weapon, defense_roll, player2))
            else:
                print("{} se défend avec {} également à hauteur de {}, ce qui est insuffisant pour parer, ses PV tombent à {} sous les coups de {} !\n".format(
                    player1, equipped_weapon, defense_roll, player1.health, player2))

            input("")

    if player1.health <= 0:
        winner = player2
        loser = player1
    else:
        winner = player1
        loser = player2
    print("Félicitations à {} qui a fait mordre la poussière à feu {} dans une démonstration de puissance indubitable ! ".format(winner, loser))

if __name__ == '__main__':
    main()

