#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月9日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.right_item.py
@description: 
"""
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, \
    QVBoxLayout

from plugins.widgets.base import BaseWidget
from plugins.apis import APIS


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class ItemHeader(QLabel):
    """顶部"""

    def __init__(self, text, parent = None):
        super(ItemHeader, self).__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        APIS.setStyleSheet(self, ItemHeader.__name__)

    def sizeHint(self):
        return QSize(220, 50)

class ItemLabel(QPushButton):
    """分类标签"""

    def __init__(self, text, parent = None):
        super(ItemLabel, self).__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setFlat(True)
        self.adjustSize()    # 自适应文字的大小

    def sizeHint(self):
        return QSize(80, 28)

class ItemHead(QPushButton):
    """头像"""

    def __init__(self, user, parent = None):
        super(ItemHead, self).__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setFlat(True)
        self.qq = user.get("qq", "")
        self.setToolTip(user.get("nick", ""))
        head = user.get("head", "")
        if head:
            self.setIcon(QIcon(head))
            self.setIconSize(QSize(50, 50))

    def sizeHint(self):
        return QSize(50, 50)

class ItemVContent(QWidget, BaseWidget):
    """下面的网格布局(每行三个)"""

    def __init__(self, parent = None):
        super(ItemVContent, self).__init__(parent)
        self.layout = QGridLayout(self)
        APIS.setStyleSheet(self, ItemVContent.__name__)

    def addItem(self, item):
        # 列(最大为3)
        col = self.layout.count() % 3
        # 行
        """
        1--0/3=0   -- 0
        2--1/3=0.3 -- 0
        3--2/3=0.6 -- 0
        4--3/3=1   -- 1
        5--4/3=1.3 -- 1
        6--5/3=1.6 -- 1
        """
        row = int(str(self.layout.count() / 3)[0])
        self.layout.addWidget(item, row, col)

class ItemContent(QWidget):

    def __init__(self, parent = None):
        super(ItemContent, self).__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 20)
        layout.setSpacing(0)
        self.content = ItemVContent(self)
        layout.addWidget(self.content)

    def addItem(self, item):
        self.content.addItem(item)
