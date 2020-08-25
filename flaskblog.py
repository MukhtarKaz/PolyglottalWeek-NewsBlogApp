from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if (__name__) == '__main__':
    app.run(debug=True)
