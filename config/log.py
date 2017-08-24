#!/usr/bin/env python
# coding: utf-8


from constant import Constant
from config import ConfigManager

import logging
import logging.config

cm = ConfigManager()

logging.config.fileConfig(Constant.QQ_CONFIG_FILE)
Log = logging.getLogger(Constant.LOGGING_LOGGER_NAME)
