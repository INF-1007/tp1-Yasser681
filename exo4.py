# -*- coding: utf-8 -*-
# Exercice 04 - Verification d'une rampe d'acces a une scene (gabarit)
"""
Objectif :
- DEMANDER : hauteur (cm, float) et longueur (m, float)
- Valider : hauteur >= 0 et longueur > 0
- Calculer :
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle = atan(hauteur_m / longueur_m) en degres
- Verifier la conformite : pente <= 12.00

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT :
    Pente: PP.PP%
    Angle: AA.AA deg
    Conforme: OUI|NON
Si NON, afficher une 4e ligne :
    Depassement: DD.DD%

Prompts EXACTS :
1) "Entrez la hauteur a franchir (en centimetres) : "
2) "Entrez la longueur horizontale (en metres) : "
"""

# TODO:
import math
# TODO: Lire hauteur_cm et longueur_m
try:
    hauteur_cm=float(input("Entrez la hauteur a franchir (en centimetres) : "))
    longueur_m=float(input("Entrez la longueur horizontale (en metres) : "))
except:
    ValueError
    print("Erreur - donnees invalides.")
    exit()
# TODO: Validation
if hauteur_cm<0 or longueur_m<=0:
    print("Erreur - donnees invalides.")
    exit()
# TODO: Calcul pente et angle
hauteur_m = hauteur_cm / 100
pente = (hauteur_m / longueur_m) * 100
angle = math.degrees(math.atan(hauteur_m / longueur_m))

# TODO: Affichage exact (+ ligne depassement si necessaire)
if pente<=12:
    Conformite="OUI"
else:
    Conformite="NON"
print(f"Pente: {pente:.2f}%")
print(f"Angle: {angle:.2f} deg")
print(f"Conforme: {Conformite}")
if pente>12.00:
    depassement=pente-12.00
    print(f"Depassement: {depassement:.2f}%")