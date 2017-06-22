# cofing: utf-8

from flask import Blueprint, render_template, g

# the url_prefix is in app.py
user = Blueprint('user', __name__,
                 template_folder='templates',
                 static_folder='static')


@user.url_value_preprocessor
def getUserID(endpoint, values):
    g.user_id = values.pop('user_id')


@user.route('/')
def index():
    # use g to store information which can be use in template
    g.name = 'user%s' % g.user_id
    return render_template('index.html')
