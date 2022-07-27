# pull official base image
FROM python:3-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory within the container
WORKDIR /oc_lettings

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /oc_lettings/
RUN pip install -r requirements.txt

# copy project
ADD . /oc_lettings/

# # run the server -> use docker-compose instead
# CMD python manage.py runserver 0.0.0.0:8000