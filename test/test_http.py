#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月2日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_http.py
@description: 
"""
import sys, os

from PyQt5.QtNetwork import QNetworkReply
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTextBrowser

from plugins.utils.httputils import Http


sys.path.append(os.path.abspath("../"))


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class Window(QWidget):

    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.result = QTextBrowser(self)
        layout.addWidget(QPushButton("test", self, clicked = self.onTest))
        layout.addWidget(self.result)

    def onTest(self):
        reply = Http().get("http://www.baidu.com")
        reply.finished.connect(lambda: self.replyFinished(reply))

    def replyFinished(self, reply):
        if reply.error() != QNetworkReply.NoError: return
        print(reply.readAll().data().decode())
        reply.deleteLater()

app = QApplication([])

w = Window()
w.show()

app.exec_()
