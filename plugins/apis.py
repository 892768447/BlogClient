#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月5日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.apis.py
@description: 
"""
import os

from PyQt5.QtCore import QFile, QIODevice, QTextStream

from plugins.utils.settings import Settings


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class APIS(object):
    """注意模块名和类名不能修改"""

    def __init__(self, parent = None):
        self.parent = parent

    @classmethod
    def setStyleSheet(self, obj, fileName):
        try: obj.setStyleSheet(self.loadTheme(fileName))
        except: pass

    @classmethod
    def readFile(self, path, coding = "UTF-8"):
        """读取文件"""
        file = QFile(path)
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        fin = QTextStream(file)
        fin.setCodec(coding)
        data = fin.readAll()
        file.close()
        return data

    @classmethod
    def loadTheme(self, fileName, settings = None):
        """加载主题"""
        if not settings: settings = Settings()
        dataDir = settings.dataDir
        themeDir = settings.themeDir
        settings.save()
        try:
            style = self.readFile(os.path.join(dataDir,
                "themes", themeDir,
                fileName + ".qss")
                ).replace("%DATA_DIR%", dataDir)
        except Exception as e:
            print(e)
            style = ""
        return style
