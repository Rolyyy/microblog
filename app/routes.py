from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Roly'}
    posts = [
        {
            'author' : {'username': 'Hans'},
            'body' : 'Beautiful day in Mont Blanc!'
        },
        {
            'author' : {'username' : 'Dutch'},
            'body' : "Django Unchained was great"
        },
        {
            'author' : {'username' : 'V'},
            'body' : "Hey Johnny"
        },
        {
            'author' : {'username' : 'John'},
            'body' : "Howdy partner"
        }



    ]


    return render_template('index.html', title='Home', user=user, posts=posts)