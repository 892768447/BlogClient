#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_style.py
@description: 
"""
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, \
    QStyleOption, QStyle


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

Style = """
FatherWidget {
    background-color: green;
}
ChildWidget {
    background-color: red;
}
#Btn {
    background-color: yellow;
}
"""

class ChildWidget(QWidget):

    def __init__(self, parent = None):
        super(ChildWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(QPushButton("ChildWidget", self, objectName = "Btn"))

    def paintEvent(self, event):
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, option, painter, self)
        super(ChildWidget, self).paintEvent(event)

class FatherWidget(QWidget):

    def __init__(self, parent = None):
        super(FatherWidget, self).__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(ChildWidget(self))
        layout.addWidget(QPushButton("FatherWidget", self))

app = QApplication([])
ui = FatherWidget()
ui.setStyleSheet(Style)
ui.show()
app.exec_()
