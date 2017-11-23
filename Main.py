# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *
from pen import *
import globalList
import paintTools
import functions
from eraser import Eraser


# INIT
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("paint")
globalList.GLOBAL_MAINSCREEN = screen
pressFlagPlus = False
pressFlagMinus = False


# <editor-fold desc="varibles">
# COLOR
color_bottle_background = (255, 255, 255)
color_menu_tools = (255, 255, 255)

# LOCATION (resizable)
location_menu = (0, 0, 650, 60)
location_tool = (0, 70, 70, 430)

# SUBSURFACE
sub_menu = screen.subsurface(location_menu)
sub_tool = screen.subsurface(location_tool)
# </editor-fold>

p = Pen()
screen.fill(color_bottle_background)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    pressed_keys = pygame.key.get_pressed()
    #改变工具
    if pressed_keys[K_1]:
        globalList.GLOBAL_PENCHOOSE = 1
    elif pressed_keys[K_2]:
        globalList.GLOBAL_PENCHOOSE = 2
    #增减笔刷大小
    if pressed_keys[61]:
        if not pressFlagPlus:
            globalList.GLOBAL_PENSIZE += 1
            pressFlagPlus = True
    elif not pressed_keys[61]:
        pressFlagPlus = False
    if pressed_keys[45]:
        if not pressFlagMinus and globalList.GLOBAL_PENSIZE > 1:
            globalList.GLOBAL_PENSIZE -= 1
            pressFlagMinus = True
    elif not pressed_keys[45]:
        pressFlagMinus = False
    #画图
    if pygame.mouse.get_pressed()[0]:
        p = functions.setTools()
        if not globalList.GLOBAL_PEN_FLAG:
            globalList.GLOBAL_PEN_LASTPOS = pygame.mouse.get_pos()
            globalList.GLOBAL_PEN_FLAG = True
        p.draw()
    elif not pygame.mouse.get_pressed()[0]:
        globalList.GLOBAL_PEN_FLAG = False
    pygame.display.update()
