# Web Scrapping Github
---
#### Réalisé par: `Khac Bao Anh NGUYEN`

# La structure du programme:
```
/project/
        app.py
        /module/
                __init__.py
                scrapping.py
                ETL.py
                api.py
```
- `scrapping.py` module: scrapper les informations d'un compte de github en cherchant des patterns de html du site
- `ETL.py` module: faire en sort de récuperer des informations du module `scrapping.py` et de transformer en bases de données relationelles.
  Sortie du module est le `data.db`.
- `api.py` module: permettre d'ouvrir un server qui reçoit le request et le répond, le request est la sortie du `ETL.py` module.
- `app.py` module: qui gères tous les modules au-dessus en étape par étape et  reçoit la demande de l'utilisateur
