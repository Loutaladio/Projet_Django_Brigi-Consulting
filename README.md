# Brigi+ Consulting — Voyage Express Django

Site vitrine réalisé exclusivement avec Django selon l'architecture MVT, sans base de données, sans modèles et sans ORM.

## Lancer le projet localement

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

Puis ouvrir `http://127.0.0.1:8000/`.

## Structure expliquée

- `brigiplus/settings.py` configure Django, le dossier global `templates/` et les fichiers statiques `static/`. `DATABASES = {}` matérialise la contrainte sans BDD.
- `brigiplus/urls.py` délègue le routage à l'application.
- `voyages/urls.py` contient uniquement des routes nommées, dont le paramètre dynamique `<str:identifiant>`.
- `voyages/views.py` applique la logique MVT : filtrage des données simulées, préparation des contextes, rendu des pages et levée de `Http404`.
- `voyages/donnees.py` remplace une base de données par une liste de dictionnaires contenant 5 offres complètes.
- `templates/base.html` est le template parent. Toutes les pages l'étendent avec `{% extends %}` et utilisent `{% url %}` pour les liens.
- `static/css/style.css` contient le design responsive ; `static/images/` contient les illustrations des destinations.

## Déploiement PythonAnywhere

1. Créer un compte PythonAnywhere et ouvrir une console Bash.
2. Envoyer l'archive du projet, la décompresser, puis se placer dans le dossier contenant `manage.py`.
3. Créer un environnement virtuel :
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 brigiplus-env
   pip install -r requirements.txt
   ```
4. Dans l'onglet **Web**, créer une application **Manual configuration** avec la version Python choisie.
5. Renseigner le chemin de l'environnement virtuel, puis le chemin du fichier WSGI :
   `/home/VOTRE_NOM/projet-django/brigiplus/wsgi.py`
6. Dans le fichier WSGI proposé par PythonAnywhere, utiliser :
   ```python
   import os, sys
   path = '/home/VOTRE_NOM/projet-django'
   if path not in sys.path:
       sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'brigiplus.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
7. Dans **Web > Static files**, ajouter :
   - URL : `/static/`
   - Directory : `/home/VOTRE_NOM/projet-django/static`
8. Recharger l'application. Aucun `migrate` n'est nécessaire puisque le projet n'utilise aucune base de données.

## Points à présenter à l'enseignant

Le projet démontre la séparation MVT : les vues ne contiennent pas de HTML, les templates ne contiennent pas de logique métier lourde et les données sont isolées dans un module dédié. Les liens sont tous construits avec des noms d'URL Django ; une URL inconnue déclenche une page 404 ; l'héritage de `base.html` évite de dupliquer la navigation et le pied de page.
