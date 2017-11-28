# -*- coding:utf-8 -*-
# @Time    : 2017/11/21 17:28
# @Author  : leolee
# @File    : eraser.py
import pygame

import globalList
import paintTools


class Eraser():
    def draw(self):
        if globalList.GLOBAL_PEN_LASTPOS != (-1,-1):
            a = pygame.mouse.get_pos()
            a = (a[0] - 75, a[1] - 50)
            pygame.draw.line(globalList.GLOBAL_MAINSCREEN,
                             (255,255,255),
                             globalList.GLOBAL_PEN_LASTPOS,
                             a,
                             globalList.GLOBAL_PENSIZE)
            globalList.GLOBAL_PEN_LASTPOS = a