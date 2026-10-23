# Module `templates`

Ce répertoire contient les gabarits HTML rendus par Flask. `index.html` fournit
l'interface de saisie et transmet l'expression au serveur avec un formulaire
POST.

Le gabarit dépend de Flask/Jinja pour `url_for` et la variable `result`.
La construction de l'expression est faite dans le navigateur; son évaluation
reste une responsabilité du backend.
