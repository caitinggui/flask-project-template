# cofing: utf-8

from flask import Blueprint, render_template, g

# the url_prefix is in app.py
admin = Blueprint('admin', __name__,
                  template_folder='templates',
                  static_folder='static')


@admin.route('/')
def index():
    # use g to store information which can be use in template
    g.name = 'ctg'
    return render_template('index.html')
