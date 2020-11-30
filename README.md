На другой машине необходимо клонировать проект:
https://github.com/rdzhusupov/django-book.git

Создать папку env и окружение virtualenv, активировать окружение, установить нужные пакеты используя команду:

pip install -r requirements.txt

Зайти в папку с проектом, проверить работоспособность (запускаемость) встроенного сервера:

python manage.py runserver

далее перейти по ссылке http://127.0.0.1:8000/book/?format=json