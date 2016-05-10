#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年4月30日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.top_title_plugin.py
@description: 
"""
from plugins.apis import APIS
from plugins.widgets.top_title_ui import TopTitleUi


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Main(APIS):

    sequence = 1    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = TopTitleUi.__name__    # 模块名(相对应的还关联到皮肤加载)
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "自定义标题栏"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.titlebar = TopTitleUi(self.parent)
        self.setStyleSheet(self.titlebar, self.name)

    def run(self):
        self.parent.vLayout.insertWidget(self.parent.vLayout.count() - 1, self.titlebar)

    def stop(self):
        self.titlebar.close()
        self.parent.vLayout.removeWidget(self.titlebar)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    t = TopTitleUi(fontPath = "data/fonts/webdings.ttf")
    # 无边框
    t.setWindowFlags(Qt.FramelessWindowHint)
    t.show()
    sys.exit(app.exec_())
