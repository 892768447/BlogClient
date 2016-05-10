#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日
@author: Irony."[讽刺]
@site: http://irony.iask.in
@email: 892768447@qq.com
@file: plugins.left_widget_plugin.py
@description: 左侧控件
'''

from plugins.apis import APIS
from plugins.widgets.left_widget import LeftWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Main(APIS):

    sequence = 3    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = LeftWidget.__name__    # 模块名
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "自定义左侧控件"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.leftwidget = LeftWidget(self.parent)
        # 设置皮肤
        self.setStyleSheet(self.leftwidget, self.name)

    def run(self):
        self.parent.hLayout.addWidget(self.leftwidget, 1)

    def stop(self):
        self.leftui.close()
        self.parent.hLayout.removeWidget(self.leftwidget)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    l = LeftWidget()
    l.show()
    sys.exit(app.exec_())
