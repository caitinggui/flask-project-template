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
app.register_blueprint(user, url_prefix='/<user_id>')
app.register_blueprint(home, url_prefix='/')


if __name__ == "__main__":
    logger.info("web start")
    app.run(host="0.0.0.0", port=8182, debug=True)
