#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年4月29日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: widgets.login.py
@description: 登录窗口
qq头像地址
http://q2.qlogo.cn/headimg_dl?bs=qq&dst_uin=892768447&spec=100

获取头像地址和昵称
http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins=892768447
http://r.pengyou.com/fcg-bin/cgi_get_portrait.fcg?uins=892768447
(portraitCallBack({"892768447":["http://qlogo4.store.qq.com/qzone/892768447/892768447/100",11767,-1,0,0,0,"Irony."[讽刺]",0]}))

头像地址
http://qlogo4.store.qq.com/qzone/892768447/892768447/100?1433299084
登录地址
http://ui.ptlogin2.qq.com/cgi-bin/login?qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=636014201&target=self&s_url=http%3A//www.qq.com/qq2012/loginSuccess.htm
"""
import re

from PyQt5.QtCore import QUrl, pyqtSlot, QByteArray, Qt, pyqtSignal    # , QEventLoop
from PyQt5.QtGui import QPixmap
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWidgets import QMenu, QWidget, QVBoxLayout

from plugins.widgets.progress_ui import ProgressUi
from plugins.libs.animation.shake import Shake


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

PATTERN = 'portraitCallBack\(\{"(.*)":\[\"(.*)",(.*),(.*),(.*),(.*),(.*),"(.*)",0\]\}\)'
INFO_URL = "http://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins={qq}"
HEAD_URL = "http://q2.qlogo.cn/headimg_dl?bs=qq&dst_uin={qq}&spec=140"
LOGIN_URL = "http://ui.ptlogin2.qq.com/cgi-bin/login?qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=636014201&target=self&s_url=http%3A//www.qq.com/qq2012/loginSuccess.htm"

class LoginPage(QWebPage):

    def __init__(self, parent = None):
        super(LoginPage, self).__init__(parent)

    def allCookies(self):
        return self.networkAccessManager().cookieJar().allCookies()

    def clearAllCookie(self):
        cookieJar = self.networkAccessManager().cookieJar()
        for cookie in self.networkAccessManager().cookieJar().allCookies():
            cookieJar.deleteCookie(cookie)

    def extension(self, extension, option, output):
        if(extension == QWebPage.ErrorPageExtension):
            output.content = QByteArray("<center>网络异常</center>".encode("utf-8"))
            return True
        return super(LoginPage, self).extension(extension, option, output)

    def supportsExtension(self, extension):
        if(extension == QWebPage.ErrorPageExtension):
            return True    # 当网络异常无法连接时返回异常调用上面的extension方法
        return super(LoginPage, self).supportsExtension(extension)

class LoginView(QWebView):

    def __init__(self, parent = None):
        super(LoginView, self).__init__(parent)
        self.parent = parent
        self._canMove = False
        # 设置自定义右键菜单
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        # 自定义的webpage
        self.wpage = LoginPage(self)
        self.setPage(self.wpage)
        # 网页Frame
        self.mainFrame = self.wpage.mainFrame()
        self.mainFrame.javaScriptWindowObjectCleared.connect(self.setJavaScriptObject)
        # 链接点击事件
        # self.linkClicked.connect(self.load)
        # 加载完成事件
        self.loadFinished.connect(self.onFinish)
        # 右键菜单事件
#         self.customContextMenuRequested.connect(self.onMenu)

        # 菜单
        self.menus = QMenu(self)
        self.menus.addAction(self.pageAction(QWebPage.Reload))
        # 浏览器设置
        setting = self.settings()
        # 设置编码
        setting.setDefaultTextEncoding("gbk")
        # 开启开发者功能
        # setting.setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

        self.isStart = True
        self.loadStarted.connect(self.onStart)

    def setJavaScriptObject(self):
        self.mainFrame.addToJavaScriptWindowObject("CLIENT", self.parent)

    def onStart(self):
        self.isStart = True

    def onFinish(self, ok):
        self.isStart = False
        if ok: self.mainFrame.evaluateJavaScript("document.onselectstart = function(){return false;}")
        # 移除所有网页中的链接跳转
        for element in self.mainFrame.findAllElements('a[class="link"]'):
            element.setAttribute("href", "javascript:void(0);")    # 把所有链接去掉

        # 查找到id为close的控件
        _close = self.mainFrame.findFirstElement(".close")
        # 修改关闭按钮的事件为关闭窗口
        if _close: _close.evaluateJavaScript('document.getElementById("close").onclick = function(){CLIENT.close();};')

        # 获取网页源码
        html = self.wpage.mainFrame().toHtml()

        # 如果发现登录成功
        if html.find("parent.login.loginSuccess()") > -1 and self.url().toString().endswith("loginSuccess.htm"):
            qq = None
            # 遍历cookie从中得到qq号码
            for cookie in self.wpage.allCookies():
                name = cookie.name()
                value = cookie.value()
                if name == b"clientuin":
                    qq = value
                    break
                for name in (b"pt2gguin", b"uin", b"superuin"):
                    try: qq = value[1:];break
                    except: pass
            # 如果没有找到则重新登录
            if not qq: self.load(LOGIN_URL);return    # 未找到qq重新加载
            # 受登录成功cookie的影响导致无法加载页面
            self.wpage.clearAllCookie()    # 所以需要清空
            # 获取头像和昵称
            self.hide()
            self.load(INFO_URL.format(qq = qq.data().decode()))
            return
        # 如果发现获取昵称和头像地址成功
        if html.find("portraitCallBack") > -1:
            # 匹配网页中的数据
            result = re.findall(PATTERN, html)
            try:
                # 未找到重新加载
                if not result: self.load(LOGIN_URL);return
                qq, _, name = result[0][0], result[0][1], result[0][7]
                # 匹配成功后下载头像文件
                manager = self.wpage.networkAccessManager()
                # loop = QEventLoop()
                # 用QWebPage的networkAccessManager管理器下载
                reply = manager.get(QNetworkRequest(QUrl(HEAD_URL.format(qq = qq))))
                # 下载结束后退出子事件循环
                reply.finished.connect(lambda: self.replyFinished(reply, qq, name))
                # 开启子事件循环
                # loop.exec_()
            except: self.load(LOGIN_URL)

    def replyFinished(self, reply, qq, name):
        data = reply.readAll()    # 读取到头像文件
        self.hide()    # 隐藏自己
        # 调用父类的信号发射
        self.parent.FINISHED.emit(qq, name, data)
        reply.deleteLater()
        if self.parent: self.parent.close()

    def contextMenuEvent(self, event):
        # self.menus.exec_(self.mapToGlobal(pos))
        # 显示右键菜单
        self.menus.exec_(self.mapToGlobal(event.pos()))
        super(LoginView, self).contextMenuEvent(event)

    @pyqtSlot(str)
    @pyqtSlot(QUrl)
    def load(self, url):
        super(LoginView, self).load(QUrl(url))

    def closeEvent(self, event):
        self.stop()
        super(LoginView, self).closeEvent(event)

    def mousePressEvent(self, event):
        super(LoginView, self).mousePressEvent(event)
        if self.isStart:
            self._canMove = True
            self.parent.mousePressEvent(event)
            return
        self._canMove = False
        element = self.mainFrame.hitTestContent(event.pos()).element()
        if not element: return
        localName = element.localName()
        if localName == "input" or localName != "div": return
        self._canMove = True
        self.parent.mousePressEvent(event)

    def mouseMoveEvent(self, event):
        super(LoginView, self).mouseMoveEvent(event)
        if self._canMove: self.parent.mouseMoveEvent(event)

    def focusInEvent(self, event):
        super(LoginView, self).focusInEvent(event)
        self.parent.focusInEvent(event)

    def focusOutEvent(self, event):
        super(LoginView, self).focusOutEvent(event)
        self.parent.focusOutEvent(event)

class LoginWindow(QWidget):

    FINISHED = pyqtSignal(str, str, QByteArray)

    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.resize(622, 366)
        # 设置模态
        self.setWindowModality(Qt.ApplicationModal)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框,不在任务栏显示
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        # 布局
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 进度条
        self.progressBar = ProgressUi(self)
        # 浏览器
        self.loginview = LoginView(self)
        self.loginview.loadProgress.connect(self.setValue)

        layout.addWidget(self.progressBar)
        layout.addWidget(self.loginview)

        self.shake = Shake(self)

    def setValue(self, value):
        if not hasattr(self, "_pshow"): self._pshow = True
        if not self._pshow: return
        self.progressBar.setValue(value)
        if value == 100: self.progressBar.hide()

    def login(self):
        self.loginview.load(LOGIN_URL)

    @pyqtSlot()
    def close(self):
        super(LoginWindow, self).close()

    def mousePressEvent(self, event):
        """鼠标按下"""
        if event.button() == Qt.LeftButton:
            self.mpos = event.globalPos() - self.pos()    # 记录坐标
        super(LoginWindow, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """鼠标拖动"""
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.mpos)
        super(LoginWindow, self).mouseMoveEvent(event)

    def focusInEvent(self, event):
        super(LoginWindow, self).focusInEvent(event)
        self.shake.stop()

    def focusOutEvent(self, event):
        super(LoginWindow, self).focusOutEvent(event)
        self.shake.shake(self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QLabel
    app = QApplication(sys.argv)
    # 进度条的样式
    app.setStyleSheet("""
ProgressBar {
    min-height: 3px;
    max-height: 10px;
}
ProgressBar::chunk {
    background-color: rgb(92, 170, 21);
}
    """)

    w = QWidget()
    layout = QVBoxLayout(w)
    t = QLabel(w)
    t.setMaximumSize(30, 30)
    layout.addWidget(t)
    w.show()

    l = LoginWindow()

    l.show()
    l.login()

    def end(qq, name, image):
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        t.setPixmap(pixmap.scaled(30, 30))
        t.setToolTip(name)

    l.FINISHED.connect(end)

    sys.exit(app.exec_())
