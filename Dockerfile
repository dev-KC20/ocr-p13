# pull official base image
FROM python:3

# set environment variables no buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# set work directory within the container
WORKDIR /oc_lettings

# install dependencies
RUN pip install --upgrade pip
ADD requirements.txt /oc_lettings/
RUN pip install --no-cache-dir  -r requirements.txt

# copy project
COPY . /oc_lettings/

# Expose an external port
EXPOSE $PORT
CMD python manage.py runserver 0.0.0.0:$PORT
# rather use the Procfile for heroku
# CMD gunicorn oc_lettings_site.wsgi:application -b 0.0.0.0:8000 -b 0.0.0.0:$PORT