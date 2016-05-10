#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月25日
@author: Irony."[讽刺]
@site: irony.iask.in
@email: 892768447@qq.com
@file: lolita.py
@description: 可拖动小萝莉
'''

import json
import sys, os
import traceback


PY3 = sys.version_info.major >= 3

if PY3:
    from PyQt5.QtCore import Qt, QPoint    # @UnusedImport @UnresolvedImport
    from PyQt5.QtGui import QPixmap, QMovie, QPainter    # @UnusedImport @UnresolvedImport
    from PyQt5.QtWidgets import QLabel, QToolTip    # @UnusedImport @UnresolvedImport
    from plugins.libs.player3 import LolitaPlayer    # @UnusedImport @UnresolvedImport
else:
    reload(sys)    # @UndefinedVariable
    sys.setdefaultencoding("utf-8")    # @UndefinedVariable
    from PyQt4.QtCore import Qt, QPoint    # @UnresolvedImport @Reimport
    from PyQt4.QtGui import QLabel, QPixmap, QMovie, QPainter, QToolTip    # @UnresolvedImport @Reimport
    from plugins.libs.player2 import LolitaPlayer    # @Reimport @UnusedImport @UnresolvedImport

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class Lolita(QLabel):
    """小萝莉"""

    def __init__(self, ddir = "", parent = None):
        super(Lolita, self).__init__(parent)
        self.parent = parent
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框,不在任务栏显示
        if not parent: self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)

        self.canPlay = True
        self.moveCanPlay = True    # 移动的时候可播放,用于控制一次
        self.moveOut = None    # 是否移动超出边界了?
        self.cindex = 0    # 当前的歌曲序号为0
        self.init(ddir)
        self.setStyleSheet("""
QToolTip {
    color: black;
    min-height: 20px; 
    border: 2px solid white;
    padding: 1px;
    border-radius: 3px;
    opacity: 200;
    background-color: white;
}
""")

    def init(self, ddir):
        """加载lolita.dat配置"""
        if not ddir or not isinstance(ddir, str): return
        try:
            if PY3: conf = json.loads(open(ddir + "/lolita.dat", "rb").read().decode())
            else: conf = json.loads(open(ddir + "/lolita.dat", "rb").read(), "utf-8")
            normal = conf.get("normal", "").format(DATA_DIR = ddir)
            move = conf.get("move", "").format(DATA_DIR = ddir)
            hover = conf.get("hover", "").format(DATA_DIR = ddir)
            press = conf.get("press", "").format(DATA_DIR = ddir)

            image = QPixmap(normal)
            self.resize(image.size())    # 设置窗口的大小
            self.setMinimumSize(image.size())
            self.setMaximumSize((image.size()))

            self.movies = {
                "normal": image,    # 普通
                "move": QPixmap(move),    # 移动
                "hover": QMovie(hover),    # 悬停(会动)
                "press": QPixmap(press),    # 按下
            }

            self._currentImage = image    # 当前的图形
            self.update()

            # 声音播放列表
            playList = conf.get("playList", [])
            self.player = LolitaPlayer(playList, ddir)
            self.player.setCurrentIndex(0)
        except Exception as e:
            self.close()
            traceback.print_exc(e)

    def exit(self):
        self.setMovie(None)
        if hasattr(self, "movies"):
            self.movies.get("hover").stop()
            for k in ("normal", "move", "hover", "press"):
                _m = self.movies.pop(k)
                del _m
            del self.movies
        if hasattr(self, "player"):
            self.player.stop()
            del self.player

    def setMovie(self, movie):
        QLabel.setMovie(self, movie)
        return movie

    def _change_image_(self, name):
        if not hasattr(self, "movies"): return
        if name not in self.movies: return
        self._currentImage = self.movies.get(name)
        if name == "hover": self.setMovie(self._currentImage).start()
        else: self.movies.get("hover").stop()

    def paintEvent(self, event):
        if not hasattr(self, "_currentImage"):
            return super(Lolita, self).paintEvent(event)
        if isinstance(self._currentImage, QMovie):    # 动画
            return super(Lolita, self).paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._currentImage)

    def mousePressEvent(self, event):
        """鼠标按下"""
        if event.button() == Qt.LeftButton:
            self.moveOut = None
            self.moveCanPlay = True
            self._change_image_("press")
            self.update()
            self.mpos = event.globalPos() - self.pos()    # 记录坐标
        event.accept()
        # super(Lolita, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """鼠标拖动"""
        if event.buttons() == Qt.LeftButton:
            if self.parent:    # 在父窗口要限制移动的位置
                x, y = self.pos().x(), self.pos().y()
                pw, ph = self.parent.width(), self.parent.height()
                _x = x
                _y = y
                if x <= 0: _x = 1
                elif y <= 0: _y = 1
                elif x + self.width() >= pw: _x = pw - self.width() - 1
                elif y + self.height() >= ph: _y = ph - self.height() - 1
                self.moveOut = QPoint(_x, _y)
            self.move(event.globalPos() - self.mpos)
            self.canPlay = False
            if self.moveCanPlay:
                self.moveCanPlay = False
                self.player.stop()
                self.player.play(0)    # 播放drag的声音
            self._change_image_("move")
            self.update()
        event.accept()
        # super(Lolita, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """鼠标释放"""
        if event.button() == Qt.LeftButton:
            if self.moveOut:
                self.move(self.moveOut)    # 限制到窗口内
                self.moveOut = None
            self._change_image_("normal")
            self.update()
            self.moveCanPlay = False
            if not self.canPlay:    # 移动了,不播放
                self.canPlay = True
                return
            # 只是点击才播放
            self.cindex = self.cindex + 1
            # 当当前序号大于了排除drag的个数或者是当前序号为drag的序号0时,改为1
            if self.cindex > self.player.mediaCount() - 1: self.cindex = 1
            self.player.play(self.cindex)    # 播放
            text = self.player.getText(self.cindex)
            # print(event.globalPos(), self.pos())
            # 解决有父窗口后无父窗口的文字坐标问题(还是解决的不是很好)
            pos = self.pos() + QPoint(0, -50) if not self.parent else event.globalPos() + QPoint(0, -50)
            QToolTip.showText(pos, text, self)
        event.accept()
        # super(Lolita, self).mouseReleaseEvent(event)

    def enterEvent(self, event):
        """鼠标进入"""
        self._change_image_("hover")
        self.update()
        event.accept()
        # super(Lolita, self).enterEvent(event)

    def leaveEvent(self, event):
        """鼠标离开"""
        self._change_image_("normal")
        self.update()
        event.accept()
        # super(Lolita, self).leaveEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.parent:
            super(Lolita, self).mouseDoubleClickEvent(event)
            return
        if event.button() == Qt.RightButton:
            self.close()
            self.exit()
            QApplication.instance().quit()    # 根据情况使用
        event.accept()
        # super(Lolita, self).mouseDoubleClickEvent(event)

if __name__ == "__main__":
    if PY3: from PyQt5.QtWidgets import QApplication    # @UnresolvedImport @UnusedImport
    else: from PyQt4.QtGui import QApplication    # @Reimport @UnresolvedImport
    app = QApplication(sys.argv)
    w = Lolita(ddir = "../../data" if PY3 else os.path.abspath("../../data"))
    w.show()
    w.setStyleSheet("""
    QToolTip {
        color: black;
        min-height: 20px; 
        border: 2px solid white;
        padding: 1px;
        border-radius: 3px;
        opacity: 200;
        background-color: white;
    }
    """)
    sys.exit(app.exec_())
