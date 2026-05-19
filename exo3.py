# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le Parc Jean-Drapeau (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_velo (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche = distance * 60 / 5 + controle
    velo   = attente_velo + distance * 60 / 15 + controle
    metro  = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "velo." ou "metro."
- 2 options ex-aequo (ordre : marcher, velo, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, velo et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "
2) "Entrez le temps d'attente pour un velo en libre-service (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math

# TODO: Lire les 4 valeurs

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)

# TODO: Afficher la phrase exacte
