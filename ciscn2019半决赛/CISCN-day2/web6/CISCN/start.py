import os

os.chdir(os.path.dirname(__file__))
while True:
    os.system("python manage.py runserver 0.0.0.0:8000")