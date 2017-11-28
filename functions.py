# -*- coding:utf-8 -*-
# @Time    : 2017/11/22 15:00
# @Author  : leolee
# @File    : functions.py
import pygame
import globalList
from pen import Pen
from eraser import Eraser
from spray import Spray
from bucket import Bucket
from pygame.locals import *

def pointInRect(pos,rect):
    if pos[0] >= rect[2] or pos[0] <= rect[0] or pos[1] >= rect[3] or pos[1] <= rect[1]:
        return False
    return True

def setTools():
    if globalList.GLOBAL_PENCHOOSE == 'pen':
        P = Pen()
        return P
    elif globalList.GLOBAL_PENCHOOSE == 'eraser':
        E = Eraser()
        return E
    elif globalList.GLOBAL_PENCHOOSE == 'spray':
        S = Spray()
        return S
    elif globalList.GLOBAL_PENCHOOSE == 'bucket':
        B = Bucket()
        return B

def create_scales(height):
    red_scale_surface = pygame.surface.Surface((575, height))
    green_scale_surface = pygame.surface.Surface((575, height))
    blue_scale_surface = pygame.surface.Surface((575, height))
    for x in range(575):
        c = int((x / 575.) * 255.)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface
