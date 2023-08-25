# Study Down Under in Django


## How To Setup
```
Create a folder as your vscode workspace in your computer.
```
Make sure to install python and xampp for mysql backend.
```
git clone https://github.com/admingrey/sdu.git
```
```
cd sdu
```
```
```
```
rename "dot_env" file to ".env"
```
```
then change the settings according to your mysql setup in the .env file:

SECRET_KEY=django-insecure-u*f@)2_=kw75$s+l+)41=weevp9*&lfc&ld*p6qog*7!t*45o6
DATABASE_NAME=studenttasktracker       // create this database first in your phpmyadmin(xampp)
DATABASE_USER=root                   
DATABASE_PASSWORD=
DATABASE_HOST=localhost
DATABASE_PORT=3306

```
```
python -m pip install virtualenv
```
```
virtualenv venv
```
```
venv/scripts/activate
```
```
python -m pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
