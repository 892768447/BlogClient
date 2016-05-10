#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.top_title_ui.py
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from plugins.uifiles.top_title_ui import Ui_BlogFormTitleBar
from plugins.widgets.base import BaseWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class TopTitleUi(QWidget, Ui_BlogFormTitleBar, BaseWidget):

    def __init__(self, parent = None):
        super(TopTitleUi, self).__init__(parent)
        self.parent = parent    # 父控件
        self.setupUi(self)

        self.blog_min_button.clicked.connect(
            self.parent.showMinimized if self.parent else \
            self.showMinimized
        )    # 控制最小化

        self.blog_max_button.clicked.connect(self.onMaxed)

        self.blog_close_button.clicked.connect(
            self.parent.close if self.parent else \
            self.close
        )    # 控制关闭

    def mouseDoubleClickEvent(self, event):
        """双击"""
        if event.buttons() == Qt.LeftButton:
            self.onMaxed()
        super(TopTitleUi, self).mouseDoubleClickEvent(event)

    def onMaxed(self):
        # 最大化和还原按钮
        if not self.parent:
            if self.isMaximized():
                self.blog_max_button.setText("1")
                self.showNormal()    # 还原
            else:
                self.blog_max_button.setText("2")
                self.showMaximized()    # 最大化
        else:
            if self.parent.isMaximized():    # 已经最大化
                self.blog_max_button.setText("1")
                self.parent.showNormal()    # 显示普通
            else:
                self.blog_max_button.setText("2")
                self.parent.showMaximized()    # 最大化

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = TopTitleUi()
    # 无边框
    w.setWindowFlags(Qt.FramelessWindowHint)
    w.show()
    dataDir = "../../data"
    w.setStyleSheet(apis.APIS.readFile(dataDir + "/themes/default/TopTitleUi.qss").replace("%DATA_DIR%", dataDir))
    sys.exit(app.exec_())
