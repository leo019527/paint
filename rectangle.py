# -*- coding:utf-8 -*-
# @Time    : 2017/11/29 14:31
# @Author  : leolee
# @File    : rectangle.py
import pygame
import globalList
from pygame import *

class Rectangle:
    def draw(self):
        if globalList.GLOBAL_PEN_LASTPOS != (-1,-1):
            a = pygame.mouse.get_pos()
            a = (a[0]-75, a[1]-50)
            globalList.GLOBAL_MAINSCREEN.blit(globalList.GLOBAL_RECTANGLE_SCREEN_TMP,(0,0))
            pygame.draw.rect(globalList.GLOBAL_MAINSCREEN,globalList.GLOBAL_RGB,(globalList.GLOBAL_RECTANGLE_START_POS[0],
                                                                                           globalList.GLOBAL_RECTANGLE_START_POS[1],
                                                                                 a[0]-globalList.GLOBAL_RECTANGLE_START_POS[0],
                                                                                 a[1]-globalList.GLOBAL_RECTANGLE_START_POS[1]
                                                                                 ),globalList.GLOBAL_PENSIZE)

