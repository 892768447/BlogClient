#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月2日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: utils.http.py
@description: 
"""
import json

from PyQt5.QtCore import QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

from plugins.utils.singleton import singleton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

@singleton
class Http(QNetworkAccessManager):

    def __init__(self, parent = None):
        QNetworkAccessManager.__init__(self, parent)

    def _getRequest(self, url):
        request = QNetworkRequest(QUrl(url))
        # key
        request.setRawHeader(b"Key", b"")
        # request.setRawHeader("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        # request.setRawHeader("Accept-Encoding", "gzip, deflate, sdch")
        # request.setRawHeader("Accept-Language", "zh-CN,zh;q=0.8")
        # header
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/octet-stream")
        # user agent
        request.setHeader(QNetworkRequest.UserAgentHeader, "Blog/Mzone 1.0")
        return request

    def get(self, url):
        return QNetworkAccessManager.get(self, self._getRequest(url))

    def post(self, url, data):
        if isinstance(data, dict): data = json.dumps(data)
        if isinstance(data, str): data = QByteArray(len(data), data)
        elif isinstance(data, bytes): data = QByteArray(data)
        else:
            data = str(data)
            data = QByteArray(len(data), data)
        return QNetworkAccessManager.post(self, self._getRequest(url), data)
