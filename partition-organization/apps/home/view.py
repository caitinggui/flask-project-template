# cofing: utf-8

from flask import Blueprint, render_template

# the url_prefix is in app.py
home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


@home.route('/')
def index():
    return render_template('home_index.html')
