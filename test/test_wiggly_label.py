#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月10日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_wiggly_label.py
@description: 
"""
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QPalette, QFontMetrics, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QLabel


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class WigglyLabel(object):

    def __init__(self, clazz):
        self.clazz = clazz
        # clazz.setBackgroundRole(QPalette.Midlight)
        # clazz.setAutoFillBackground(True)

        setattr(clazz, "paintEvent", self.paintEvent)
        setattr(clazz, "timerEvent", self.timerEvent)

#         newFont = self.clazz.font()
#         newFont.setPointSize(newFont.pointSize() + 20)
#         self.clazz.setFont(newFont)

        self.timer = QBasicTimer()

        self.step = 0;
        self.timer.start(60, self.clazz)

    def __del__(self):
        self.timer.stop()

    def getText(self):
        return self.clazz.text()

    def paintEvent(self, event):
        # 上下跳动
        # sineTable = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)

        metrics = QFontMetrics(self.clazz.font())
        x = (self.clazz.width() - metrics.width(self.getText())) / 2
        y = (self.clazz.height() + metrics.ascent() - metrics.descent()) / 2
        color = QColor()

        painter = QPainter(self.clazz)

        for i, ch in enumerate(self.getText()):
            index = (self.step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.setPen(color)
            # 上下跳动
            # painter.drawText(x, y - ((sineTable[index] * metrics.height()) / 400), ch)
            painter.drawText(x, y , ch)
            x += metrics.width(ch)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.step += 1
            self.clazz.update()
        else:
            super(WigglyLabel, self).timerEvent(event)

app = QApplication([])
label = QLabel("欢迎访问")
label.setStyleSheet("font-size: 12pt;")
label.show()
print(label.fontMetrics().height())
WigglyLabel(label)
app.exec_()
