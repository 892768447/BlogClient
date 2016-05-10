#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: settings.py
@description: 
"""
from PyQt5.QtCore import QSettings, QTextCodec


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class Settings(QSettings):

    def __init__(self, conf = "qt.conf", parent = None):
        super(Settings, self).__init__(conf, QSettings.IniFormat, parent)
        self.setIniCodec(QTextCodec.codecForName("utf-8"))

    def save(self):
        self.sync()

    @property
    def dataDir(self):
        """获取data目录路径"""
        path = self.value("data", None)
        if not path:
            path = "data"
            self.setValue("data", path)
        return path

    @property
    def themeDir(self):
        """获取theme目录"""
        theme = self.value("theme", None)
        if not theme:
            theme = "default"
            self.setValue("theme", theme)
        else: return theme

    @themeDir.setter
    def themeDir(self, theme):
        """设置theme目录"""
        self.setValue("theme", theme)
