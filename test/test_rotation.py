#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月5日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_rotation.py
@description: 
"""
import types

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QStylePainter, \
    QStyle, QStyleOptionButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

def getSyleOptions(self):
    options = QStyleOptionButton()
    options.initFrom(self)
    size = options.rect.size()
    size.transpose()
    options.rect.setSize(size)
    options.features = QStyleOptionButton.DefaultButton
    options.text = self.text()
    options.icon = self.icon()
    options.iconSize = self.iconSize()
    return options

def paintEvent(self, event):
    painter = QStylePainter(self)
    if self.orientation == 'west':
        # 设置中心为旋转的中心
        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(90)
        # 将原点复位
        painter.translate(-self.width() / 2, -self.height() / 2)
        # painter.translate(0, -1 * self.width())
    elif self.orientation == 'east':
        painter.rotate(270)
        # painter.translate(-1 * self.height(), 0)
    else:
        raise TypeError
    painter.drawControl(QStyle.CE_PushButton, self.getSyleOptions())

class Test():

    def __init__(self, clazz):
        self.clazz = clazz

    def test(self, event):
        print(self.clazz, event)

class Widget(QWidget):

    def __init__(self, parent = None):
        super(Widget, self).__init__(parent)
        self.btn = QPushButton("=", self)
        setattr(self.btn, "orientation", "west")
        setattr(self.btn, "getSyleOptions", types.MethodType(getSyleOptions, self.btn))
        setattr(self.btn, "paintEvent", types.MethodType(paintEvent, self.btn))

        # setattr(self.btn, "paintEvent", Test(self.btn).test)

    def enterEvent(self, *args, **kwargs):
        return QWidget.enterEvent(self, *args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        return QWidget.leaveEvent(self, *args, **kwargs)

app = QApplication([])
w = Widget()
w.setStyleSheet("""
QPushButton {
    border: 2px solid red;
    width: 60px;
    height: 60px;
    border-top-left-radius: 30px;
}
""")
w.show()
app.exec_()
