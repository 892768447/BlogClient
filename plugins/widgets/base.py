#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.base.py
@description: 
"""
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyleOption, QStyle, QWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class BaseWidget(object):

    def paintEvent(self, event):
        """由于继承的问题会导致子控件QWidget无法通过QSS设置样式,需要重写该方法"""
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, option, painter, self)
        QWidget.paintEvent(self, event)
        # super(BaseWidget, self).paintEvent(event)