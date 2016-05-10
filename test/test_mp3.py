#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月25日
@author: Irony."[讽刺]
@site: irony.iask.in
@email: 892768447@qq.com
@file: test.test_mp3.py
@description: 
'''
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtCore import QUrl

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


app = QApplication([])

# 播放列表
playlist = QMediaPlaylist()

_list = []
for i in range(1, 12):
    print("../data/lolita/voice/kiana_%d.mp3" % i)
    _list.append(QMediaContent(QUrl("../data/lolita/voice/kiana_%d.mp3" % i)))
playlist.addMedia(_list)
# 只播放当前的
playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)


player = QMediaPlayer()
# 设置播放列表
player.setPlaylist(playlist)
# 设置音量
player.setVolume(100)

def play():
    playlist.setCurrentIndex(2)
    player.play()
    playlist.setCurrentIndex(0)
#     currentIndex = playlist.currentIndex() + 1
#     print(currentIndex)
#     if currentIndex > playlist.mediaCount():
#         currentIndex = 0
#     playlist.setCurrentIndex((currentIndex))
#     player.play()

btn = QPushButton("play", clicked = play)
btn.show()

app.exec_()
