#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月5日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_font.py
@description: 
"""
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QPushButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

app = QApplication([])

QFontDatabase.addApplicationFont("../data/fonts/webdings.ttf")
QFontDatabase.addApplicationFont("../data/fonts/fontawesome-webfont.ttf")

btn = QPushButton()
btn.setObjectName("blog_up_button")
btn.show()
# 圆形进度 \uf110
# 搜索 \uf002

app.setStyleSheet("""
#blog_up_button {
    qproperty-text: "\uf002";
    font-family: "FontAwesome";
}
""")

app.exec_()
