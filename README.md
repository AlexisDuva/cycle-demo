# cycle-demo

App Flask minimale ("Hello World") servant de support à un cycle de développement
itératif complet : build → test → CI/CD → déploiement → monitoring.

## Prérequis

- Python 3.8+

## Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

## Lancer l'app

```bash
python app.py
```

L'app répond sur http://127.0.0.1:5000 avec `Hello World`.

## Déploiement (Render)

Le fichier `render.yaml` décrit le service (Blueprint Render) :

- serveur de prod : `gunicorn app:app`
- `autoDeploy: true` → chaque push sur `main` redéploie
- health check sur `/`
- plan `free` (l'instance se met en veille après ~15 min d'inactivité)

Mise en place initiale :

1. Sur https://dashboard.render.com → **New > Blueprint**
2. Connecter le repo GitHub `AlexisDuva/cycle-demo`
3. Render lit `render.yaml` et crée le service

L'URL publique sera de la forme `https://cycle-demo.onrender.com`.
