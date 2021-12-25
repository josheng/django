# django
testing out django framework

installed everything via python3 -m pip install (module)

ran local server using python3 manage.py runserver, similar to rails s

# Some useful commands

python3 manage.py makemigrations polls -> run this to create the model/migration file
python3 manage.py migrate -> this will do the migration
python3 manage.py shell -> to launch interactive python shell

# things to take note
create templates(html files) in app folder, this allows views to use the corresponding html files
use render() or 404 shortcut to render the views
django uses context variable, aka instance variable from rails
django seems to perform the logic in views? (update again when i finish django's tutorial)
define url path in urls.py in the app folder -> have to define the relavent views for each path 
