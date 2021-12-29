# django
testing out django framework

installed everything via python3 -m pip install (module)

ran local server using python3 manage.py runserver, similar to rails s

# Some useful commands

python3 -m pip install python-decouple -> install python decouple module

python3 manage.py makemigrations polls -> run this to create the model/migration file

python3 manage.py migrate -> this will do the migration

python3 manage.py shell -> to launch interactive python shell

sudo -u postgres psql -> enter postgres cmd as user postgres for windows

sudo psql -U my.username postgres -> for macos

ALTER USER django CREATEDB; -> grant user django to createdb in psql

CREATE USER username WITH password 'xxxx'; -> create a user with pw to access psql

CREATE DATABASE djangopolls; -> to create the db, in this case its djangopolls

python3 manage.py test polls -> run test

python3 manage.py createsuperuser -> creates admin account for admin site

# things to take note

create templates(html files) in app folder, this allows views to use the corresponding html files

use render() or 404 shortcut to render the views

django uses context variable, aka instance variable from rails

django seems to perform the logic in views? (update again when i finish django's tutorial)

define url path in urls.py in the app folder -> have to define the relavent views for each path

https://docs.djangoproject.com/en/4.0/intro/tutorial05/#the-django-test-client -> this is to test the views
