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
