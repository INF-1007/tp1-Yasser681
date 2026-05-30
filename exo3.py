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
import math
# TODO: Lire les 4 valeurs
try:
 distance=float(input("Entrez la distance jusqu'au Parc Jean-Drapeau (en kilometres) : "))
 attente_velo=float(input("Entrez le temps d'attente pour un velo en libre-service (en minutes) : "))
 temps_metro=float(input("Entrez le temps du trajet en metro (en minutes) : "))
 controle=float(input("Entrez le temps de controle a l'entree (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
    exit()
# TODO: Validation

for element in distance,attente_velo,temps_metro,controle:
 if element<0:
  print("Erreur - donnees invalides.")
  exit()

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
# - Calculer les temps bruts (minutes) :
#     marche = distance * 60 / 5 + controle
#     velo   = attente_velo + distance * 60 / 15 + controle
#     metro  = temps_metro + controle
# - Arrondir chaque temps a la minute superieure (ceil)
# - Determiner la/les option(s) minimale(s)
marche = math.ceil(distance * 60 / 5 + controle)
velo = math.ceil(attente_velo + distance * 60 / 15 + controle)
metro  = math.ceil(temps_metro + controle)

# TODO: Afficher la phrase exacte

dicto={"marcher":marche,"velo":velo,"metro":metro}
deux_ex_aequo=[ m for m,n in dicto.items() if n==min(dicto.values())]
if marche==velo and marche==metro and velo==metro:
 print("Egalite : marcher, velo et metro.")
elif marche!=velo and marche!=metro and velo!=metro:
  print(f"Option la plus rapide : {min(dicto,key=lambda k: dicto[k])}.")
else:
 print(f"Egalite : {deux_ex_aequo[0]} et {deux_ex_aequo[1]}.")
       


 
