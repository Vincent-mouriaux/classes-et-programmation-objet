import characters as chars

nom1 = input("Bienvenu Player 1, quel sera votre nom ? ")
nom2 = input("Bienvenu Player 2, quel sera votre nom ? ")
player1 = chars.Wizard(nom1)
player2 = chars.Wizard(nom2)

print("Bienvenus dans l'arène, {} et {} vont maintenant s'affronter dans un combat sans merci !\n".format(player1, player2))

equipped_weapon, attack_points = player1.attack()
print("{} attaque {} avec {} et tente de lui infliger {} points de dégâts !\n".format(player1, player2, equipped_weapon, attack_points))

defense_roll, healthp2 = player2.defend(equipped_weapon, attack_points)
if defense_roll >= attack_points:
    print("{} se défend avec {} également à hauteur de {}, ce qui lui permet de parer l'attaque de {} !".format(player2, equipped_weapon, defense_roll, player1))
else:
    print("{} se défend avec {} également à hauteur de {}, ce qui est insuffisant pour parer, ses PV tombent à {} sous les coups de {} !".format(player2,
                                                                                                                equipped_weapon,
                                                                                                                defense_roll, healthp2,
                                                                                                                player1))
