""""
Classe chargée de gérer les joueurs du tic tac toe
"""
from IA import *


class Joueur:

    def __init__(self, jeu, symbole, type_de_joueur='humain'):
        """Fonction qui initialise la classe"""
        self.jeu = jeu
        self.symbole = symbole
        self.type_de_joueur = type_de_joueur
        if self.type_de_joueur == 'IA':
            self.IA = IA(self)

    def jouer(self):
        """Fonction chargée de rediriger le mode de jeu en fonction du type de joueur"""
        if self.type_de_joueur == 'humain':
            return self.jouer_humain()
        if self.type_de_joueur == 'IA':
            return self.jouer_IA()
        if self.type_de_joueur == 'hasard':
            return self.jouer_hasard()

    # noinspection PyBroadException
    def jouer_humain(self):
        """Fonction qui permet à un joueur humain de jouer"""
        self.jeu.afficher_le_plateau()
        # On demande à l'utilisateur où il veut jouer et on répète l'opération jusqu'à ce que tt soit OK
        run = True
        while run:
            pos = input(f"Joueur {self.symbole} ou voulez vous jouer (entre 0 et 8) ? ")
            try:
                pos = int(pos)
                if self.jeu.plateau[pos // 3][pos % 3] == '-':
                    self.jeu.plateau[pos // 3][pos % 3] = self.symbole
                    run = False
            except:
                pass
        return True

    def jouer_hasard(self):
        """Fonction qui permet à un joueur de jouer de façon aléatoire"""
        # On cherche les cases possibles et on en joue une au hasard
        liste_coups_possibles = []
        for i in range(3):
            for j in range(3):
                if self.jeu.plateau[i][j] == '-':
                    liste_coups_possibles.append(i*3+j)
        pos = choice(liste_coups_possibles)
        self.jeu.plateau[pos // 3][pos % 3] = self.symbole
        return True

    def jouer_IA(self):
        """Fonction qui permet à l'IA de jouer"""
        return self.IA.jouer()
