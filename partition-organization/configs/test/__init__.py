# -*- coding: utf-8 -*-

import json
import os
current_path = os.path.dirname(os.path.abspath(__file__))
# configs = {}

# with open("%s/config.json" % (current_path)) as f:
#     configs = json.loads(f.read())
with open(os.path.join(current_path, 'config.json')) as f:
    configs = json.load(f)

with open(os.path.join(current_path, 'log_config.json')) as f:
    log_config = json.load(f)
__all__ = [configs, log_config]
