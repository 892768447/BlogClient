#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.progress_ui.py
@description: 
"""
from PyQt5.QtWidgets import QProgressBar


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class ProgressUi(QProgressBar):

    def __init__(self, parent = None):
        super(ProgressUi, self).__init__(parent)
        self.setMaximum(100)
        self.setTextVisible(False)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QTimer
    from plugins import apis
    app = QApplication(sys.argv)
    w = ProgressUi()
    w.show()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/ProgressUi.qss"))
    def test():
        if w.value() == 100: w.setValue(0)
        else: w.setValue(w.value() + 1)
    t = QTimer(timeout = test)
    t.start(10)
    sys.exit(app.exec_())
