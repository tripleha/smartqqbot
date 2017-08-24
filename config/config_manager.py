#!/usr/bin/env python
# coding: utf-8

from constant import Constant
import ConfigParser
import os


class ConfigManager(object):

    def __init__(self):
        self.config = Constant.QQ_CONFIG_FILE
        self.cp = ConfigParser.ConfigParser()
        self.cp.read(self.config)

        data_dir = self.get('setting', 'prefix')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def get(self, section, option):
        return self.cp.get(section, option)

    def set(self, section, option, value):
        self.cp.set(section, option, value)
        self.cp.write(open(self.config, 'w'))

    def getpath(self, dir):
        prefix = self.get('setting', 'prefix')
        r_dir = prefix + self.get('setting', dir)
        return r_dir
