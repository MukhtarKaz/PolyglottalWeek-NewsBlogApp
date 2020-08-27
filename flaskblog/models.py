from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,  nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# class Source(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text, nullable=False)
#     subtitle = db.Column(db.Text, nullable=False)
#     link = db.Column(db.Text, nullable=False)
#     feed = db.Column(db.Text, nullable=False)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text, nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     link = db.Column(db.Text, nullable=False)
#     guid = db.Column(db.String(255), nullable=False)
#     unread = db.Column(db.Boolean, default=True, nullable=False)
#     source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
#     source = db.relationship('Source', db.backref('articles', lazy=True))
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#     date_published = db.Column(db.DateTime)
#     __table_args__=(
#         db.UniqueConstraint('source_id', 'guid', name='uc_source_guid')
#     )