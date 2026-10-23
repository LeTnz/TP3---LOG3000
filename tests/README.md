# Module `tests`

Ce répertoire contient les tests de la calculatrice. `test_calculator.py`
couvre les quatre opérations, le comportement attendu du parseur d'expressions,
les erreurs de validation et la route Flask.

## Exécution

Depuis la racine du projet :

```powershell
python -m unittest discover -s tests -v
```

Les échecs observés sur la version initiale sont des preuves reproductibles
pour les Issues GitHub. Ils doivent disparaître après les corrections réalisées
sur les branches correspondantes.
