#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: widgets.clientui.py
@description: 
"""

from plugins.apis import APIS
from plugins.widgets.client_ui import ClientWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class Main(APIS):

    sequence = 0    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = ClientWidget.__name__    # 模块名(相对应的还关联到皮肤加载)
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "主窗口"    # 描述

    def __init__(self, pluginManager):
        self.clientwidget = ClientWidget(pluginManager = pluginManager)    # 不需要parent了
        self.parent = self.clientwidget
        self.setStyleSheet(self.clientwidget, self.name)

    def run(self):
        self.clientwidget.show()

    def stop(self):
        self.clientwidget.close()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    t = ClientWidget()
    t.show()
    sys.exit(app.exec_())
