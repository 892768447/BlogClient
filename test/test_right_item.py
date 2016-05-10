#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月8日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.test_right_item.py
@description: 
"""
import os

from PyQt5.QtWidgets import QWidget, QApplication, QTreeWidgetItem

from plugins.uifiles.right_ui import Ui_BlogFormRight
from plugins.widgets.right_item import ItemLabel, ItemHead, ItemHeader, \
    ItemContent


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

class RightUi(QWidget, Ui_BlogFormRight):

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
        head = os.path.join("../data", "images", "head.png")
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


app = QApplication([])
r = RightUi()
r.show()
r.setStyleSheet("""
/*右侧Item*/
#blog_right_widget {
    outline:0px; /*去掉虚线框*/
    background-color: transparent;
}

/*右侧Item选中状态样式*/
#blog_right_widget::item:selected {
    background-color: transparent;
}

/*右侧Item鼠标悬停样式*/
#blog_right_widget::item:hover {
    background-color: transparent;
}

/*item的头部*/
ItemHeader {
    min-height: 50px;
    max-height: 50px;
    color: white;
    text-align: left;
    padding-left: 20px;
    margin-top: 20px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    background-color: rgb(64, 74, 88);
}

/*item标签*/
ItemLabel {
    min-height: 28px;
    max-height: 28px;
    border: none;
    color: rgb(136, 136, 136);
    background-color: rgb(245, 245, 245);
}

/*item标签鼠标悬停*/
ItemLabel:hover {
    color: white;
    background-color: rgb(39, 174, 97);
}

/*ItemVContent*/
ItemVContent {
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    background-color: white;
}

/*item头像*/
ItemHead {
    min-height: 50px;
    max-height: 50px;
    border: none;
}
""")
app.exec_()
