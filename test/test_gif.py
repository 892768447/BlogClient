#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日
@author: Irony."[讽刺]
@site: irony.iask.in
@email: 892768447@qq.com
@file: test.test_gif.py
@description: 
'''
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


app = QApplication([])

label = QLabel()

move = QMovie("../data/lolita/kiana-3.gif")
label.setMovie(move)
move.start()


label.show()

app.exec_()
