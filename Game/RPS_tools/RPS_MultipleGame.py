"""Version plus performante de la classe SimpleGame, 
comprenant un stockage et une analyse des resultats des partie precedentes"""

import random
import RPS_SimpleGame

class RPS_MultipleGame(RPS_SimpleGame):

    def __init__ (self):
        self.nom = "Nom"
        self.historique = []

    def set_nom (self):
        self.nom = input("Nom du joueur du joueur ?").lower

    def set_historique (self,c):
        self.historique.append(c)

    def deux_joueurs (self):
        choix_ordi = self.RPS_SimpleGame.choisir_ordi()
        choix_joueur = self.RPS_SimpleGame.choisir()
        self.set_historique(choix_joueur)
        self.ecrire(choix_joueur)
        if choix_joueur == choix_ordi:
            return 0
        self.RPS_SimpleGame.deux_joueurs(choix_joueur,choix_ordi)

    def ecrire (self,c):
        doc = open("%s.txt","w+" %(self.nom))
        doc.write("%s\n" %c)
        doc.close




"""if __name__ == "__main__":
    RPS_MultipleGame()"""