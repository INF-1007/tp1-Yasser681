[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vTPz04SY)
# TP1 : Exercices d'introduction a Python

:alarm_clock: Date de remise : **Le 31 Mai à 23:59**

:mailbox_with_mail: **À remettre sur GitHub Classroom** (vous devez utiliser les commandes git vues au TP0)

## Introduction

Bienvenue dans cette série de cinq exercices pour votre TP1!

Lors de ces exercices, vous allez devoir écrire des programmes qui permettront d'interagir avec l'utilisateur en lisant des données entrées au clavier. 

En Python, cela se fait à l'aide de la fonction `input()`.

### Lire une donnée

La fonction `input()` permet de lire ce que l'utilisateur écrit au clavier. 

Par exemple:

```python
nom = input("Entrez votre nom: ")
```
La valeur retournée par `input()` est toujours une chaîne de caractères (texte), même si l'utilisateur entre un nombre. 

### Convertir une donnée

Pour effectuer des calculs, il est souvent nécessaire de convertir la chaîne de caractères entrée par l'utilisateur en un nombre.

Par exemple:

```python
age = int(input()) # Pour convertir en nombre entier
distance = float(input()) # avec décimales
```

Dans cet exemple, si l'utilisateur entre une valeur invalide (c'est-à-dire du texte au lieu d'un nombre), Python génère une **erreur**, ce qu'on ne veut pas. 

### Gérer les erreurs avec `try/except`

Afin d'éviter que le programme s'arrête en cas d'erreur, on peut utiliser des blocs `try/except`. 

Par exemple:

```python
try:
    age = int(input())
except ValueError:
    print("Erreur - donnees invalides.")
```

Dans cet exemple:
- Si l'utilisateur entre un nombre valide, la conversion fonctionne normalement
- Si l'utilisateur entre une valeur qui ne peut pas être convertie en entier, une erreur (`ValueError`) se produit
- Le programme affiche alors le message d'erreur au lieu de s'arrêter brutalement.

Dans ce TP, **toutes les entrées doivent être validées à l'aide de blocs `try/except`**. 

### Gestion de contraintes d'entrée

On peut également vouloir imposer d'autres contraintes d'entrée de données à l'utilisateur (ex: doit être un nombre positif, ne peut pas être égal à zéro, etc.). Ces contraintes peuvent être vérifiées après la conversion. 

Par exemple: 

```python
if age < 0:
    print("Erreur - donnees invalides.")

```

**Consignes générales :**
- Respectez **exactement** les formats d'entrée et de sortie demandées (majuscule/minuscule, orthographe, ponctuation, espaces, etc.)
- Aucune erreur Python ne doit apparaître à l'écran lors de l'exécution. Toute entrée invalide (type incorrect ou valeur hors contraintes) doit être gérée à l'aide de blocs `try / except`, comme présenté ci-dessus, et mener à l'affichage du message d'erreur demandé.
- Chaque exercice est indépendant
- Le niveau de difficulté est progressif

## Exercices

Cet été, Montréal accueille le **FestiSon 2026**, un grand festival de musique extérieur qui se déroule au Parc Jean-Drapeau tout au long de la saison estivale. Des dizaines de milliers de festivaliers et de bénévoles sont attendus pour assister à des spectacles électroniques et live sur huit scènes réparties autour du site. Dans le cadre de l'organisation de l'événement, le comité souhaite automatiser quelques calculs liés aux statistiques de participation, à l'estimation de temps de trajet, à la sécurité des infrastructures et à la planification des billets. Ces exercices vous permettront de pratiquer les entrées/sorties, les opérations mathématiques, les conditions, les arrondis, le formatage et de petites boucles de recherche.

## 01. Bilan d'écoute au festival

Écrivez un programme qui salue l'utilisateur puis calcule son temps total d'écoute de spectacles au FestiSon 2026.

**Le programme doit demander à l'utilisateur :**
1) Son nom complet
2) Le nombre de spectacles électroniques assistés (entier)
3) La durée moyenne par spectacle électronique (en minutes, entier)
4) Le nombre de spectacles live assistés (entier)
5) La durée moyenne par spectacle live (en minutes, entier)

**Contraintes de validation des entrées:**
- Tous les nombres doivent être des entiers
- Nombre de spectacles >= 0
- Durée moyenne > 0

En cas d'erreur, afficher exactement :

```text
Erreur - donnees invalides.
```

Sinon, afficher exactement 4 lignes (formatage obligatoire) :

```text
Bonjour NOM
Electronique: A spectacle(s), HhMM d'ecoute
Live: B spectacle(s), HhMM d'ecoute
Total: HhMM
```

Notes :
- Convertissez correctement les minutes en heures et minutes.
- Les minutes doivent être affichées sur 2 chiffres (ex: 11h00, 1h05).

## 02. Affluence sur les scènes
Lors du FestiSon 2026, le comité souhaite visualiser l'affluence autour des scènes avec un diagramme similaire à celui-ci :
![Affluence sur les scènes](https://t4.ftcdn.net/jpg/03/33/23/41/360_F_333234186_rWQQpvHnOnia4l9RIYHQ3UsK5GeHAEOr.jpg)

où les lignes verticales représentent le niveau d'affluence et chaque colonne représente une scène du festival.

Le site du FestiSon est divisé en 8 scènes, nommées P, Q, R, S, T, U, V et W.

Vous devez lire le nombre de personnes présentes devant les 8 scènes,
calculer un niveau d'affluence pour chaque scène, puis afficher ces niveaux sous forme de grille verticale.

### Entrées

Votre programme doit lire **8 nombres entiers**, un par ligne, correspondant au nombre
de personnes devant les scènes **P à W**, dans cet ordre.

Contraintes :
- chaque valeur doit être un entier
- chaque valeur doit être ≥ 0

En cas d'entrée invalide (non entier ou valeur négative), afficher exactement :
```
Erreur - donnees invalides.
```

### Intensité brute de chaque scène

À chaque scène est associé un facteur d'affluence. Voici les valeurs que vous devez utiliser pour chaque scène: 

| Scène   | P    | Q    | R    | S    | T    | U    | V    | W    |
| ------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Facteur | 1.20 | 1.15 | 1.05 | 0.90 | 0.90 | 1.05 | 1.15 | 1.20 |

Pour chaque scène, calculez l'intensité brute :
```
intensité = nombre de personnes × facteur
```

### Normalisation des intensités

Les intensités doivent être converties en niveaux de 0 à 10.

Soit maxI la plus grande intensité brute:

- Si maxI == 0, alors tous les niveaux valent 0
- Sinon :
```
niveau = int((intensite / maxI) * 10 + 0.5)
```

L'ajout de `+ 0.5` avant la conversion avec `int()` sert à arrondir la décimale à l'entier le plus proche (par exemple, 3.2 est arrondi à 3, 3.7 est arrondi à 4, 3.5 est arrondi à 4).

Le niveau final doit être compris entre 0 et 10.

**Affichage:**

Vous devez afficher une grille verticale selon les directives suivantes :
- Lignes : Les niveaux d'affluence (de 10 à 1)
- Colonnes : scènes P à W
- Afficher `❚` si le niveau d'affluence de la scène est ≥ niveau de la ligne
- Sinon, afficher `.`
- La première colonne affiche les niveaux d'affluence (10 à 1), suivi d'un espace et d'une ligne verticale | 
- La dernière ligne affiche les labels des scènes (P à W)
- Les cellules sont séparées par un espace

Exemple de format exact : 
```
10 | ❚ ❚ . . . . ❚ ❚
 9 | ❚ ❚ . . . . ❚ ❚
 8 | ❚ ❚ ❚ . . ❚ ❚ ❚
 7 | ❚ ❚ ❚ . . ❚ ❚ ❚
 6 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚
 5 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚
 1 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚
     P Q R S T U V W
```

## 03. Choisir le meilleur trajet vers le Parc Jean-Drapeau

Écrivez un programme qui compare trois options pour arriver au Parc Jean-Drapeau (marche, vélo en libre-service, métro), en incluant un temps de contrôle à l'entrée du festival pour la vérification des billets. 

**Le programme doit prendre en entrée :**
- Distance jusqu'a ❚
 4 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚
 3 | ❚ ❚ ❚ ❚ ❚ ❚ ❚ ❚
 2 | ❚ ❚ ❚ ❚ ❚ ❚ ❚u Parc Jean-Drapeau (km, float)
- Temps d'attente pour un vélo en libre-service (minutes, float)
- Temps du trajet en métro (minutes, float)
- Temps de contrôle à l'entrée du festival (minutes, float)

**Hypothèses :**
- vitesse de marche = 5 km/h
- vitesse de vélo = 15 km/h

**Calculs (en minutes) :**
- `marche = distance * 60 / 5 + controle`
- `velo = attente + distance * 60 / 15 + controle`
- `metro = temps_metro + controle`

Pour la comparaison, vous devez arrondir chaque temps à la minute supérieure (ceil).

**En sortie, le programme doit faire les affichages suivants:**

- Si une seule option est la plus rapide:

```
Option la plus rapide : X.
```

où X est l'option la plus rapide (`marcher`, `velo` ou `metro`)

- Si 2 options sont ex-aequo et minimales :

```
Egalite : X et Y.
```
où X et Y sont les deux options les plus rapides, avec l'ordre d'affichage suivant : marcher, velo, metro

- Si 3 options sont ex-aequo :

```
Egalite : marcher, velo et metro.
```

- En cas de données invalides (valeurs négatives), afficher exactement :

```text
Erreur - donnees invalides.
```

## 04. Vérification d'une rampe d'accès à une scène

Écrivez un programme qui calcule la pente (%) et l'angle (degrés) d'une rampe d'accès à une scène temporaire, puis vérifie si elle respecte une pente maximale de 12%.

**Entrées :**
- Hauteur à franchir (en centimètres, float)
- Longueur horizontale (en mètres, float)

**Contraintes à respecter:**
- Hauteur >= 0
- Longueur > 0

En cas de données invalides, afficher :

```text
Erreur - donnees invalides.
```

**Calculs :**
- `hauteur_m = hauteur_cm / 100`
- `pente (%) = (hauteur_m / longueur_m) * 100`
- `angle (deg) = atan(hauteur_m / longueur_m)`, converti en degrés

**Sortie**

L'affichage en sortie doit suivre le format suivant:

```text
Pente: PP.PP%
Angle: AA.AA deg
Conforme: OUI|NON
```

Si la rampe ne respecte PAS une pente maximale de 12%, affichez une 4e ligne : 

```text
Depassement: DD.DD%
```

## 05. Planification d'achat de billets de festival

Écrivez un programme qui choisit la combinaison la moins dispendieuse pour acheter au moins `n` billets pour le FestiSon 2026.

**Les options pour acheter des billets sont les suivantes:**
- Forfait de 20 journées : 80.00$
- Forfait de 10 journées : 44.00$
- Forfait de 4 journées  : 18.00$
- Billet journalier      :  5.00$

**Rabais bénévole :**
- Si statut bénévole = O, appliquer 10% de réduction sur les forfaits uniquement
- Les billets journaliers ne sont jamais réduits

**Objectifs :**
- Couvrir au moins `n` billets
- Minimiser le coût total
- En cas d'égalité sur le coût : choisir la solution avec le plus petit nombre de billets total (surplus minimal), puis le plus petit nombre de billets journaliers

En cas de données invalides :

```text
Erreur - donnees invalides.
```

Sinon, afficher exactement 6 lignes :

```text
Forfaits de 20 journees - A
Forfaits de 10 journees - B
Forfaits de 4 journees - C
Billets journaliers - D
Total billets - T
Prix total - PPP.PP$
```

## Fichiers du projet

- README.md : consignes et informations générales
- `exo1.py` : exercice 01
- `exo2.py` : exercice 02
- `exo3.py` : exercice 03
- `exo4.py` : exercice 04
- `exo5.py` : exercice 05
- `test.py` : script de tests automatisés

**Vous devez compléter les exercices à l'intérieur des fichiers `exo1.py` à `exo5.py`.**

**Vous pouvez exécuter le fichier `test.py` pour vérifier vos réponses.**

## Directives pour la remise

Vous devez remettre votre travail avant 23:59 le 20 juin.

Votre travail doit être remis en utilisant les commandes git vues au TP0, sur votre répertoire GitHub créé avec GitHub Classroom. Nous corrigerons votre dernier commit avant la date limite. 

## Barème de correction

| Exercice                                                          | Critère       | Description                                         | Points   |
| ----------------------------------------------------------------- | ------------- | --------------------------------------------------- | -------- |
| **Exercice 1 – Bilan d'écoute au festival**                       |               |                                                     | **/3.5** |
| 1.1                                                               | Entrées       | Lecture du nom et des 4 valeurs numériques          | 0.5      |
| 1.2                                                               | Validation    | Validation des données et message d'erreur exact    | 1.0      |
| 1.3                                                               | Calculs       | Calcul correct des durées électronique et live      | 0.75     |
| 1.4                                                               | Formatage     | Conversion minutes → HhMM (minutes sur 2 chiffres) | 0.75     |
| 1.5                                                               | Sortie        | Affichage exact des 4 lignes demandées              | 0.5      |
| **Exercice 2 – Affluence sur les scènes**                         |               |                                                     | **/5.0** |
| 2.1                                                               | Entrées       | Lecture et validation des 8 scènes (entiers ≥ 0)   | 1.0      |
| 2.2                                                               | Calculs       | Calcul des intensités brutes avec facteurs          | 0.75     |
| 2.3                                                               | Normalisation | Gestion de maxI et du cas maxI = 0                  | 0.75     |
| 2.4                                                               | Arrondi       | Arrondi half-up et bornage des niveaux (0–10)       | 1.0      |
| 2.5                                                               | Affichage     | Grille correcte (symboles, alignement, labels)      | 1.5      |
| **Exercice 3 – Choisir le meilleur trajet vers le Parc J.-D.**    |               |                                                     | **/3.5** |
| 3.1                                                               | Entrées       | Lecture et validation des 4 entrées (floats ≥ 0)   | 1.0      |
| 3.2                                                               | Calculs       | Calcul correct des temps (marche, vélo, métro)      | 1.0      |
| 3.3                                                               | Arrondi       | Application correcte du `ceil`                      | 0.5      |
| 3.4                                                               | Décision      | Comparaison correcte et gestion des égalités        | 1.0      |
| **Exercice 4 – Vérification d'une rampe d'accès à une scène**     |               |                                                     | **/3.5** |
| 4.1                                                               | Entrées       | Lecture et validation des données                   | 0.75     |
| 4.2                                                               | Calculs       | Calcul correct de la pente (%)                      | 0.75     |
| 4.3                                                               | Calculs       | Calcul correct de l'angle (degrés)                  | 0.75     |
| 4.4                                                               | Sortie        | Affichage exact et dépassement si non conforme      | 1.25     |
| **Exercice 5 – Planification d'achat de billets de festival**     |               |                                                     | **/4.5** |
| 5.1                                                               | Entrées       | Lecture et validation de `n` et du statut bénévole  | 1.0      |
| 5.2                                                               | Tarification  | Application correcte des prix et réductions         | 1.0      |
| 5.3                                                               | Couverture    | Combinaison couvrant au moins `n` billets           | 1.0      |
| 5.4                                                               | Optimisation  | Prix minimal, surplus minimal, billets journaliers  | 1.0      |
| 5.5                                                               | Sortie        | Affichage exact des 6 lignes demandées              | 0.5      |
| **Total**                                                         |               |                                                     | **/20**  |
