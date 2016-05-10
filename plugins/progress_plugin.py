#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.progressbar_plugin.py
@description: 
"""
from plugins.apis import APIS
from plugins.widgets.progress_ui import ProgressUi
from PyQt5.QtCore import QTimer


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Main(APIS):

    sequence = 2    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = ProgressUi.__name__    # 模块名
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "自定义标题栏"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.progressui = ProgressUi(self.parent)
        self.progressui.setVisible(False)    # 默认不可见
        self.setStyleSheet(self.progressui, self.name)

        # 测试加载进度
        self.i = 0
        self.progressui.setVisible(True)    # 测试改为可见
        self.timer = QTimer(timeout = self.onTimeout)
        self.timer.start(50)

    def onTimeout(self):
        self.i += 1
        self.progressui.setValue(self.i)
        if self.i > 100:
            self.timer.stop()
            self.progressui.setValue(0)
            self.progressui.setVisible(False)

    def run(self):
        self.parent.vLayout.insertWidget(self.parent.vLayout.count() - 1, self.progressui)

    def stop(self):
        self.timer.stop()
        self.progressui.close()
        self.parent.vLayout.removeWidget(self.progressui)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    t = ProgressUi()
    t.show()
    sys.exit(app.exec_())
