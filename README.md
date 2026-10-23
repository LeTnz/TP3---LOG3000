# LOG3000 - TP3 : Calculatrice Flask

## Équipe

- Numéro d'équipe :12
- Membres : Ahmed Ben Khalifa et Ahmed Benhamla

## Objectif

Cette application est une calculatrice web simple développée avec Python et
Flask. Elle permet de saisir deux nombres et une opération arithmétique (`+`,
`-`, `*` ou `/`), puis d'afficher le résultat.

## Prérequis

- Python 3.10 ou plus récent;
- pip;
- Git.

## Installation

```powershell
git clone <URL_DU_DEPOT>
cd TP3---LOG3000
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Utilisation

Lancer le serveur depuis la racine du dépôt :

```powershell
python app.py
```

Ouvrir ensuite <http://127.0.0.1:5000/>. Utiliser les boutons pour composer
une expression, cliquer sur `=` pour la soumettre et sur `C` pour l'effacer.

## Tests

Les tests sont dans `tests/`. Ils couvrent les opérations arithmétiques,
le parsing des expressions et la route Flask. Sur la version initiale, certains
tests échouent volontairement et servent à documenter les bogues à corriger.

```powershell
python -m unittest discover -s tests -v
```

## Structure

- `app.py` : serveur Flask et parsing des expressions.
- `operators.py` : opérations arithmétiques.
- `templates/` : interface HTML.
- `static/` : styles CSS.
- `tests/` : tests automatisés.

Chaque répertoire contient un README qui précise ses responsabilités.

## Contribution

Pour chaque issue, créer une branche dédiée (`fix/issue-numero-description`),
ajouter ou mettre à jour un test, corriger le problème, puis exécuter toute la
suite. Ouvrir une Pull Request liée à l'issue, demander une revue et fusionner
seulement après validation.
