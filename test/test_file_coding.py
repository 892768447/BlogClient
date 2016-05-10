#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月5日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_file_coding.py
@description: 
"""
from PyQt5.QtCore import QFile, QIODevice, QTextStream

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

def test1():
    file = QFile("utf8.txt")
    file.open(QIODevice.ReadOnly)
    fin = QTextStream(file)
    fin.setCodec("UTF-8")
    print(fin.readAll())
    file.close()

def test2():
    file = QFile("ansi.txt")
    file.open(QIODevice.ReadOnly | QIODevice.Text)
    fin = QTextStream(file)
    fin.setCodec("UTF-8")
    print(fin.readAll())
    file.close()

def test3():
    file = QFile("TopTitleUi.qss")
    file.open(QIODevice.ReadOnly | QIODevice.Text)
    fin = QTextStream(file)
    fin.setCodec("UTF-8")
    print(fin.readAll())
    file.close()

test1()
test2()
test3()