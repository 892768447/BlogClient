#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.signal.py
@description: 
"""
from PyQt5.QtCore import pyqtSignal, QObject, QByteArray
from PyQt5.QtWidgets import QScrollBar

from plugins.utils.singleton import singleton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

@singleton
class Signal(QObject):

    Set_VScrollBar = pyqtSignal(QScrollBar)    # 设置中间的QListWidget的竖着的滚动条信号槽

    VScrollBar_ValueChanged = pyqtSignal(int)    # 在主界面滚动时发送滚动的值

    Login_Success = pyqtSignal(str, str, QByteArray)    # 登陆成功(qq,昵称,头像)
