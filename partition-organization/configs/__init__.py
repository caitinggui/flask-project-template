# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger('web')

try:
    isTest = os.environ["TEST"]
except Exception as ex:
    isTest = "online"

if isTest == "online":
    from online import configs, log_config
else:
    from test import configs, log_config


__all__ = [configs, log_config]
