#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.libs.animation.shake.py
@description: 
"""
from PyQt5.QtCore import QTimer


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class Shake(QTimer):

    MaxLimitTimes = 12
    MaxLimitSpace = 5

    def __init__(self, *args, **kwargs):
        super(Shake, self).__init__(*args, **kwargs)
        self._parent = None
        self.m_nPosition = 0
        self.setInterval(40)
        self.timeout.connect(self.slot_timerOut)

    def shake(self, parent):
        self._parent = parent
        self.m_nPosition = 0
        self.m_curPos = parent.pos()
        self.start()

    def slot_timerOut(self):
        if self.m_nPosition == 12:
            self.stop()
            return
        if not self._parent: return
        if self.m_nPosition < self.MaxLimitTimes:
            self.m_nPosition += 1
            mp = self.m_nPosition % 4
            if mp == 1:
                self._parent.move(self.m_curPos.x(), self.m_curPos.y() - self.MaxLimitSpace)
                return
            if mp == 2:
                self._parent.move(self.m_curPos.x() - self.MaxLimitSpace, self.m_curPos.y() - self.MaxLimitSpace)
                return
            if mp == 3:
                self._parent.move(self.m_curPos.x() - self.MaxLimitSpace, self.m_curPos.y())
                return
            if mp == 0:
                self._parent.move(self.m_curPos)
                return
            self.start()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
    app = QApplication([])
    w = QWidget()

    layout = QVBoxLayout(w)

    shake = Shake(w)

    btn = QPushButton("test", w, clicked = lambda: shake.shake(w))

    layout.addWidget(btn)
    w.show()
    app.exec_()
