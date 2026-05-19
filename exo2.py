# Exercice 02 - Affluence sur les scenes (P a W) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes devant les scenes P, Q, R, S, T, U, V, W (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par scene : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes P a W
    - afficher "❚" si niveau_scene >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     P Q R S T U V W"
"""

FACTEURS = [1.20, 1.15, 1.05, 0.90, 0.90, 1.05, 1.15, 1.20]

# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter

# TODO: Calculer les intensites brutes (liste de 8 floats)

# TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])

# TODO: Afficher la grille (10 lignes) puis la ligne des labels
