![forthebadge](https://forthebadge.com/images/badges/cc-0.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)  



# ocr-p13 Développez une architecture back-end sécurisée en utilisant Django ORM

![](img/oclet-logo.png)  
  
- Table of Content
  - [Disclaimer](#disclaimer)
  - [Introduction](#introduction)
  - [Quick Start local](#1-local)
  - [Quick Start docker](#2-local-docker)
  - [Quick Start remote](#3-remote)
  - [Security and Privacy](#security-and-privacy)
  - [Tests passed](#tests-passed)
  - [Crédits and good reads](#credits-and-good-reads)
  - [PEP 8 check](#pep-8-check)


  
## Disclaimer

---

This code is the last part of the openclassrooms learning adventure split in 13 business alike projects. 

As a junior deelopper to the OC Lettngs company, I've been asked to refactor the letting site as well as to include the renewed site into a continuous integration and a continuous delivery process **CI/CD**.
  
  
Some materials or links may have rights to be granted by https://openclassrooms.com. 
The additionnal code follows "CC BY-SA ".
  
** Not to be used for production **  

---

## Introduction

...




Orange County Lettings web site

Three means to run the OC Lettings web site are available :

![](img/p13-where-to-run.png)  
  
**Have fun, Devs!**
  



## 1. local

In order to install and use locally the O.C. Lettings site, assuming you have Python 3 installed on your Windows computer, open bash prompt: 

1.  clone the ocr-p13 directory into your local copy.  
    `git clone https://github.com/dev-KC20/ocr-p13.git`   
  
2.  move to the working directory   
    `cd ocr-p13`   
  
3. create a python virtual environment named ENV  
    `python -m venv ENV`   
  
4.  do not forget to active the ENV virtual environment  
    `ENV\scripts\activate.bat`   

5.  install all the requirments,  
    `pip install -r requirements.txt`   

6.  create a .env file in order to keep all secrets local and safe (see hereunder for details),  
     ``` 
        SECRET_KEY = *"yourverystrongandsecurekey"*
        DEBUG = True
        HEROKU_API_KEY=*"yourherokuapikey"*
        HEROKU_APP_NAME="the-app-name-from-heroku"
        DOCKER_USERNAME=yourdockerhubaccount
        DOCKER_PASSWORD=yourdockerhubpassword
        IMAGE_REPO=oclettings-image-repo
        SENTRY_DSN=the-sentry-url-to-sent-events-to
        ALLOWED_HOSTS=localhost, 127.0.0.1

     ``` 

      
7. create and run Django models migration    
    `python manage.py makemigrations`     
    `python manage.py migrate`    
    
8. the Django superuser is:   
    `Username: admin`  
    `Password: Abcd1234!`  

9. Eventually run the server and follow instructions   
    `python manage.py runserver`     






## 2. local docker
  
![](img/p13-dockerhub-tags-2022-08-09-190600.png)  
  
  
![](img/p13-docker-local-run-2022-08-09-191638.png)  
  


## 3. remote

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
  
![github repo](img/p13-github-repo-2022-08-09-191023.png)  
  
![circleci](img/p13-circleci-pipelines-2022-08-09-190809.png)  
   
![heroku deploy](img/p13-heroku-activity-2022-08-09-190350.png)  
  
![sentry monitoring](img/p13-sentry-events-2022-08-09-190036.png)  



Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---

 
## Security and privacy  
    
    Orange County Lettings and its co-workers do take your privacy and your data safety very seriously. 
    Our IT team has set several security measures to ensure nothing bad may happen to your data.  
  
    All technical operations are logged and help us to prevent and identify any mis-behavior or attacks

    Finally the code itself is secured by reducing the exposure of secrets to public repositories,   


### Secret's management

    Django use "secret" to generate its certificates and advises to keep this key secret.
    OC Lettings uses the python-decouple module to replace the secret key's values of the settings.py file by their decouple link :
    Storing actual secret in a .env file make its possible to keep them local provided one does exclude the .env file from the commits by regitering it in .gitignore.  
  
    When being remote, it is important that one creates environment variables of the same key and values as the ones stored locally in the .env file. 
    Some keys require a small change like :  
                                                                                             `ALLOWED_HOSTS=.herokuapp.com`  
  
  



## Tests passed  

![](img/p13-pytest-pass-2022-08-09-191825.png)  
  
  

## Credits and good reads.

Openclassrooms and even more the DA Python discord gals & guys!

Offical [Django](https://docs.djangoproject.com/fr/4.0/topics/security/#sql-injection-protection), [DRF](https://www.django-rest-framework.org/) et [pytest](https://docs.pytest.org/en/7.1.x/) documentation!  
...
  
  
## PEP 8 check
  
`flake8`   
  
  
```bash  
(ENV) \dev\python\ocr\ocr-p13>flake8 
  
(ENV) \dev\python\ocr\ocr-p13>  
```  