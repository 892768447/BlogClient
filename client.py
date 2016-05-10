#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月20日
@author: Irony."[讽刺]
@site: http://irony.iask.in
@email: 892768447@qq.com
@file: client.py
@description: 
'''
import os
import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from pluginmanager import PluginManager
from settings import Settings
import traceback


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Client(object):

    def __init__(self):
        self.pluginmanager = PluginManager()
        self.pluginmanager.loadPlugins()

    @classmethod
    def loadFont(cls):
        """加载外部字体"""
        path = os.path.join(Settings().dataDir, "fonts")
        for font in os.listdir(path):
            QFontDatabase.addApplicationFont(os.path.join(path, font))

def start():
    sys.path.append(os.path.abspath("plugins"))
    app = QApplication(sys.argv)
    Client.loadFont()
    Client()
    sys.exit(app.exec_())

if __name__ == "__main__":
    try: start()
    except Exception as e:
        traceback.print_exc(e)