# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets de festival (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut benevole (O/N)
- Options :
    20 journees : 80.00$
    10 journees : 44.00$
     4 journees : 18.00$
     1 journee  :  5.00$
- Reduction : si benevole = O, appliquer 10% de reduction sur le cout des forfaits uniquement.
  Les billets journaliers ne sont pas reduits.
But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, 
puis le plus petit nombre de billets journaliers

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 20 journees - A
    Forfaits de 10 journees - B
    Forfaits de 4 journees - C
    Billets journaliers - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut benevole (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)
from sys import exit
from math import ceil

# ─── Données de base ─────────────────────────────────────────────
FORFAITS = {20: 80.00, 10: 44.00, 4: 18.00}   # prix bruts
PRIX_JOURNALIER = 5.00

# ─── Lecture et validation ───────────────────────────────────────
try:
    n = int(input("Entrez le nombre de billets necessaires : "))
except ValueError:
    print("Erreur - donnees invalides.")
    exit()

benevole = input("Entrez le statut benevole (O/N) : ").strip().upper()

if n < 0 or benevole not in {"O", "N"}:
    print("Erreur - donnees invalides.")
    exit()

reduc = 0.90 if benevole == "O" else 1.00   # 10 % de rabais sur les forfaits

# ─── Recherche exhaustive de la meilleure combinaison ───────────
best = None  # contiendra (prix_total, total_billets, journaliers, a, b, c)

max20 = n // 20 + 1
max10 = n // 10 + 1
max4  = n // 4  + 1

for a in range(max20 + 1):         # forfaits de 20 j.
    for b in range(max10 + 1):     # forfaits de 10 j.
        for c in range(max4 + 1):  # forfaits de 4 j.
            billets_forfaits = a * 20 + b * 10 + c * 4
            d = max(0, n - billets_forfaits)           # billets à l’unité
            total_billets = billets_forfaits + d

            # coût :
            cout_forfaits = (a * FORFAITS[20] +
                             b * FORFAITS[10] +
                             c * FORFAITS[4]) * reduc
            prix_total = cout_forfaits + d * PRIX_JOURNALIER

            candidat = (prix_total, total_billets, d, a, b, c)

            if best is None or candidat < best:
                best = candidat

# ─── Sortie ───────────────────────────────────────────────────────
prix, total_billets, D, A, B, C = best

print(f"Forfaits de 20 journees - {A}")
print(f"Forfaits de 10 journees - {B}")
print(f"Forfaits de 4 journees - {C}")
print(f"Billets journaliers - {D}")
print(f"Total billets - {total_billets}")
print(f"Prix total - {prix:.2f}$")