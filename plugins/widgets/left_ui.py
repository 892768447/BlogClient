#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.left_ui.py
@description: 
"""
import os
import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QImage, QPainter
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from plugins.libs.animation.rotation import ButtonRotationRnimation
from plugins.uifiles.left_ui import Ui_BlogFormLeft
from plugins.utils.settings import Settings
from plugins.widgets.base import BaseWidget
from plugins.widgets.signal import Signal


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class LeftUi(QWidget, Ui_BlogFormLeft, BaseWidget):

    def __init__(self, parent = None):
        super(LeftUi, self).__init__(parent)
        self.setupUi(self)
        # 对应字体库里面的搜索图标
        self.blog_search_button.setText("\uf002")
        # 设置间隔
        self.blog_menu_list.setSpacing(10)
        # 设置动画效果
        ButtonRotationRnimation(self.blog_head_label)

        # 绑定登录成功后设置头像的信号
        Signal().Login_Success.connect(self.setHead)

        # 测试数据
        for menu in ("PyQt", "Python", "Android", "About", "Message"):
            item = QListWidgetItem(menu, self.blog_menu_list)
            item.setTextAlignment(Qt.AlignHCenter)

    def setHead(self, qq, name, head):
        """设置头像"""
        self.blog_head_label.setToolTip(name)
        pixmap = QPixmap()
        pixmap.loadFromData(head)
        path = os.path.join(Settings().dataDir, "images", "head.png")    # 头像保存路径
        pixmap.save(path, format = "png")
        if os.path.exists(path):    # 如果存在
            # 匹配出样式
            qss = re.findall("#blog_head_label(.*?)}", self.styleSheet(), re.S)
            if qss:
                # 修改头像的样式
                qss = "#blog_head_label" + re.sub("url\((.*?)\)", "url(%s/images/head.png)" % Settings().dataDir, qss[0]) + "}"
                self.blog_head_label.setStyleSheet(qss)
                return
        # 不存在则直接处理
        # ---变成圆形---
        pixmap = self.getRoundPixmap(pixmap)
        #-------------
        # 调整大小
        pixmap = pixmap.scaled(self.blog_head_label.size())
        self.blog_head_label.setIcon(QIcon(pixmap))
        self.blog_head_label.setIconSize(self.blog_head_label.size())

    def getRoundPixmap(self, pixmap):
        """pixmap原图"""
        resultImage = QImage(pixmap.size(), QImage.Format_ARGB32_Premultiplied)
        head_mask = QPixmap(os.path.join(Settings().dataDir, "images", "mask.png"))
        painter = QPainter(resultImage)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(resultImage.rect(), Qt.transparent)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawPixmap(0, 0, head_mask)
        painter.setCompositionMode(QPainter.CompositionMode_SourceOut)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationOver)
        painter.end()
        result = QPixmap.fromImage(resultImage)
        del resultImage, head_mask
        return result

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = LeftUi()
    w.show()
    sys.exit(app.exec_())
