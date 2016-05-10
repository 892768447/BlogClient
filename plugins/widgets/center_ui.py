#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.center_ui.py
@description: 
"""
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from plugins.libs.animation.wiggly import WigglyLabel
from plugins.uifiles.center_ui import Ui_BlogFormCenter
from plugins.widgets.base import BaseWidget
from plugins.widgets.content_ui import ContentUi
from plugins.widgets.signal import Signal
from PyQt5.QtCore import QSize


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class CenterUi(QWidget, Ui_BlogFormCenter, BaseWidget):

    def __init__(self, parent = None):
        super(CenterUi, self).__init__(parent)
        self.setupUi(self)
        # 连接
        Signal().Set_VScrollBar.connect(self.blog_list_widget.setVerticalScrollBar)

        # 底部加载进度条(默认先不显示)
        self.blog_progress_label.setVisible(False)

        # 公告文字(彩色)
        self.blog_notice_content_label.setText("欢 迎 访 问 博 客 !")
        WigglyLabel(self.blog_notice_content_label)

        for i in range(20):    # @UnusedVariable
            item = QListWidgetItem(self.blog_list_widget)
            contentui = ContentUi(self)    # 调整大小
            item.setSizeHint(contentui.size())
            # 添加自定义控件
            self.blog_list_widget.setItemWidget(item, contentui)

    def resizeEvent(self, event):
        """当大小改变时"""
        for i in range(self.blog_list_widget.count()):
            item = self.blog_list_widget.item(i)    # 遍历item
            item.setSizeHint(QSize(
                self.blog_list_widget.size().width(),    # 列表的宽度
                self.blog_list_widget.itemWidget(item).sizeHint().height()    # 控件原来的高度
            ))
        return super(CenterUi, self).resizeEvent(event)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = CenterUi()
    w.show()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/CenterUi.qss"))
    sys.exit(app.exec_())
