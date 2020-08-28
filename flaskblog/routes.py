
from PIL import Image
from flask import render_template, url_for, flash, redirect, request,abort
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
import feedparser
from flaskblog.feed import parse, get_source, get_articles
from datetime import datetime


url1 = 'http://www.informationweek.com/rss_simple.asp'
url_weather = 'https://weather-broker-cdn.api.bbci.co.uk/en/observation/rss/1850147'

parsed_it = parse(url1)
feed_sourse_it= get_source(parsed_it)
feed_articles_it= get_articles(parsed_it)

parsed_weather = feedparser.parse(url_weather)
#print(parsed_weather['entries'])
# feed_sourse_it= get_source(parsed_it)
# feed_articles_it= get_articles(parsed_it)

# newsfeed  
@app.route('/newsfeed')
def newsfeed():
    return render_template('it-newsfeed.html', articles=feed_articles_it, sourse=feed_sourse_it)


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts, weather=parsed_weather, datetime=datetime)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created, you can log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))  
        else:
            flash('Please, check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(pic):
    random_hash = secrets.token_hex(8)
    _, f_ext = os.path.splitext(pic.filename)
    pic_fn = random_hash + f_ext
    pic_path = os.path.join(app.root_path, 'static/profile_pics', pic_fn)
   
    resize = (125, 125)
    i = Image.open(pic)
    i.thumbnail(resize)

    i.save(pic_path)
    return pic_fn



@app.route('/account',methods=['GET', 'POST'] )
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', 
    form=form,legend='New Post' )


## Create route to update and delete
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
     form=form, legend='Update Post' )


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))

   