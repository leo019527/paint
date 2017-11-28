# -*- coding:utf-8 -*-
import sys
import pygame
from pygame import *
from pygame.locals import *
from pen import *
import globalList
import paintTools
import functions
from eraser import Eraser


# INIT
pygame.init()
screen = pygame.display.set_mode((575, 700),pygame.RESIZABLE)
mainSurface = Surface((500,500))
mainSurface.fill((255,255,255))
pygame.display.set_caption("paint")
globalList.GLOBAL_MAINSCREEN = mainSurface
pressFlagPlus = False
pressFlagMinus = False
globalList.GLOBAL_RED,\
    globalList.GLOBAL_GREEN,\
    globalList.GLOBAL_BLUE = functions.create_scales(50)


# <editor-fold desc="varibles">
# COLOR
color_bottle_background = (189, 189, 189)
color_menu_tools = (255, 255, 255)
# </editor-fold>

p = Pen()
screen.fill(color_bottle_background)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    # 调色板
    screen.blit(globalList.GLOBAL_RED, (0, 550))
    screen.blit(globalList.GLOBAL_GREEN, (0, 600))
    screen.blit(globalList.GLOBAL_BLUE, (0, 650))
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component * 50 + 550 and y < component * 50 + 600:
                tmp = list(globalList.GLOBAL_RGB)
                tmp[component] = int((x / 574.) * 255.)
                globalList.GLOBAL_RGB = tmp
    for component in range(3):
        pos = (int((globalList.GLOBAL_RGB[component] / 255.) * 574) , component*50 + 575)
        pygame.draw.circle(screen,(255,255,255),pos,25)


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
            globalList.GLOBAL_PEN_LASTPOS = (globalList.GLOBAL_PEN_LASTPOS[0]-75,globalList.GLOBAL_PEN_LASTPOS[1]-50)
            globalList.GLOBAL_PEN_FLAG = True
        p.draw()
    elif not pygame.mouse.get_pressed()[0]:
        globalList.GLOBAL_PEN_FLAG = False

    screen.blit(globalList.GLOBAL_MAINSCREEN,(75,50))
    #修改标题
    pygame.display.set_caption("Paint - pensize:" + str(globalList.GLOBAL_PENSIZE) + " RGB:" + str(globalList.GLOBAL_RGB) + " pen:" + str(globalList.GLOBAL_PENCHOOSE))
    pygame.display.update()
