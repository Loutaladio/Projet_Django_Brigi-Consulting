# Guide de présentation — Brigi+ Consulting

## 1. Présenter le projet en 30 secondes

« J'ai réalisé un site vitrine pour l'agence fictive Brigi+ Consulting. Le site utilise Django selon l'architecture MVT. La contrainte importante était de ne pas utiliser de base de données : les cinq destinations sont donc définies dans `voyages/donnees.py`, sous forme d'une liste de dictionnaires. Les vues récupèrent ces données et les transmettent aux templates. Les templates sont regroupés à la racine, héritent tous de `base.html`, et les ressources visuelles passent par le système de fichiers statiques de Django. »

## 2. Pourquoi cette arborescence ?

- `manage.py` est le point d'entrée des commandes Django.
- `brigiplus/` est le paquet de configuration du projet : réglages, URL racine et point WSGI.
- `voyages/` est l'application métier. Elle contient les vues, les routes et les données simulées.
- `templates/` est volontairement à la racine, comme demandé dans le cahier des charges. Cela explique la présence de `BASE_DIR / "templates"` dans `settings.py`.
- `static/` regroupe le CSS et les images. `STATICFILES_DIRS` indique à Django où chercher ces ressources.
- `docs/` contient ce support de présentation et `README.md` contient les instructions d'installation et PythonAnywhere.

## 3. Expliquer le MVT

### Modèle

Il n'y a pas de modèle Django, volontairement. La contrainte « sans BDD » interdit l'utilisation des modèles et de l'ORM. Le rôle de stockage minimal est assuré par `voyages/donnees.py`, qui contient une liste Python de dictionnaires.

### Vue

`voyages/views.py` contient cinq fonctions : `accueil`, `destinations`, `detail_destination`, `a_propos` et `contact`. Une vue reçoit une requête, prépare un contexte Python et appelle `render` pour afficher un template. Pour le détail, `next` recherche l'identifiant dans la liste. Si aucun élément ne correspond, la vue lève `Http404`.

### Template

Les fichiers HTML affichent la présentation. `base.html` contient le squelette commun : en-tête, navigation, zone de contenu et pied de page. Les pages utilisent `{% extends 'base.html' %}` et remplissent `{% block content %}`. Les liens internes utilisent systématiquement `{% url 'voyages:nom_de_route' %}` ; aucune URL de navigation n'est écrite en dur.

## 4. Démontrer le routage dynamique

Dans `voyages/urls.py`, la route `destinations/<str:identifiant>/` capture un identifiant, par exemple `zanzibar`. Django appelle alors `detail_destination(request, identifiant)`. La vue cherche ce code dans `DESTINATIONS` et envoie l'objet correspondant au template `detail_destination.html`. Pour tester la limite : `/destinations/inconnue/` retourne une réponse 404 personnalisée.

## 5. Expliquer le formulaire

Le formulaire de `contact.html` est une simulation. En `POST`, la vue constate `request.method == "POST"` et affiche un message de confirmation. Rien n'est enregistré, car enregistrer impliquerait une base de données ou un système de stockage qui n'est pas demandé dans le sujet.

## 6. Expliquer les fichiers statiques

Dans les templates, `{% load static %}` permet de construire le chemin officiel vers les ressources. Une image est appelée ainsi : `{% static destination.image %}`. Le CSS est appelé par `{% static 'css/style.css' %}`. En production PythonAnywhere, l'URL `/static/` est reliée au dossier `static/` dans l'onglet Web.

## 7. Questions possibles du professeur

**Pourquoi `DATABASES = {}` ?** — Pour rendre explicite que le projet n'a aucune base de données configurée. Il n'y a ni fichier `models.py`, ni migration, ni appel à l'ORM.

**Pourquoi une application `voyages` ?** — Pour séparer la fonctionnalité métier du paquet de configuration `brigiplus`. Même pour un petit projet, cela montre la logique d'organisation Django.

**Pourquoi utiliser `app_name` ?** — Pour créer un espace de noms (`voyages:accueil`) et éviter les collisions si d'autres applications sont ajoutées.

**Que se passe-t-il si une destination est supprimée ?** — Elle disparaît automatiquement du catalogue puisque les cartes sont générées avec une boucle sur la liste. Le détail d'un ancien identifiant retourne 404.

**Comment déployer ?** — Installer les dépendances dans un environnement virtuel, déclarer le fichier `brigiplus/wsgi.py`, ajouter le chemin statique `/static/` vers le dossier `static/`, puis recharger l'application. Aucun `migrate` n'est nécessaire.
