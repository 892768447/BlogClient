#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月10日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.loliat_plugin.py
@description: 
"""
from plugins.apis import APIS
from plugins.widgets.lolita import Lolita
from plugins.utils.settings import Settings


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class Main(APIS):

    sequence = 7    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = Lolita.__name__    # 模块名
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "萝莉"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.lolita = Lolita(parent = self.parent)    # 在父窗口的任何位置都可以

    def run(self):
        self.lolita.init(Settings().dataDir)
        # 设置到父窗口的右下角
        pw = self.parent.size().width()
        ph = self.parent.size().height()
        w = self.lolita.width()
        h = self.lolita.height()
        # 设置坐标
        self.lolita.setGeometry(pw - w, ph - h, w, h)
        self.lolita.show()

    def stop(self):
        self.lolita.close()
        self.lolita.exit()
