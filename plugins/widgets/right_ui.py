#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月4日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: plugins.widgets.right_ui.py
@description: 
"""
import os

from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from plugins.uifiles.right_ui import Ui_BlogFormRight
from plugins.utils.settings import Settings
from plugins.widgets.base import BaseWidget
from plugins.widgets.right_item import ItemHeader, ItemContent, ItemHead, \
    ItemLabel


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class RightUi(QWidget, Ui_BlogFormRight, BaseWidget):

    def __init__(self, parent = None):
        super(RightUi, self).__init__(parent)
        self.setupUi(self)
        # 添加分类测试数据
        self.addItems("分类目录", ItemLabel, [
            "Qt",
            "QSS",
            "PyQt",
            "Python",
            "Android",
        ])
        # 添加最近访客测试数据
        head = os.path.join(Settings().dataDir, "images", "head.png")
        self.addItems("最近访客", ItemHead, [
            {"qq":"892768447", "nick":"Irony.\"[讽刺]", "head":head},
            {"qq":"892768447", "nick":"Irony.\"[讽刺]", "head":head},
            {"qq":"892768447", "nick":"Irony.\"[讽刺]", "head":head},
            {"qq":"892768447", "nick":"Irony.\"[讽刺]", "head":head},
        ])

        # 全部展开
        self.blog_right_widget.expandAll()

    def addItems(self, name, widget, datas):
        # 头部
        itemHeader = QTreeWidgetItem(self.blog_right_widget)
        # 自定义控件
        self.blog_right_widget.setItemWidget(itemHeader, 0, ItemHeader(name, self))
        # 内容
        itemHeads = QTreeWidgetItem(itemHeader)
        itemContent = ItemContent(self)
        for data in datas:
            itemContent.addItem(widget(data, self))
        self.blog_right_widget.setItemWidget(itemHeads, 0, itemContent)

    # QTreeWidget父节点单击事件
    def on_blog_right_widget_itemClicked(self, item, column):
        if item.childCount() > 0:
            # 如果含有child则展开或者关闭
            if item.isExpanded():
                # 如果展开则关闭
                item.setExpanded(False)
            else:
                item.setExpanded(True)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from plugins import apis
    app = QApplication(sys.argv)
    w = RightUi()
    w.show()
    w.setStyleSheet(apis.APIS.readFile("../../data/themes/default/RightUi.qss"))
    sys.exit(app.exec_())
