#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.center_widget_plugin.py
@description: 中间控件
"""
from plugins.apis import APIS
from plugins.widgets.center_ui import CenterUi


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class Main(APIS):

    sequence = 4    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = CenterUi.__name__    # 模块名
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "自定义右侧分栏"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.centerui = CenterUi(self.parent)
        # 设置皮肤
        self.setStyleSheet(self.centerui, self.name)
        # listwidget bug?
        self.setStyleSheet(self.centerui.blog_list_widget, self.name)

    def run(self):
        self.parent.hLayout.addWidget(self.centerui, 2)

    def stop(self):
        self.centerui.close()
        self.parent.hLayout.removeWidget(self.centerui)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    t = CenterUi()
    t.show()
    sys.exit(app.exec_())

