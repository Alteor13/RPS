"""Version plus performante de la classe SimpleGame, 
comprenant un stockage et une analyse des resultats des partie precedentes"""

from RPS_SimpleGame import RPS_SimpleGame as sim

class RPS_MultipleGame(sim):
    """Modelise unepartie de RPS dans laquelle le jeu de l'ordinateur
    dépend des parties précédentes"""

    def __init__ (self):
        """Constructeur de la classe"""
        super().__init__()
        self.nom = "Nom"
        self.historique = []

    def set_nom (self):
        """Permet de modifier l'attribut self.nom d'une instance de la classe
        @param /
        @return /
        """
        self.nom = input("Nom du joueur du joueur ?").lower

    def set_historique (self,c):
        """Permet de modifier l'attribut self.historique d'une instance de la classe
        @param c, le coup que vient de jouer l'utilisateur
        @return /
        """
        self.historique.append(c)

    def deux_joueursmultiple (self):
        """
        @param / 
        @return 0, 1 ou 2 suivant le gagnant de la manche
        """
        choix_ordi = self.choisir_ordi()
        choix_joueur = self.choisir()
        self.set_historique(choix_joueur)
        self.ecrire(choix_joueur)
        if choix_joueur == choix_ordi:
            return 0
        return self.deux_joueurs(choix_joueur,choix_ordi)

    def ecrire(self, c):
        """Ajoute au document .txt associé à un joueur le dernier coup qu'il a joué
        @param c: R, P ou S selon le coup que vient de jouer le joueur
        @return: /
        """
        with open(f"{self.nom}.txt", "a", encoding = "utf-8") as doc:
            doc.write(f"{c}\n")

#if __name__ == "__main__":
#    RPS_MultipleGame()
        