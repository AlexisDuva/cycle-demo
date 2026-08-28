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
