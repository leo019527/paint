# -*- coding:utf-8 -*-
# @Time    : 2017/11/21 17:28
# @Author  : leolee
# @File    : eraser.py
import pygame
import paintTools
import globalList

class pen(paintTools):
    def draw(self):
        pygame.draw.circle(globalList.GLOBAL_MAINSCREEN,
                           (255,255,255),
                           pygame.mouse.get_pos(),
                           globalList.GLOBAL_PENSIZE)