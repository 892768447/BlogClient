#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月8日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.left_widget.py
@description: 
"""
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from plugins.widgets.left_link_ui import LeftLinkUi
from plugins.widgets.left_ui import LeftUi
from plugins.widgets.base import BaseWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class LeftWidget(QWidget, BaseWidget):

    def __init__(self, parent = None):
        super(LeftWidget, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(LeftUi(self))
        layout.addWidget(LeftLinkUi(self))

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = LeftWidget()
    w.show()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/LeftUi.qss"))
    sys.exit(app.exec_())
