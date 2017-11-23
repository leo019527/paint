# -*- coding:utf-8 -*-
# @Time    : 2017/11/20 16:43
# @Author  : leolee
# @File    : pen.py
import pygame
import globalList
import paintTools


class Pen():
    def draw(self):
        if globalList.GLOBAL_PEN_LASTPOS != (-1,-1):
            a = pygame.mouse.get_pos()
            pygame.draw.line(globalList.GLOBAL_MAINSCREEN,
                             globalList.GLOBAL_RGB,
                             globalList.GLOBAL_PEN_LASTPOS,
                             a,
                             globalList.GLOBAL_PENSIZE)
            globalList.GLOBAL_PEN_LASTPOS = a
