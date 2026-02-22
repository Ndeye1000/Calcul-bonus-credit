# Calcul Bonus Crédit

## Description

Ce projet contient un programme Python qui calcule le montant de crédits obtenus en fonction d'un pourcentage de bonus et du montant d'un achat.

## Fonctionnalité

Le programme calcule les crédits bonus selon la formule suivante :

```
Crédits = montant / (100 / bonus) + montant
```

Par exemple, avec un bonus de 500% et un achat de 5000 FCFA :

- Crédits = 5000 / (100 / 500) + 5000 = 5000 / 0.2 + 5000 = 30000 FCFA

## Installation

Aucune dépendance externe requise. Python 3.x est nécessaire.

## Utilisation

Exécutez le programme :

```bash
python bonus.py
```

Le programme vous demandera :

1. Votre pourcentage de bonus (ex: 500 pour 500%)
2. Le montant de votre achat en FCFA

Il affichera ensuite le montant total de crédits obtenus.

### Exemple

```
Si votre bonus est de 500 %, entrez 500 : 500
Entrez le montant de votre achat : 5000
Vous avez obtenu 30000.0 FCFA de credits. Felicitations 🎉
```

## Fichiers

- `bonus.py` : Script principal contenant la fonction de calcul
- `README.md` : Cette documentation

## Auteur

Ndeye Sermy Mergane