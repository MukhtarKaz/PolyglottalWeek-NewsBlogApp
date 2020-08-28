# "This was created during my time as a student at Code Chrysalis."

##   A News Blog Application, made during the Polyglottal Week

## Author

- Mukhtar Otarbayev @MukhtarKaz


##  The main purpose of the app:  
    1. Reading IT news from Informationweek.com newsfeed RSS.
    2. Weather news from BBC newsfeed RSS.
    3. Posting own blogs
    4. User can have own account


## Backend Part

  The Python Flask Framework has been used to create all backend parts of the application.

## Frontend Part

  Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

  <title>{% block title %}{% endblock %}</title>
  <ul>
  {% for user in users %}
    <li><a href="{{ user.url }}">{{ user.username }}</a></li>
  {% endfor %}
  </ul>

  Jinja uses a template inheritance

## Database

  SQLite is used to store data

## Database ORM

  SQL Alchemy ORM
    pip install flask-sqlalchemy
  
  $ python

from flaskblog import db

db.create_all()
from flaskblog import User
Post # import table template
user_1 = User(username='tokyo', email='tokyo@japan.com', password='password')
db.session.add(user_1)
db.session.commit()

User.query.all() - get all users
User.query.first() - get first user
User.query.filter_by(username='tokyo').all() - get user by filter
User.query.get(1) - get user by id

db.drop_all() - drop database
db.create_all() - create database

## Form Validation with WTForms

  pip install flask-wtf
  pip install email_validator

## Create a secret key

CLI
$ python
$ import secrets
\$ secrets.token_hex(16)

The result will be a random secret key


## Create hash using Bcrypt

pip install flask-bcrypt
bcrypt.generate_password_hash('test') - creates bite version of hash
bcrypt.generate_password_hash('test').decode('utf-8') - creates string version of hash

check password
bcrypt.check_password_hash(hashed password, 'password')


## Creating login system

pip install flask-login

## Solve lint problems

pip install pylint-flask

In case of Visual Studio Code: Open File > Preferences > Settings > Edit in settings.json as below:
"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
