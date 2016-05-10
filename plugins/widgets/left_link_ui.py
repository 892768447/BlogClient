#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.left_link_ui.py
@description: 
"""
from PyQt5.QtWidgets import QWidget

from plugins.apis import APIS
from plugins.libs.animation.rotation import ButtonRotationRnimation
from plugins.uifiles.left_link_ui import Ui_BlogFormLeftLink
from plugins.widgets.base import BaseWidget
from plugins.widgets.login import LoginWindow
from plugins.widgets.signal import Signal


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = 1.0

class LeftLinkUi(QWidget, Ui_BlogFormLeftLink, BaseWidget):

    def __init__(self, parent = None):
        super(LeftLinkUi, self).__init__(parent)
        self.setupUi(self)
        # 对应字体FontAwesome文件里面的向上符号
        self.blog_up_button.setText("\uf106")
        # 登录按钮事件
        self.blog_login_button.clicked.connect(self.onLogin)
        # 设置动画效果
        ButtonRotationRnimation(self.blog_qq_button)
        ButtonRotationRnimation(self.blog_group_button)
        ButtonRotationRnimation(self.blog_weixin_button)
        ButtonRotationRnimation(self.blog_login_button)

    def onLogin(self):
        if not hasattr(self, "loginWindow"):
            self.loginWindow = LoginWindow()
        APIS.setStyleSheet(self.loginWindow, LoginWindow.__name__)    # 设置登录窗口的进度条样式
        self.loginWindow.FINISHED.connect(Signal().Login_Success.emit)
        self.loginWindow.show()
        self.loginWindow.login()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = LeftLinkUi()
    w.show()
    sys.exit(app.exec_())
