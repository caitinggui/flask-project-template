#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config

from flask import Flask
from configs import config, log_config

logger = logging.getLogger('web')

app = Flask(__name__)

logger.debug('register blueprint')
# app.register_blueprint()

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    logger.info("web start")
    app.run(host="0.0.0.0", port=8182, debug=True)
