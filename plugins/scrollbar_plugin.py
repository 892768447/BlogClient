#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.scrollbar_plugin.py
@description: 
"""
from plugins.apis import APIS
from plugins.widgets.scrollbar_ui import ScrollBarUi


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class Main(APIS):

    sequence = 6    # 插件加载顺序(重要,顺序不同可能导致界面混乱)
    name = ScrollBarUi.__name__    # 模块名
    author = __Author__    # 作者
    version = __Version__    # 版本
    description = "自定义滚动条"    # 描述

    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.scrollbarui = ScrollBarUi(self.parent)
        self.setStyleSheet(self.scrollbarui, self.name)

    def run(self):
        self.parent.hLayout.addWidget(self.scrollbarui, 1)

    def stop(self):
        self.scrollbarui.close()
        self.parent.hLayout.removeWidget(self.scrollbarui)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    t = ScrollBarUi()
    t.show()
    sys.exit(app.exec_())
