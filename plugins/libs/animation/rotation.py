#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月5日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.libs.animation.rotation.py
@description: 
"""
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QStyleOptionButton, QStylePainter, QStyle, \
    QStyleOption


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class RotationRnimation(object):
    """旋转动画(由于采用ui设计的界面所以没法自定义控件,只能通过替换内部函数来实现)"""

    def __init__(self, clazz):
        self.clazz = clazz
        self.rotate = 0    # 旋转角度
        self.step = 45    # 度数增加步长
        self.direction = None    # clockwise 顺时针 anticlockwise 逆时针
        self.timer = QTimer(clazz, timeout = self.update)    # 刷新界面

        setattr(clazz, "getSyleOptions", self.getSyleOptions)
        # 修改控件的paintEvent事件
        setattr(clazz, "paintEvent", self.paintEvent)
        setattr(clazz, "enterEvent", self.enterEvent)
        setattr(clazz, "leaveEvent", self.leaveEvent)

    def __del__(self):
        self.stop()

    def stop(self):
        self.timer.stop()

    def getSyleOptions(self):
        options = QStyleOption()
        options.initFrom(self.clazz)
        size = options.rect.size()
        size.transpose()
        options.rect.setSize(size)
        options.features = QStyleOption.SO_Default
        return options

    def getControlElement(self):
        return QStyle.CE_CustomBase

    def update(self):
        if self.direction == "clockwise":    # 顺时针
            # 0 45 90 135 180 225 270 315 360
            if self.rotate == -360: self.rotate = 45
            else: self.rotate += self.step
            if self.rotate > 360:    # 旋转一周后停止
                self.rotate = 360
                self.direction = None
                self.timer.stop()    # 停止计时器
            else:
                # print("顺时针: ", self.rotate)
                # 调用控件的update函数刷新界面
                self.clazz.update()
        elif self.direction == "anticlockwise":    # 逆时针
            # 360 -45 -90 -135 -180 -225 -270 -315 -360
            if self.rotate == 360: self.rotate = -45
            else: self.rotate -= self.step
            if self.rotate < -360:
                self.rotate = -360
                self.direction = None
                self.timer.stop()
            else:
                # print("逆时针: ", self.rotate)
                # 调用控件的update函数刷新界面
                self.clazz.update()

    def paintEvent(self, event):
        """绘制事件"""
        painter = QStylePainter(self.clazz)
        width = self.clazz.width() / 2
        height = self.clazz.height() / 2
        if self.direction in ("clockwise", "anticlockwise"):
            painter.translate(width, height)    # 设置中心为旋转的中心
            painter.rotate(self.rotate)
            painter.translate(-width, -height)    # 将原点复位
        painter.drawControl(self.getControlElement(), self.getSyleOptions())

    def enterEvent(self, event):
        """鼠标进入事件"""
        self.timer.stop()
        self.direction = "clockwise"    # 顺时针旋转
        self.timer.start(20)

    def leaveEvent(self, event):
        """鼠标离开事件"""
        self.timer.stop()
        self.direction = "anticlockwise"    # 逆时针旋转
        self.timer.start(20)

class ButtonRotationRnimation(RotationRnimation):

    def getControlElement(self):
        return QStyle.CE_PushButton

    def getSyleOptions(self):
        """QPushButton的Options"""
        options = QStyleOptionButton()
        options.initFrom(self.clazz)
        size = options.rect.size()
        size.transpose()
        options.rect.setSize(size)
        options.features = QStyleOptionButton.DefaultButton
        options.text = self.clazz.text()
        options.icon = self.clazz.icon()
        options.iconSize = self.clazz.iconSize()
        return options

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
    app = QApplication([])
    app.setStyleSheet("""
QPushButton {
    min-width: 100px;
    max-width: 100px;
    min-height: 100px;
    max-height: 100px;
    border-radius: 50px;
    background-color: green;
}
QLabel {
    min-width: 100px;
    max-width: 100px;
    min-height: 100px;
    max-height: 100px;
    border-radius: 50px;
    background-color: red;
    border-radius: 50px;
}
""")
    w = QWidget()

    layout = QVBoxLayout(w)

    btn = QPushButton("--------", w)
    ButtonRotationRnimation(btn)
    layout.addWidget(btn)

    label = QLabel("aaaa", w)
    layout.addWidget(label)

    w.show()
    app.exec_()
