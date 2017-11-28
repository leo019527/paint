# -*- coding:utf-8 -*-
# @Time    : 2017/11/28 21:00
# @Author  : leolee
# @File    : tube.py
import pygame
import globalList

class Tube:
    def draw(self):
        a = pygame.mouse.get_pos()
        a = (a[0] - 75, a[1] - 50)
        if 0 < a[0] < 500 and 0 < a[1] < 500:
            rgb = globalList.GLOBAL_MAINSCREEN.get_at(a)
            globalList.GLOBAL_RGB = (rgb[0],rgb[1],rgb[2])