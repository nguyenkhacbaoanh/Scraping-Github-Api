# Web Scrapping Github
---
#### Réalisé par: `Khac Bao Anh NGUYEN`

# La structure du programme:
```
/project/
        app.py
        /DataBase/
                __init__.py
                db_scrapping.py
        /ScrappingGithub/
                __init__.py
                scrapping.py
        /API/
                __init__.py
                api.py
```

- `scrapping.py` scripts dans `ScrappingGithub` module: scrapper les informations d'un compte de github en cherchant des patterns de html du site.
- `db_scrapping.py` scripts dans `DataBase` module: faire en sort de récuperer des informations du module `scrapping.py` et de transformer en bases de données relationelles en utilisant `ORM SqlAlchemy`.
  Sortie du module est le `database.db`.
- `api.py` scripts dans API module: permettre d'ouvrir un server qui reçoit le request et le répond ce qui contiennent des methodes `GET` `PUT` `UPDATE` `DELETE` (`GET` et `PUT` pour l'instant) et même créer des requêtes ou les interfaces d'utisateur sur des routes.
- `app.py` module: qui gères tous les modules au-dessus en étape par étape et reçoit la demande de l'utilisateur.

# Tester ce projets:
- Dans terminal:
```bash
git clone
cd web-Scrapping-Github
virtualenv -p python3 scrapping-env
source scrapping-env/bin/activate
pip install -r requirements.txt
```
- créer un fichier `.env` et écrire et sauvegarde.
```
port=3000
id=your mail github
password = your password
```
- lancer sur terminal
```bash
python app.py # lancer le server
curl http://localhost:3000/accgithub -X PUT # pour creuser les données
```
- allez sur navigateur `http://localhost:3000/all` ou `http://localhost:3000/accgithub`
