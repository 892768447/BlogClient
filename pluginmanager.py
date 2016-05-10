#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: pluginmanager.py
@description: 插件管理器
"""
from collections import OrderedDict
import os
import traceback


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

class PluginManager(object):

    def __init__(self):
        self.parent = None
        self.__plugins = []    # 插件模块名
        self.__clazzs = OrderedDict()    # 插件模块信息

    def __iter__(self):
        return iter(self.__clazzs.keys())

    def clear(self):
        if not hasattr(self, "__clazzs"): return
        if not hasattr(self, "__plugins"): return
        self.stopAll()
        self.__plugins.clear()
        for _, info in self.__clazzs.items():
            info.pop("class")
        self.__clazzs.clear()
        del self.__plugins
        del self.__clazzs

    def __del__(self):
        print("PluginManager", "__del__")
        self.clear()

    def loadPlugins(self, pluginDir = "plugins"):
        """加载插件"""
        self._getPlugins(pluginDir)
        for name in self.__plugins:
            # import module,get Main class
            try: self._parsePlugins(__import__(pluginDir + "." + name, fromlist = ("Main")).Main)
            except Exception as e: traceback.print_exc(e)
        def sort_key(k):
            # 根据value中的seq排序
            return self.__clazzs.get(k).get("seq", -1)
        # 得到排序后的keys
        keys = sorted(self.__clazzs, key = sort_key)
        a = OrderedDict()
        for key in keys:
            a[key] = self.__clazzs.get(key)
        self.__clazzs.clear()
        self.__clazzs = a.copy()
        del a
        self._runPlugins()

    def _runPlugins(self):
        """按顺序运行插件"""
        for clazz, info in self.__clazzs.items():
            try:
                if info.get("seq", -1) == 0:    # 如果是第一个则当作主界面
                    main = clazz(self)    # 实例化类
                    self.parent = main.parent
                else:
                    main = clazz(self.parent)
                main.run()
                info["state"] = 1    # 运行成功
                info["class"] = main
            except Exception as e:
                info["state"] = -1    # 运行失败
                traceback.print_exc(e)

    def stopPlugin(self, clazz):
        """停止插件"""
        try:
            main = self.__clazzs.get(clazz).get("class")
            main.stop()
            self.__clazzs.get(clazz)["state"] = 0
        except Exception as e: traceback.print_exc(e)

    def stopAll(self):
        """停止所有插件"""
        keys = list(self.__clazzs.keys())    # 得到所有的键
        keys.reverse()    # 翻转
        for clazz in keys:    # 从最后开始停止
            self.stopPlugin(clazz)

    def _getPlugins(self, pluginDir = "plugins"):
        """遍历插件的目录得到模块名称"""
        for name in os.listdir(pluginDir):
            if name == "__init__.py": continue
            if name.endswith("_plugin.py"):
                self.__plugins.append(name[:-3])
            if name.endswith("_plugin.pyc"):
                self.__plugins.append(name[:-4])
        # print(self.__plugins)

    def _parsePlugins(self, clazz):
        """获取插件中的基本信息"""
        try: name = getattr(clazz, "name")
        except: name = str(clazz)
        try: author = getattr(clazz, "author")
        except: author = ""
        try: version = getattr(clazz, "version")
        except: version = 1.0
        try: description = getattr(clazz, "description")
        except: description = ""
        try: seq = getattr(clazz, "sequence")
        except: seq = -1
#         print("\n\n-----*plugin info*-----\nname={name}, seq={seq}, author={author}, version={version}, description={description}\n-----***-----".format(
#             name = name, seq = seq, author = author, version = version, description = description
#         ))
        self.__clazzs[clazz] = {
            "name":name, "author":author, "state":0,    # 0表示未运行,1运行,-1失败
            "seq":seq,    # 加载顺序
            "version":version, "description":description, "class":None
        }
