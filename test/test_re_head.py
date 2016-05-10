#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2016年5月7日
@author: Irony."[讽刺]
@site: irony.iask.in , mzone.iask.in
@email: 892768447@qq.com
@file: test.a.py
@description: 
"""
import re


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2016 Irony.\"[讽刺]"
__Version__ = 1.0

s = """
/*左侧控件*/
#BlogFormLeft {
    min-width: 260px;
    max-width: 260px;
    background-color: #27ae61;
}

/*左侧头像控件*/
#blog_head_label {
    min-width: 130px;
    max-width: 130px;
    min-height: 130px;
    max-height: 130px;
    border-radius: 65px; /*圆角*/
    background: url(%DATA_DIR%/themes/default/images/icon_face.png) center no-repeat;
}

/*左侧博客名字*/
#blog_title_label {
    min-width: 130px;
    max-width: 130px;
    color: white;
    font: 20pt "Microsoft YaHei";
    padding-top: -15px;
}

/*左侧搜索区域*/
#blog_search_widget {
    height: 30px;
    border: none;
    background-color: white;
    border-radius: 15px;
}

/*左侧搜索框*/
#blog_search_edit {
    width: 220px;
    height: 30px;
    border: none;
    color: #666;
    background: #fff;
    outline: none;
    padding-left: 10px;
    padding-right: 5px;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
}

/*左侧搜索框按钮*/
#blog_search_button {
    width: 26px;
    height: 26px;
    border: none;
    color: white;
    background-color: rgb(39, 174, 97);
    outline: none;
    margin: 4px;
    border-radius: 13px;
    font: 12pt "FontAwesome";
}

/*左侧搜索框按钮鼠标悬停*/
#blog_search_button:hover {
    background-color: rgb(232, 76, 61);
}

/*左侧底部的菜单列表*/
#blog_menu_list {
    outline:0px; /*去掉虚线框*/
    background-color: transparent;
}

/*左侧底部的菜单列表选中状态样式*/
#blog_menu_list::item:selected {
    background-color: transparent;
}

/*左侧底部的菜单列表鼠标悬停样式*/
#blog_menu_list::item:hover {
    background-color: transparent;
}
"""

ss = re.findall("#blog_head_label(.*?)}", s, re.S)[0]

print(ss)

ss = re.sub("url\((.*?)\)", "url(%s/test.png)" % "data", ss)

print(ss)
