""""
Classe chargée de gérer une partie de tic tac toe
"""
from Joueur import *


class Morpion:
    def __init__(self, affichage):
        """Fonction qui initialise la classe"""
        self.plateau = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.liste_IA = [Joueur(self, '0', 'IA'), # IA qui joue en premier
                         Joueur(self, '1', 'IA'),  # IA qui joue en deuxième
                         
        print(" Formation de l'IA (prend plusieurs dizaines de secondes)")
                        ]
        print("###################### IA 1 : formation contre aléatoire pour jouer en deuxieme  ##############################")
        for i in range(10):
            self.liste_IA[1].IA.former_IA(iteration=1000,
                                          adversaire=Joueur(self, 'A', 'hasard'),
                                          commencer=False,
                                          graphique=True and affichage
                                          )
            self.liste_IA[1].IA.purifier_mémoire_IA()

        print("###################### IA 0 : formation contre l'IA 1 pour jouer en premier ##############################")
        for i in range(10):
            self.liste_IA[0].IA.former_IA(iteration=1000,
                                          adversaire=self.liste_IA[1],
                                          commencer=True,
                                          graphique=True and affichage
                                          )

            self.liste_IA[0].IA.former_IA(iteration=9000,
                                          adversaire=self.liste_IA[1],
                                          commencer=True,
                                          graphique=False
                                          )
            self.liste_IA[0].IA.purifier_mémoire_IA()

        print("###################### IA 0 : fin de la formation de l'IA contre l'aléatoire ##############################")
        for i in range(10):
            self.liste_IA[0].IA.former_IA(iteration=5000,
                                          adversaire=Joueur(self, 'A', 'hasard'),
                                          commencer=True,
                                          graphique=True and affichage
                                      )

    def initialiser_plateau(self):
        """Fonction chargée de remettre le plateau à zéro"""
        self.plateau = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def afficher_le_plateau(self):
        """Fonction chargée d'afficher le plateau de jeu sous la forme :
            -------
            |0|1|2|
            |3|4|5|
            |6|7|8|
            -------
        """
        txt = "-" * 7 + '\n'
        for i in range(3):
            for j in range(3):
                txt += '|'
                txt += self.plateau[i][j]
            txt += '|\n'
        txt += "-" * 7
        print(txt)

    def jouer_une_partie(self, joueur1, joueur2):
        """Fonction chargée de lancer une nouvelle partie"""
        self.initialiser_plateau()
        while True:
            # Tour du J1
            if not joueur1.jouer():  # si l'on ne peut pas jouer
                return f"victoire joueur {joueur2.symbole}"
            tester_fin = self.tester_fin_de_partie()
            if tester_fin == 'victoire':
                return f"victoire joueur {joueur1.symbole}"
            if tester_fin == 'égalité':
                return 'égalité'
            # Tour du J2
            if not joueur2.jouer():  # si l'on ne peut pas jouer
                return f"victoire joueur {joueur1.symbole}"
            tester_fin = self.tester_fin_de_partie()
            if tester_fin == 'victoire':
                return f"victoire joueur {joueur2.symbole}"
            if tester_fin == 'égalité':
                return 'égalité'

    def tester_fin_de_partie(self):
        """Fonction chargée de tester si la partie est terminée"""
        ########## On teste les victoires ##########
        # On teste les lignes
        for i in range(3):
            if self.plateau[i][0] == self.plateau[i][1] == self.plateau[i][2] != '-':
                return 'victoire'
        # on teste les colonnes
        for j in range(3):
            if self.plateau[0][j] == self.plateau[1][j] == self.plateau[2][j] != '-':
                return 'victoire'
        # On teste la diagonale haut-gauche - bas-droit
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] != '-':
            return 'victoire'
        # On teste la diagonale haut-droit - bas-gauche
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] != '-':
            return 'victoire'
        ########## On teste les égalités ##########
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j] == '-':
                    return 'continue'
        return 'égalité'
