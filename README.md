На другой машине необходимо клонировать проект:
https://github.com/rdzhusupov/django-book.git

Создать папку env и окружение virtualenv, активировать окружение, установить нужные пакеты используя команду:

pip install -r requirements.txt

Зайти в папку с проектом, проверить работоспособность (запускаемость) встроенного сервера:

python manage.py runserver