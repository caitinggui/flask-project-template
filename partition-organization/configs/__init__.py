# -*- coding: utf-8 -*-

import os
import logging

logger = logging.getLogger('web')

try:
    isTest = os.environ["TEST"]
except Exception as ex:
    logger.warn("os.environ don't have 'TEST'")
    isTest = "test"

if isTest == "online":
    logger.info('Use online config')
    from online import config, log_config
else:
    logger.info('Use test config')
    from test import config, log_config


__all__ = [config, log_config]
