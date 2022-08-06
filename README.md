![forthebadge](https://forthebadge.com/images/badges/cc-0.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)  



# ocr-p13 Développez une architecture back-end sécurisée en utilisant Django ORM

- Table of Content
  - [Disclaimer](#disclaimer)
  - [Old site instruction](#to-refactor)
  - [Introduction](#introduction)
  - [Quick Start](#quick-start)
  - [Security and Privacy](#security-and-privacy)
  - [Orange County Lettings API documentation](#Epic-Events-API-documentation)
  - [Tests passed](#tests-passed)
  - [Crédits and good reads](#credits-and-good-reads)
  - [PEP 8 check](#pep-8-check)


  
## Disclaimer

---

This code is part of the openclassrooms learning adventure split in 13 business alike projects.  
  
  
Some materials or links may have rights to be granted by https://openclassrooms.com. 
The additionnal code follows "CC BY-SA ".
  
** Not to be used for production **  

---

## To Refactor

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

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

## Introduction

...

**Have fun, Devs!**



## Quick start


In order to install and use locally the O.C. Lettings solution, assuming you have Python 3 installed, open bash prompt: 

1.  clone the ocr-p13 directory into your local copy.  
    `git clone https://github.com/dev-KC20/ocr-p13.git`   
  
2.  move to the working directory   
    `cd ocr-p13`   
  
3. create a python virtual environment named ENV  
    `python -m venv ENV`   
  
4.  do not forget to active the ENV virtual environment  
    `ENV\scripts\activate.bat`   

5.  install all the requirments,  
    `pip install -r requirements-dev.txt`   

6.  move into the source directory,  
    `cd oclets`       
  
7.  create a .env file in order to keep all secrets local and safe (see hereunder for details),  
     ``` 
        SECRET_KEY = *"yourverystrongandsecurekey"*
        DEBUG = True
        # db postgreSQL
        PG_NAME = oclets
        PG_USER = admin-oc
        PG_PASSWORD = *"yourverystrongandsecurepassword"*
        PG_HOST = localhost
        ADMIN_ID = admin-oc
        ADMIN_PASSWORD = *"yourverystrongandsecurepassword"*
        #PYTHONPATH = *"yourlocalpathtopython"*
        ALLOWED_HOSTS=localhost, 127.0.0.1 
        #.herokuapp.com
     ``` 
  
8.  download PostgreSQL database from [PostgreSQL: Downloads](https://www.postgresql.org/download/) and follow their instructions.  
   
    You will have to provide an account and password for PostgreSQL root user.  
    Our team uses psql in version 14 and also installed the full SQL admin studio 'pgAdmin 4'  
  
9.  open the psql shell provided with at step 8. and connect to the database  
```  
            psql  
            Server [localhost]:  
            Database [postgres]:  
            Port [5432]:  
            Username [postgres]: PostgreSQL root user  
            Mot de passe pour l'utilisateur PostgreSQL root user :  
```  
11. create a dedicated database for the Orange County Lettings CRM,  
```sql  
            CREATE DATABASE oclets  
                WITH  
                OWNER = "PostgreSQL root user"  
                ENCODING = 'UTF8'  
                LC_COLLATE = 'French_France.1252'  
                LC_CTYPE = 'French_France.1252'  
                TABLESPACE = pg_default  
                CONNECTION LIMIT = -1;  
  
            ALTER ROLE "PostgreSQL root user" SET default_transaction_isolation TO "read committed";  
            ALTER ROLE "PostgreSQL root user"  SET timezone TO "UTC";  
            GRANT ALL PRIVILEGES ON DATABASE "oclets" TO "PostgreSQL root user";  
            ALTER USER "PostgreSQL root user" CREATEDB;  
```  
     
      
12. back to the python prompt, build and run Django models migration    
    `python manage.py makemigrations`     
    `python manage.py migrate`    
    
13. create a Django superuser  
    `python manage.py createsuperuser`     
    Username: ADMIN_ID  
    Email address: adminoc@mail.fr  
    Password: ADMIN_PASSWORD  
    Password (again):  

14. Eventually run the server  
    `python manage.py runserver`      
   
  
## Security and privacy  
    
    Orange County Lettings and its co-workers do take your privacy and your data safety very seriously. 
    Our IT team has set several security measures to ensure nothing bad may happen to your data.  
    Orange County Lettings publishes a developper technical guide which requires to protect our solutions 
    against top 10 "owasp" security threats (see also the "credits and good reads" section).  
  
    First of all, we introduced the segregation of duties in how our staff is interacting with your data.  
    Only the manager level has full access whereas salesmen only work on prospection and 
    contract and the support team only care about the events we organize.  
 
  
|dep./object  |	User      |  Customer | Contract |	Event    |    
|-------------|-----------|-----------|----------|-----------|    
|anonymous    |	forbidden |	forbidden | forbidden|	forbidden|    
|sales_team   |		      |  [CR]UDL  |    RL    |  RL       |    
|sales_contact|		      |   inherit |own [CR]UD|	own [CR] |    
|support_team |		      |    RL	  |    RL	 |    RL     |    
|supp_contact |			  |     	  |          |   own UD  |    
|managmnt_team|	  CRUDL   |	  CRUDL	  |  CRUDL	 |  CRUDL    |    
  
    For instance, creating user or clients cannot be done thru our exposed back-end API server
     but need to use a dedicated Admin front-end whose access is strongly restricted.  
      
    On the exposed back-end API server side, we ensure that front-end clients don't temper 
    with the url or the json request body they send to the server.  
  
    All technical operations are logged and help us to prevent and identify any mis-behavior 
    or attacks

    Finally the code itself is secured by reducing the exposure of secrets to public repositories,   


### Secret's management

    Django use "secret" to generate its certificates and advises to keep this key secret.
    Epinc Events uses the python-decouplemodule to replace the secret key's values of the 
    settings.py file by their decouple link :
    Storing actual secret in a .env file make its possible to keep them local provided one 
    does exclude the .env file from the commits by regitering it in .gitignore.  
  
    For learners we, for ones allowed the commit of this (fake) .env file.  

    ```py
    from decouple import config
    ...
    SECRET_KEY = config("SECRET_KEY")

    ```  

## Orange County Lettings API documentation


Postman documentation link 



### Business workflow

We could suggest the following workflow to support an event:

1. Sales adds the new prospect. 
2. ...

The application structure includes basically 3 levels of embedded models : Clients, Contracts, Events.

For these, the basic CRUD methods are provided thru the available end-points.

The permissions are granted following the user's role in the workflow:

1. Only authenticated user can acces end-points.
2. Only staff can access the admin site.
3. Only Superuser can create a superuser
4. Only Sales creates from Client, Contract, Event
5. Only Support updates the Event

Authentication is managed with Django auth `django.contrib.auth` as well as with ` simple-jwt`  tokens.
Authorization is managed thru the ` has_permission`  method of the permission class 

If you need mock user data for the above role segregation, here is what we suggest:

![](img/p12-sample-data.png)  
  
(A) Support ; (M) Management ; (S) Sales.

Two front ends app are needed for the workflow:
* the provided (and hidden) Django Admin
* the Postman client side.

For the latter, remember when checking User permissions that "admin-oc" is also 
the Orange County Lettings API superuser.


## Tests passed  


### Django ApiTestCase pass 9/9


## Credits and good reads.

Openclassrooms and even more the DA Python discord gals & guys!

Offical [Django](https://docs.djangoproject.com/fr/4.0/topics/security/#sql-injection-protection), [DRF](https://www.django-rest-framework.org/) et [pytest](https://docs.pytest.org/en/7.1.x/) documentation!  
...


## PEP 8 check

`flake8 --format=html --htmldir=flake8_report


