#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.scrollbar_ui.py
@description: 
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollBar

from plugins.widgets.signal import Signal


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class ScrollBarUi(QScrollBar):

    def __init__(self, parent = None):
        super(ScrollBarUi, self).__init__(Qt.Vertical, parent)

        # 发送信号(通过信号槽把自定义的滚动条设置到中间的QListWidget上)
        Signal().Set_VScrollBar.emit(self)
        # 连接由父窗口发送过来的滚动值
        Signal().VScrollBar_ValueChanged.connect(self._setValue)

    def _setValue(self, value):
        # value * 3 目前不清楚这个3是怎么得到的,测试的时候发现是3
        self.setValue(self.value() + value * -3)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = ScrollBarUi()
    w.show()
    dataDir = "../../data"
    w.setStyleSheet(apis.APIS.readFile(dataDir + "/themes/default/ScrollBarUi.qss").replace("%DATA_DIR%", dataDir))
    print(w.styleSheet())
    sys.exit(app.exec_())
