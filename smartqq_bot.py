#!/usr/bin/env python
# coding: utf-8

from smartqq import SmartQQ
from smartqq.utils import *
from qq_handler import QQMsgHandler
from qq_handler import Bot
from db import SqliteDB
from config import ConfigManager
from config import Constant
from config import Log

import traceback
import os
import sys
import logging
import time

cm = ConfigManager()
msg_db = SqliteDB(cm.getpath('database'))
qq_msg_handler = QQMsgHandler(msg_db)
smartqq = SmartQQ()

smartqq.bot = Bot()
smartqq.msg_handler = qq_msg_handler
qq_msg_handler.smartqq = smartqq

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)

while True:
    try:
        smartqq.start()
    except (KeyboardInterrupt, SystemExit):
        smartqq.exit_code = 1
    else:
        error(traceback.format_exc())
    finally:
        smartqq.stop()

    if smartqq.exit_code == 0:
        echo('断开连接\n')
    else:
        # kill process
        echo('关闭数据库\n')
        msg_db.close()
        os.system(Constant.LOG_MSG_KILL_PROCESS % os.getpid())
