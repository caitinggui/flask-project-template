# cofing: utf-8

from flask import Blueprint, render_template, g

# the url_prefix is in app.py
home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


@home.url_value_preprocessor
def getUserID(endpoint, values):
    g.user_id = values.pop('home_id')


@home.route('/')
def index():
    # use g to store information which can be use in template
    g.name = 'user%shome' % g.user_id
    return render_template('index.html')
