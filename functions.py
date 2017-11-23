# -*- coding:utf-8 -*-
# @Time    : 2017/11/22 15:00
# @Author  : leolee
# @File    : functions.py

import globalList
from pen import Pen
from eraser import Eraser

def pointInRect(pos,rect):
    if pos[0] >= rect[2] or pos[0] <= rect[0] or pos[1] >= rect[3] or pos[1] <= rect[1]:
        return False
    return True

def setTools():
    if globalList.GLOBAL_PENCHOOSE == 1:
        P = Pen()
        return P
    elif globalList.GLOBAL_PENCHOOSE == 2:
        E = Eraser()
        return E
