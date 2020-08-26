
from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app


posts = [
    {
        'author': 'Mukhtar Otarbayev',
        'title': 'First Post',
        'content': "WBD247 - Has the Bitcoin Bull Woken? With Anthony Pompliano",
        'date_posted': 'May 23, 2020'
    },
    {
        'author': 'Adam Doe',
        'title': 'Second Post',
        'content': "New content",
        'date_posted': 'May 25, 2020'
    }
]


@ app.route('/')
@ app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@ app.route('/about')
def about():
    return render_template('about.html', title='About')


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@com.com' and form.password.data == 'pass':
            flash('You logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please, check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
