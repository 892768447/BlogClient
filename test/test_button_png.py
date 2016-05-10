#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_button_png.py
@description: 
"""
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QSize

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

app = QApplication([])

btn = QPushButton()
btn.resize(300, 300)
btn.show()

btn.setIcon(QIcon("../data/lolita/kiana-1.png"))
btn.setIconSize(QSize(300, 300))

app.exec_()
