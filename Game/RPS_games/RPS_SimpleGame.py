"""Ensemble d'outils consacres a une partie unitaire de RPS"""

import random

class RPS_SimpleGame:
    """Modelise une partie de RPS simple, independante des precedentes"""

    def __init__ (self):
        """Constructeur de la classe"""

    def deux_joueurs(self,choix_joueur1,choix_joueur2):
        """Met en place une partie entre deux utilisateurs
        @param les coups decides par les joueurs 1 et 2, R,P ou S
        @return 0 si egalite, 1 si le joueur gagne, 2 si l'ordi gagne
        """
        if choix_joueur1 == choix_joueur2:
            return 0
        return self.comparaison(choix_joueur1,choix_joueur2)

    def un_joueur(self,choix_joueur):
        """Met en place une partie entre un utilisateur et l'ordinateur
        @param choix_joueur le coup decide par le joueur, R,P ou S
        @return 0 si egalite, 1 si le joueur gagne, 2 si l'ordi gagne
        """
        choix_ordi = self.choisir_ordi()
        if choix_joueur == choix_ordi:
            return 0
        return self.comparaison(choix_joueur,choix_ordi)

    def comparaison (self,c1,c2):
        """Compare deux choix pour decider du vainqueur
        @param c1 et c2, chacun etant R,P ou S selon les tirages
        @return 1 ou 2 selon la gagnant
        """
        if (c1=='R' and c2=='S')or(c1=='S' and c2=='P')or(c1=='P' and c2=='R'):
            return 1
        return 2

    def choisir (self):
        """Permet à l'utilisateur de sélectionner le coup à effectuer
        @param /
        @return choix = R, P ou S selon l'input de l'utilisateur
        """
        choix = 0
        while choix not in ["R","P","S"]:
            choix = input("[R] rock, [P] paper, [S] scissors").upper()
        return choix
        
    def choisir_ordi (self):
        """Decide du choix aleatoire de l'ordinateur
        @param /
        @return R,P ou S aleatoirement et equitablement
        """
        rand = 3*random.random()
        if rand < 1:
            return "R"
        if rand < 2:
            return "P"
        return "S"
