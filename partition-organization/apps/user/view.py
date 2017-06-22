# coding: utf-8

from flask import Blueprint, render_template, g

# the url_prefix is in app.py
user = Blueprint('user', __name__,
                 template_folder='templates',
                 static_folder='static')


@user.url_value_preprocessor
def getUserID(endpoint, values):
    """取出url中的user_id, 同时避免route书写冗余"""
    g.user_id = values.pop('user_id')


@user.url_defaults
def add_project(endpoint, values):
    """将user_id添加回values中, 避免url_for失效"""
    if 'user_id' in values or not g.project:
        return
    values['project_name'] = g.project.name


@user.route('/')
def index():
    # use g to store information which can be use in template
    g.name = 'user%s' % g.user_id
    return render_template('user_index.html')
