# Auteur : Martin CHARRONDIERE

RPS_SimpleGame

# Objectif & Principe

Modélise en python une partie élémentaire de RPS, entre deux joueurs ou entre un joueur et l'ordinateur. Les fonctions sollicitées comparent les coups joués par les deux partis, et renvoient un résultat selon lequel des deux a gagné, ou s'il y a égalité.

# Contenu

- Jouer une partie entre deux joueurs.
- Jouer une partie entre un joueur et l'ordinateur.
- Déterminer le vainqueur en fonction des choix des joueurs (Pierre, Papier ou Ciseaux).
- Générer un choix aléatoire pour l'ordinateur.
- Interface simple en ligne de commande pour l'interaction avec l'utilisateur.

# Utilisation
 
Voici un exemple d'utilisation :

```python
from RPS_SimpleGame import RPS_SimpleGame

game = RPS_SimpleGame()

# Jouer une partie entre deux joueurs
resultat = game.deux_joueurs("R", "P")

# Jouer une partie entre un joueur et l'ordinateur
resultat = game.un_joueur("R")