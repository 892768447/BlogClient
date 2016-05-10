#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年4月19日
@author: Irony."[讽刺]
@site: http://irony.iask.in
@email: 892768447@qq.com
@file: utils.tea.py
@description: 
'''

from random import randrange
from time import time

import xxtea


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2015 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

def encrypt(key, data):
    """
    @note: 加密
    @param key: getTime()
    @param data: data
    @return: bytes
    """
    try: return xxtea.encrypt(key + data, key[:16])
    except: return b""

def decrypt(key, data):
    """
    @note: 加密
    @param key: getTime()
    @param data: data
    @return: bytes
    """
    try: return xxtea.decrypt(data, key[:16])[len(key):]
    except: return b""

def encrypt_hex(key, data):
    """
    @note: 加密内容变为hex
    @return: bytes
    """
    try: return xxtea.encrypt_hex(data, key)
    except: return b""

def decrypt_hex(key, data):
    """
    @note: 解密内容变为hex
    @return: bytes
    """
    try: return xxtea.decrypt_hex(data, key)
    except: return b""

def getKey():
    """
    @note: 获取key(由16位time + | + time加密的数据组成)
    @return: encrypt time
    @return: bytes
    """
    __t = str(time())
    __l = len(__t)
    if __l > 16: __t = __t[:16]
    elif __l < 16: __t += "".join((str(randrange(9)) for i in range(16 - __l)))
    return __t.encode() + b"|" + encrypt_hex(__t, __t)

def getKey16(key = None):
    """
    @note: 获取key的前16位
    """
    if isinstance(key, str): key = key.encode()    # str->bytes
    if key: return key[:16]
    return getKey()[:16]

def check(key):
    """
    @note: 校验key合法性
    """
    if isinstance(key, str): key = key.encode()    # str->bytes
    k, d = key[:16], key[17:]
    if k != decrypt_hex(k, d):
        return False
    return True

if __name__ == "__main__":
    key = getKey()
    print(len(key), key)
    k, d = key[:16], key[17:]
    print(k, d, decrypt_hex(k, d))

    key = getKey16(key)

    data = b"1232134"
    d = encrypt(key, data)
    print(d)
    d = decrypt(key, d)
    print(d)
