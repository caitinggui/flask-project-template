#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from flask import Flask, request
from configs import config, log_config
from apps.admin.view import admin
from apps.user.view import user
from apps.home.view import home

logging.config.dictConfig(log_config.log_config)
logger = logging.getLogger('web')

app = Flask(__name__)

logger.debug('register blueprint')
app.register_blueprint(admin, url_prefix='/admin')
# /<user_id> 是动态前缀，如果这里两个blueprint出现动态前缀，
# 那么按顺序分配，也就是说后面的blueprint将不会被使用到
# app.register_blueprint(user, url_prefix='/<user_id>')
app.register_blueprint(home, url_prefix='/<home_id>')

@app.before_request
def addBluepirntTemplate():
    logger.debug("default app templates path: %s", app.jinja_loader.searchpath)
    if request.blueprint:
        bp = app.blueprints[request.blueprint]
        if bp.jinja_loader:
            logger.debug('blueprint templates searchpath: %s', bp.jinja_loader.searchpath)
            if bp.jinja_loader.searchpath[0] in app.jinja_loader.searchpath:
                logger.debug("blueprint templates in app searchpath")
            else:
                new_serach_path = bp.jinja_loader.searchpath + app.jinja_loader.searchpath[-1:]
                logger.debug('searchpath: %s', new_serach_path)
                app.jinja_loader.searchpath = new_serach_path
        else:
            # blueprint没有指定template时，使用app默认template
            logger.debug("blueprint don't have templates")
            app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
    else:
        # 没有blueprint时，使用app默认template
        logger.debug("don't have blueprint")
        app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
    logger.debug("app templates path after before_request: %s", app.jinja_loader.searchpath)

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    logger.info("web start")
    app.run(host="0.0.0.0", port=8182, debug=True)
