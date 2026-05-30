# -*- coding: utf-8 -*-
# Exercice 01 - Bilan d'ecoute au festival (gabarit)
"""
Objectif :
- DEMANDER : nom complet, spectacles electroniques, duree electronique, spectacles live, duree live
- Valider : spectacles >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Electronique: {A} spectacle(s), {He}h{Me:02d} d'ecoute
    Live: {B} spectacle(s), {Hl}h{Ml:02d} d'ecoute
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de spectacles electroniques assistes au festival : "
3) "Entrez la duree moyenne d'un spectacle electronique (en minutes) : "
4) "Entrez le nombre de spectacles live assistes au festival : "
5) "Entrez la duree moyenne d'un spectacle live (en minutes) : "
"""

# TODO: Lire le nom (str) 
# TODO: Lire les 4 valeurs (int)
try:
 nom_complet=input("Entrez votre nom complet : ")
 spectacles_electroniques=int(input("Entrez le nombre de spectacles electroniques assistes au festival : "))
 duree_electronique=int(input("Entrez la duree moyenne d'un spectacle electronique"
 " (en minutes) : "))
 spectacles_live=int(input("Entrez le nombre de spectacles live assistes au festival : "))
 duree_live=int(input("Entrez la duree moyenne d'un spectacle live (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
    raise SystemExit
# TODO: Valider les donnees (spectacles >= 0, durees > 0)

# TODO: Calculer les minutes totales (electronique, live, total)

# TODO: Convertir en heures/minutes et afficher exactement 4 lignes

duree_total=duree_electronique*spectacles_electroniques+duree_live*spectacles_live
if spectacles_electroniques<0:
    print("Erreur - donnees invalides.")
elif duree_electronique<=0:
        print("Erreur - donnees invalides.")
elif spectacles_live<0:
      print("Erreur - donnees invalides.")
elif duree_live<=0:
      print('Erreur - donnees invalides.')
else:
      print(f"""Bonjour {nom_complet}
Electronique: {spectacles_electroniques} spectacle(s), {duree_electronique*spectacles_electroniques//60}h{duree_electronique*spectacles_electroniques%60:02d} d'ecoute
Live: {spectacles_live} spectacle(s), {duree_live*spectacles_live//60}h{duree_live*spectacles_live%60:02d} d'ecoute
Total: {duree_total//60}h{duree_total%60:02d}""")
