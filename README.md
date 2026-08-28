# cycle-demo

![CI/CD](https://github.com/AlexisDuva/cycle-demo/actions/workflows/ci.yml/badge.svg)

App Flask minimale ("Hello World") servant de support à un cycle de développement
itératif complet : build → test → CI/CD → déploiement → monitoring.

## Prérequis

- Python 3.8+

## Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements-dev.txt
```

## Lancer l'app

```bash
python app.py
```

L'app répond sur http://127.0.0.1:5000 avec `Hello World`.

## Qualité (local)

```bash
ruff check .
ruff format --check .
pytest
```

## CI/CD

Workflow : `.github/workflows/ci.yml`

- **CI** (push + pull request sur `main`) : lint `ruff`, tests `pytest`
  avec couverture 100 %, matrice Python 3.8 / 3.10 / 3.12.
- **CD** (push sur `main`, uniquement si la CI passe) : déclenche le déploiement
  Render via un Deploy Hook, attend le redémarrage, puis lance un smoke test
  sur l'URL publique.

L'auto-deploy natif de Render est désactivé (`autoDeploy: false` dans
`render.yaml`) pour que rien ne parte en prod sans tests verts.

### Configuration requise sur GitHub

Dans **Settings > Secrets and variables > Actions** :

| Type   | Nom                  | Valeur |
|--------|----------------------|--------|
| Secret | `RENDER_DEPLOY_HOOK` | URL du Deploy Hook (Render : service > Settings > Deploy Hook) |
| Secret | `APP_URL`            | `https://cycle-demo.onrender.com` |

## Déploiement (Render)

Le fichier `render.yaml` décrit le service (Blueprint Render) :

- serveur de prod : `gunicorn app:app`
- health check sur `/`
- plan `free` (l'instance se met en veille après ~15 min d'inactivité)

Mise en place initiale :

1. Sur https://dashboard.render.com → **New > Blueprint**
2. Connecter le repo GitHub `AlexisDuva/cycle-demo`
3. Render lit `render.yaml` et crée le service

L'URL publique sera de la forme `https://cycle-demo.onrender.com`.
