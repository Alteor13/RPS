"""Ensemble d'outils consacrés à une partie de RPS"""

import random

class RPS_SimpleGame:
    """Modelise une partie de RPS"""

    def deux_joueurs(self,choix_joueur1, choix_joueur2):
        """Met en place une partie entre deux utilisateurs"""
        if choix_joueur1 == choix_joueur2 :
            return 0
        return self.comparaison(choix_joueur1,choix_joueur2)

    def un_joueur(self,choix_joueur):
        """Met en place une partie entre un utilisateur et l'ordinateur"""
        choix_ordi = self.choisir()
        if choix_joueur == choix_ordi:
            return 0
        return self.comparaison(choix_joueur,choix_ordi)

    def comparaison (self,c1,c2):
        """Compare deux choix pour décider du vainqueur"""
        if (c1=='R' and c2=='S')or(c1=='S' and c2=='P')or(c1=='P' and c2=='R'):
            return 1
        return 2

    def choisir (self):
        """Decide du choix aleatoire de l'ordinateur"""
        rand = 3*random.random()
        if rand < 1:
            return 'R'
        if rand < 2:
            return 'P'
        return 'S'
