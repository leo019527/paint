# -*- coding:utf-8 -*-
# @Time    : 2017/11/20 16:43
# @Author  : leolee
# @File    : pen.py
import pygame
import paintTools
import globalList

class pen(paintTools):
    def draw(self):
        pygame.draw.circle(globalList.GLOBAL_MAINSCREEN,
                           globalList.GLOBAL_RGB,
                           pygame.mouse.get_pos(),
                           globalList.GLOBAL_PENSIZE)