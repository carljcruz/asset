$makemigrations = 'python manage.py makemigrations assets'
$migrate = 'python manage.py migrate'

Invoke-Expression $makemigrations


Invoke-Expression $migrate