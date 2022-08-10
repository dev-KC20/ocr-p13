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
  - [Refactoring ](#refactor)
  - [Tests passed](#tests-passed)
  - [Crédits and good reads](#credits-and-good-reads)
  - [PEP 8 check](#pep-8-check)


  
## Disclaimer

---

This code is the last part of the openclassrooms learning adventure split in 13 business alike projects. 

As a junior developper of the OC Lettings company, you've been asked to refactor the Lettings web site as well as to include the refreshed site into a continuous integration and a continuous delivery process **CI/CD**.
  
  
Some materials or links here may have rights to be granted to https://openclassrooms.com. 
The additionnal material follows "CC BY-SA ".
  
** Not to be used for production **  

---

## Introduction

...




Orange County Lettings decided to include its web site into a continuous improvement wheel.  
Three means to run the OC Lettings web site are available :  
  
![](img/p13-where-to-run.png)  
  
**Have fun, Devs!**
  

## 1. local  

`instructions were tested on Windows10, VSCodium 1.70, Python 3.10, Django 4.0`

In order to install and use locally the O.C. Lettings site, assuming you have Python 3 installed on your computer, open a bash prompt and : 


1.  clone the ocr-p13 directory into your local copy.  
    `git clone https://github.com/dev-KC20/ocr-p13.git`   
  
2.  move to the working directory   
    `cd ocr-p13`   
  
3. create a python virtual environment named ENV  
    `python -m venv ENV`   
  
4.  do not forget to active the ENV virtual environment  
    `ENV\scripts\activate.bat`   

5.  install all the requirements,  
    `pip install -r requirements.txt`   

6.  create a .env file in order to keep all secrets local and safe (see hereunder for details),  
   
``` 
| where |(l)|(c)|(h)|   what key           |        content                  |  
|-------| --| --| --|----------------------|---------------------------------|  
|       | X | X | X | SECRET_KEY           | *yourverystrongandsecurekey*    |  
|       | O | O | O | DEBUG                | False                           |  
|       | O | O | O | ALLOWED_HOSTS        | localhost, 127.0.0.1,.heroku.com|  
|       |   |   | O | CSRF_TRUSTED_ORIGINS |         .herokuapp.com          |  
|       | X | X | X | DISABLE_COLLECTSTATIC|         1                       |  
|       |   | X |   | HEROKU_API_KEY       | *yourherokuapikey*              |  
|       |   | X |   | HEROKU_APP_NAME      | the-app-name-from-heroku        |  
|       | X | X |   | DOCKER_USERNAME      | yourdockerhubaccount            |  
|       | X | X |   | DOCKER_PASSWORD      | *yourdockerhubpassword*         |  
|       | X | X | X | SENTRY_DSN           | sentry-url-to-sent-events-to    |  

(l): local including local container  
(c): circleci  
(h): heroku   
 X: same value everywhere  
 O: depending on context  
and used to store images on the dockerhub: IMAGE_REPO=oclettings-image-repo
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
  
We assume that you have a running docker daemon set on your computer.  

![](img/p13-dockerhub-tags-2022-08-09-190600.png)  

OC Lettings provides a proofchecked docker image that you collect by the following instructions:  

1. pull the lastest image available:  
    `docker pull $DOCKER_USERNAME/$IMAGE_REPO:$CIRCLE_SHA1`     

2. get and write down the docker image tag:  
    `docker images -q $DOCKER_USERNAME/$IMAGE_REPO`     

3. run the docker image tag:  
    `docker run --env-file .env -d -p 8000:8000 docker-image-tag`     

4. open your browser and navigate to:  
    `https://localhost:8000`      
    or  
    `https://localhost:8000/admin/`    

    remember credentials were provided on step 8. of the above '1. local' section. 

 
You could also do stepS 1,2 &3 in one by:   
    `docker run --env-file .env -p 8000:8000 -i -t $DOCKER_USERNAME/$IMAGE_REPO:$CIRCLE_SHA1`     
  
![](img/p13-docker-local-run-2022-08-09-191638.png)  
  


## 3. remote

OC Lettings had already a good practise to commit its source code changes to a github repo.  
We decided to add remote checks of the source base for linting issues as well as tests regression.  
If successfull, a docker image is built and store on the company DockerHub repo.  
It is this very image that we recommend the developer use when they need to locally run the OC Lettings web site.  
  
The last part of our CI/CD pipeline is to push the image to our heroku app and run it from there.
  
![pipeline organisation](img/p13-pipeline-organisation.png)  
  
Also shown on the picture, the monitoring is done thru the sentry.io solution.


### What do you need to run the CI/CD pipeline

- GitHub account in order to clone and host your own code  
    
![github repo](img/p13-github-repo-2022-08-09-191023.png)  
   
- Circleci account in order to design and operate the CI/CD pipeline  
  
![circleci](img/p13-circleci-pipelines-2022-08-09-190809.png)  
   
- Dockerhub account in order to push and pull the web app images from and to.  


- Heroku account in order to run the web app image.

![heroku deploy](img/p13-heroku-activity-2022-08-09-190350.png)  

- Sentry account in order to hook it to your app logs and set email alerts in case of issues during the operations.
  
![sentry monitoring](img/p13-sentry-events-2022-08-09-190036.png)  



---

 
## Security and privacy  
    
    Orange County Lettings and its co-workers do take your privacy and your data safety very seriously. 
    Our IT team has set several security measures to ensure nothing bad may happen to your data.  
  
    All technical operations are logged and help us to prevent and identify any mis-behavior or attacks

    Finally the code itself is secured by reducing the exposure of secrets to public repositories,   


### Secret's management

    Django uses "secret" to generate its certificates and advises to keep the secret key, secret.
    OC Lettings uses the python-decouple module to replace the secret key's values of the settings.py file by their decouple link :
    Storing actual secret in a .env file make its possible to keep them local provided one does exclude the .env file from the commits by regitering it in .gitignore.  
  
    When being remote, it is important that one creates environment variables of the same key and values as the ones stored locally in the .env file. 
    When remote, some key's value require a small change like the following one :  
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