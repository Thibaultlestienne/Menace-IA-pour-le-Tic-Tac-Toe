"""
L'objectif de ce programme est de créer une IA pour jouer au morpion basée sur le système MENACE (cf. sources)

SOURCES :
    https://images.math.cnrs.fr/Une-machine-en-boites-d-allumettes-qui-apprend-a-jouer-au-Morpion.html
    https://en.wikipedia.org/wiki/Matchbox_Educable_Noughts_and_Crosses_Engine
"""
from Morpion import *

print("0 pour l'affichage minimal de la formation 1 pour l'affichage complet : ", end = '')

affichage = input()

if int(affichage) == 0:
    partie = Morpion(False)
else :
    partie = Morpion(False)

print ("la grille est de la forme")
print("-------")
print("|0|1|2|")
print("|3|4|5|")
print("|6|7|8|")
print("-------")

print(partie.jouer_une_partie(partie.liste_IA[0], Joueur(partie, 'H', 'humain')))
partie.afficher_le_plateau()



