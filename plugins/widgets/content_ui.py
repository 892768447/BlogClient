#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月10日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.content.py
@description: 
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from plugins.apis import APIS
from plugins.uifiles.center_content_ui import Ui_BlogFormCenterContent
from plugins.widgets.base import BaseWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class ContentUiItem(QWidget, Ui_BlogFormCenterContent, BaseWidget):

    def __init__(self, parent = None):
        super(ContentUiItem, self).__init__(parent)
        self.setupUi(self)
        # 默认置顶不显示
        self.blog_stick_label.setVisible(False)

        self.addItem(
            {
                "stick":False, "title":"测试标题",
                "detail":"测试详情", "time":"2016-04-07",
                "classify":"PyQt", "comment":"0评论", "views":"5查看",
            }
        )

    def addItem(self, data):
        # 置顶
        if data.get("stick"): self.blog_stick_label.setVisible(True)
        self.blog_title_button.setText(data.get("title"))
        self.blog_content_text.setText(data.get("detail"))
        self.blog_time_label.setText(data.get("time"))
        self.blog_classify_button.setText(data.get("classify"))
        self.blog_comment_button.setText(data.get("comment"))
        self.blog_views_label.setText(data.get("views"))

    def addItems(self, datas):
        for data in datas:
            self.addItem(data)

class ContentUi(QWidget):

    def __init__(self, parent = None):
        super(ContentUi, self).__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 35)
        layout.setSpacing(0)
        self.item = ContentUiItem(self)
        layout.addWidget(self.item)
        APIS.setStyleSheet(self, ContentUi.__name__)

    def sizeHint(self):    # 默认大小
        return QSize(400, 335)

    def addItem(self, data):
        self.item.addItem(data)

    def addItems(self, datas):
        self.item.addItems(datas)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = ContentUi()
    w.show()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/ContentUi.qss"))
    sys.exit(app.exec_())
