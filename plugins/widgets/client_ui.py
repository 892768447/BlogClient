#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: widgets.clientui.py
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

from plugins.uifiles.client_ui import Ui_BlogFormClient
from plugins.widgets.signal import Signal


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class ClientWidget(QWidget, Ui_BlogFormClient):

    def __init__(self, parent = None, pluginManager = None):
        super(ClientWidget, self).__init__(parent)
        self.pluginManager = pluginManager
        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        # 控制是否可以移动
        self._canMove = False
        # 根据屏幕设置窗口大小
        self.resize(QApplication.desktop().screenGeometry().size() * 5 / 6)

    def closeEvent(self, event):
        """窗口关闭事件"""
        if self.pluginManager:
            self.pluginManager.clear()    # 停止所有插件
        super(ClientWidget, self).closeEvent(event)

    def mousePressEvent(self, event):
        """鼠标按下(主要有titlebar来实现)"""
        super(ClientWidget, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._canMove = True
            # 记录坐标
            self.mpos = event.globalPos() - self.pos()
            if self.isMaximized(): self._canMove = False

    def mouseMoveEvent(self, event):
        """鼠标拖动(主要有titlebar来实现)"""
        super(ClientWidget, self).mouseMoveEvent(event)
        if event.buttons() == Qt.LeftButton and self._canMove and hasattr(self, "mpos"):
            self.move(event.globalPos() - self.mpos)

    def mouseReleaseEvent(self, event):
        """鼠标释放开"""
        super(ClientWidget, self).mouseReleaseEvent(event)
        self._canMove = False

    def mouseDoubleClickEvent(self, event):
        """双击"""
        if event.buttons() == Qt.LeftButton:
            # 传递到子控件上面
            super(ClientWidget, self).mouseDoubleClickEvent(event)
        else:
            event.ignore()

    def wheelEvent(self, event):
        """
        #鼠标转轮滑动一圈是360度,鼠标滚轮转动一圈是24步,
        #计算后就是15度一步,而鼠标转轮滑动的角度对应于窗口界面单位尺度的8倍,
        #也就是滚动一度,鼠标滚轮在界面上滑动的距离（比如滚动条等）是8个unit单位,
        #在这种情况下,delta的返回值是120（8*15）的倍数
        #delta()已经被弃用了,QT5中用的是angleDelta(),计算的时候取angleDelta().y()值
        #eg: ui->listWidget->horizontalScrollBar()->setValue(ui->listWidget->horizontalScrollBar()->value() + numberSteps);
        """
        Signal().VScrollBar_ValueChanged.emit(int(event.angleDelta().y() / 8 / 15))
        super(ClientWidget, self).wheelEvent(event)

if __name__ == "__main__":
    import sys
    from plugins.widgets.left_ui import LeftUi
    from plugins import apis
    app = QApplication(sys.argv)
    w = ClientWidget()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/ClientWidget.qss"))


    l = LeftUi(w)
    l.setStyleSheet(apis.APIS.readFile("../../data/themes/default/LeftUi.qss"))

    w.hLayout.addWidget(l)

    w.show()

    sys.exit(app.exec_())
