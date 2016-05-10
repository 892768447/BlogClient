#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月20日
@author: Irony."[讽刺]
@site: irony.iask.in
@email: 892768447@qq.com
@file: singleton.py
@description: 
'''
from threading import Lock


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

def singleton(cls, *args, **kwargs):
    """单例模式"""
    __instances = {}
    __lock = Lock()

    def _singleton(*args, **kwargs):
        if cls not in __instances:
            __lock.acquire()
            __instances[cls] = cls(*args, **kwargs)
            __lock.release()
        return __instances[cls]
    return _singleton
