### This is polyglootal week

## Template

Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

<title>{% block title %}{% endblock %}</title>
<ul>
{% for user in users %}
  <li><a href="{{ user.url }}">{{ user.username }}</a></li>
{% endfor %}
</ul>

Jinja uses a template inheritance

### Form Validation with WTForms

pip install flask-wtf
pip install email_validator

### Create a secret key

CLI
$ python
$ import secrets
\$ secrets.token_hex(16)

the result will be a random secret key

## Creating and working with database

### Install ORM SQL Alchemy

pip install flask-sqlalchemy

## Create DB using sqlite

\$ python

from flaskblog import db

db.create_all()
from flaskblog import User, Post # import table template
user_1 = User(username='tokyo', email='tokyo@japan.com', password='password')
db.session.add(user_1)
db.session.commit()

User.query.all() - get all users
User.query.first() - get first user
User.query.filter_by(username='tokyo').all() - get user by filter
User.query.get(1) - get user by id

db.drop_all() - drop database
db.create_all() - create database

## Create Package Structure in Flask

Modules have been restructured

## Create hash using Bcrypt

pip install flask-bcrypt
bcrypt.generate_password_hash('test') - creates bite version of hash
bcrypt.generate_password_hash('test').decode('utf-8') - creates string version of hash

check password
bcrypt.check_password_hash(hashed password, 'password')

Debugger Mode in Flask

You can use Debugger Mode when an error throws  by entering pin from terminal where a server is running.

## Creating login system

pip install flask-login

## Solve lint problems

pip install pylint-flask

In case of Visual Studio Code: Open File > Preferences > Settings > Edit in settings.json as below:
"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]

## Resize pictures by Pillow
pip install Pillow

## Others

### About Flask, and generally about Python

1. Good suggestion if you make error
2. Good Exception handling
3. Circular import -
4. Python ternary operator - "do something" if true else "do another thing"

##  Difference between JS and Python

| Features      | Javascript    | Python|
| ------------- |:-------------:| -----:|
| Function declaration     | function | def|
|      |      |    |
||     |    |