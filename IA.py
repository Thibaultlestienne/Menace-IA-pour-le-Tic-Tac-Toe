""""
Classe chargée de gérer les joueurs du tic tac toe
"""
from random import choice


def transformer_plateau_liste_vers_string(plateau):
    txt = ""
    for ligne in plateau:
        for case in ligne:
            txt += case
    return txt


def transformer_plateau_string_vers_liste(plateau):
    return [[plateau[0], plateau[1], plateau[2]],
            [plateau[3], plateau[4], plateau[5]],
            [plateau[6], plateau[7], plateau[8]]
            ]


class IA:
    """Fonction qui permet à un joueur humain de jouer"""

    def __init__(self, joueur):
        self.joueur = joueur
        self.dico_des_coups_possibles_et_reaction = {}
        self.dico_coups = {}

    def jouer(self):
        """Fonction qui permet à un joueur de jouer de façon aléatoire"""
        # On cherche les cases possibles et on en joue une au hasard
        liste_coups_possibles = []
        for i in range(3):
            for j in range(3):
                if self.joueur.jeu.plateau[i][j] == '-':
                    liste_coups_possibles.append(i * 3 + j)

        string_plateau = transformer_plateau_liste_vers_string(self.joueur.jeu.plateau)
        if string_plateau not in self.dico_des_coups_possibles_et_reaction:
            self.dico_des_coups_possibles_et_reaction[string_plateau] = liste_coups_possibles
        try:
            pos = choice(self.dico_des_coups_possibles_et_reaction[string_plateau])
        except:
            return False
        self.dico_coups[string_plateau] = pos
        self.joueur.jeu.plateau[pos // 3][pos % 3] = self.joueur.symbole
        return True

    def réagir_aux_résultats(self, résultat, commencer):
        if résultat == f'victoire joueur {self.joueur.symbole}':
            if commencer:
                for key, value in self.dico_coups.items():
                    self.dico_des_coups_possibles_et_reaction[key] += [value, value]
            else:
                for key, value in self.dico_coups.items():
                    self.dico_des_coups_possibles_et_reaction[key] += [value, value, value, value]

        elif résultat == 'égalité':
            pass

        else:
            for key, value in self.dico_coups.items():
                self.dico_des_coups_possibles_et_reaction[key].remove(value)

        self.dico_coups = {}

    def former_IA(self, iteration, adversaire, commencer=True,  graphique=False):
        """Fonction qui permet de former l'IA contre un adversaire de son choix
                int iteration = nombre de parties jouées
                Joueur adversaire = adversaire face à qui l'IA se forme
                bool commencer = True si l'IA doit commencer
                bool graphique = True si l'on veut un rapport sur ce qui s'est passé
        """
        if commencer:
            if not graphique:
                for i in range(iteration):
                    résultat = self.joueur.jeu.jouer_une_partie(self.joueur, adversaire)
                    self.réagir_aux_résultats(résultat, commencer)
            else:
                compteur_victoire_joueur = 0
                compteur_victoire_adversaire = 0
                compteur_égalité = 0
                for i in range(iteration):
                    résultat = self.joueur.jeu.jouer_une_partie(self.joueur, adversaire)
                    self.réagir_aux_résultats(résultat, commencer)
                    if résultat == 'égalité':
                        compteur_égalité += 1
                    elif résultat == f'victoire joueur {self.joueur.symbole}':
                        compteur_victoire_joueur += 1
                    elif résultat == f'victoire joueur {adversaire.symbole}':
                        compteur_victoire_adversaire += 1
                print("------------------")
                print(f"victoire {self.joueur.symbole} {compteur_victoire_joueur}")
                print(f"victoire {adversaire.symbole} {compteur_victoire_adversaire}")
                print(f"égalité {compteur_égalité}")
                print("------------------")
        else:
            if not graphique:
                for i in range(iteration):
                    résultat = self.joueur.jeu.jouer_une_partie(adversaire, self.joueur)
                    self.réagir_aux_résultats(résultat, commencer)
            else:
                compteur_victoire_joueur = 0
                compteur_victoire_adversaire = 0
                compteur_égalité = 0
                for i in range(iteration):
                    résultat = self.joueur.jeu.jouer_une_partie(adversaire, self.joueur)
                    self.réagir_aux_résultats(résultat, commencer)
                    if résultat == 'égalité':
                        compteur_égalité += 1
                    elif résultat == f'victoire joueur {self.joueur.symbole}':
                        compteur_victoire_joueur += 1
                    elif résultat == f'victoire joueur {adversaire.symbole}':
                        compteur_victoire_adversaire += 1
                print("------------------")
                print(f"victoire {self.joueur.symbole} {compteur_victoire_joueur}")
                print(f"victoire {adversaire.symbole} {compteur_victoire_adversaire}")
                print(f"égalité {compteur_égalité}")
                print("------------------")

    def purifier_mémoire_IA(self):
        """Fonction chargée de purifier la liste des coups que l'IA veut jouer
        Si la liste est vide on la reinitialise
        si la liste est trop longue on la raccourcit
        """
        for key, value in self.dico_des_coups_possibles_et_reaction.items():
            if value == []:
                plateau_liste = transformer_plateau_string_vers_liste(key)
                for i in range(3):
                    for j in range(3):
                        if plateau_liste == '-':
                            value.append(i * 3 + j)

            elif len(value) > 10000: # évite les boites trop pleines
                longeur = len(value)
                nb0 = value.count(0)
                nb1 = value.count(1)
                nb2 = value.count(2)
                nb3 = value.count(3)
                nb4 = value.count(4)
                nb5 = value.count(5)
                nb6 = value.count(6)
                nb7 = value.count(7)
                nb8 = value.count(8)
                value = int((nb0 / longeur)-1) * [0] + \
                        int((nb1 / longeur)-1) * [1] + \
                        int((nb2 / longeur)-1) * [2] + \
                        int((nb3 / longeur)-1) * [3] + \
                        int((nb4 / longeur)-1) * [4] + \
                        int((nb5 / longeur)-1) * [5] + \
                        int((nb6 / longeur)-1) * [6] + \
                        int((nb7 / longeur)-1) * [7] + \
                        int((nb8 / longeur)-1) * [8]
