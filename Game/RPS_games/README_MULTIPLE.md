# Auteur : Martin CHARRONDIERE

RPS_MultipleGame

# Objectif & Principe

Modélise en python une partie approfondie de RPS, entre un joueur et l'ordinateur. Les fonctions sollicitées comparent les coups joués par les deux partis, et renvoient un résultat selon lequel des deux a gagné, ou s'il y a égalité.
En fonction de l'identité de l'utilisateur en train de jouer, un fichier texte est créé et édité pour stocker tous ses coups au fur et à mesure des manches disputées. Une base de données se forme ainsi nominativement sur les différents utilisateurs ce qui permettra dans les fonctionnalités suivantes d'adapter l'ordinateur aux stratégies les plus fréquemment utilisées par ses différents adversaires, augmentant ainsi le niveau de diffuckté du jeu progressivement.

# Contenu

- Jouer une partie entre un joueur et l'ordinateur.
- Déterminer le vainqueur en fonction des choix des joueurs (Pierre, Papier ou Ciseaux).
- Générer un choix aléatoire pour l'ordinateur.
- Interface simple en ligne de commande pour l'interaction avec l'utilisateur.
- Ecrire dans un fichier texte nominatif créé si inexistant au préalable.
- Stocker et modifier l'identité du joueur en train de participer.

# Utilisation
 
Voici un exemple d'utilisation :

```python
from RPS_MultipleGame import RPS_MultipleGame

game = RPS_MultipleGame()

# Jouer une partie entre un joueur et l'ordinateur
resultat = game.deux_joueursmultiple("R")