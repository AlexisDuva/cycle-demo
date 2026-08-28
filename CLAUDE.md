# Contexte du projet

App Flask minimale ("Hello World") servant de support à un cycle de développement itératif complet (build → test → CI/CD → déploiement → monitoring). Objectif : minimiser le temps passé sur le développement lui-même.

**Nom du projet :** `cycle-demo`

**Stack :** Python 3.8+, Flask uniquement — pas de base de données, pas de frontend complexe.

## Tâches de setup

1. Créer un environnement virtuel Python (venv)
2. Installer Flask (`pip install flask`)
3. Créer `app.py` :

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
```

4. Lancer l'app (`python app.py`) et vérifier que `http://127.0.0.1:5000` répond "Hello World"
