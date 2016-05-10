#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月26日
@author: Irony."[讽刺]
@site: irony.iask.in
@email: 892768447@qq.com
@file: test.test_json.py
@description: 
'''
import json

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

data = """
{
    "data" : [["", "data/voice/kiana_drag.mp3"],
        ["快看快看，我抽到了什么~", "data/voice/kiana_1.mp3"],
        ["去死去死去死去死！", "data/voice/kiana_2.mp3"],
        ["主人，人家钱包都空了", "data/voice/kiana_3.mp3"],
        ["变态！", "data/voice/kiana_4.mp3"],
        ["Kiana，变身！", "data/voice/kiana_5.mp3"],
        ["嗯，miHoYo什么的，最讨厌了~", "data/voice/kiana_6.mp3"],
        ["千万别小看我哟~", "data/voice/kiana_7.mp3"],
        ["要加油哦！", "data/voice/kiana_8.mp3"],
        ["我就知道主人最疼人家啦~", "data/voice/kiana_9.mp3"],
        ["锵锵~", "data/voice/kiana_10.mp3"],
        ["烦死啦，走开走开啦！", "data/voice/kiana_11.mp3"]]
}
"""

d = json.loads(open("../data/lolita.dat", "rb").read().decode()).get("playList")

print(d)
