# Module `tests`

Ce répertoire contient les tests de la calculatrice. `test_calculator.py`
couvre les quatre opérations, le comportement attendu du parseur d'expressions,
les erreurs de validation et la route Flask.

## Exécution

Depuis la racine du projet :

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

La suite contient actuellement 10 tests et vérifie :

- les quatre opérations arithmétiques;
- le refus explicite de la division par zéro;
- le parsing des expressions et le rejet des expressions invalides;
- l'affichage des boutons `2`, `8`, `*` et `/`;
- les réponses GET et POST de la route Flask principale.

Résultat attendu après les corrections :

```text
Ran 10 tests
OK
```

Les tests ont d'abord permis de reproduire les quatre bogues suivis dans les
Issues GitHub. Chaque correction a été réalisée sur une branche dédiée,
validée par le test ciblé, puis intégrée dans `main` par Pull Request. La
commande complète doit être exécutée après chaque fusion afin de vérifier que
les corrections restent compatibles entre elles.
