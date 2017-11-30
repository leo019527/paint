# -*- coding:utf-8 -*-
import sys
import pygame
from pygame import *
from pygame.locals import *
from pen import *
import globalList
import functions
import time

# <editor-fold desc="varibles">
# COLOR
color_bottle_background = (189, 189, 189)
color_menu = (118, 118, 118)
tool_choose_flag = -1
ctrlZ_flag = False
tool_dic = {'pen':1,'eraser':2,'spray':3,'bucket':4,'tube':5,'rectangle':6}
rectangle_flag = False
# </editor-fold>


# INIT
pygame.init()
screen = pygame.display.set_mode((575, 700),pygame.RESIZABLE)
mainSurface = Surface((500,500))
mainSurface.fill((255,255,255))
pygame.display.set_caption("paint")
globalList.GLOBAL_MAINSCREEN = mainSurface
globalList.GLOBAL_MAINSCREEN_WIDTH = mainSurface.get_width()
globalList.GLOBAL_MAINSCREEN_HEIGHT = mainSurface.get_height()
pressFlagPlus = False
pressFlagMinus = False
globalList.GLOBAL_RED,\
    globalList.GLOBAL_GREEN,\
    globalList.GLOBAL_BLUE = functions.create_scales(50)
globalList.GLOBAL_SPRAY_TIME = time.time()
tools = []
toolsRect = []
for i in range(1,7):
    tools.append(pygame.image.load("imgs/"+str(i)+".png").convert_alpha())
for i in range(6):
    toolsRect.append((5,80+75*i,70,145+75*i))


p = Pen()
screen.fill(color_bottle_background)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    screen.fill(color_bottle_background)
    # 工具栏
    for i in range(6):
        screen.blit(tools[i],(7,82+75*i))
    # 调色板
    screen.blit(globalList.GLOBAL_RED, (0, 550))
    screen.blit(globalList.GLOBAL_GREEN, (0, 600))
    screen.blit(globalList.GLOBAL_BLUE, (0, 650))
    #处理鼠标事件
    x, y = pygame.mouse.get_pos()
    if tool_choose_flag != -1 and not functions.pointInRect((x,y),toolsRect[tool_choose_flag]):
        functions.cleanBorder(screen,tool_choose_flag)
        tool_choose_flag = -1
    # 鼠标移动
    for i in range(6):
        if functions.pointInRect((x,y),toolsRect[i]):
            functions.drawBorder(screen,i)
            tool_choose_flag = i
    # 鼠标点击
    if pygame.mouse.get_pressed()[0]:
        if tool_choose_flag != -1:
            if tool_choose_flag == 0:
                globalList.GLOBAL_PENCHOOSE = 'pen'
            elif tool_choose_flag == 1:
                globalList.GLOBAL_PENCHOOSE = 'eraser'
            elif tool_choose_flag == 2:
                globalList.GLOBAL_PENCHOOSE = 'spray'
            elif tool_choose_flag == 3:
                globalList.GLOBAL_PENCHOOSE = 'bucket'
            elif tool_choose_flag == 4:
                globalList.GLOBAL_PENCHOOSE = 'tube'
            elif tool_choose_flag == 5:
                globalList.GLOBAL_PENCHOOSE = 'rectangle'
        else:
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
        globalList.GLOBAL_PENCHOOSE = 'pen'
    elif pressed_keys[K_2]:
        globalList.GLOBAL_PENCHOOSE = 'eraser'
    elif pressed_keys[K_3]:
        globalList.GLOBAL_PENCHOOSE = 'spray'
    elif pressed_keys[K_4]:
        globalList.GLOBAL_PENCHOOSE = 'bucket'
    elif pressed_keys[K_5]:
        globalList.GLOBAL_PENCHOOSE = 'tube'
    elif pressed_keys[K_6]:
        globalList.GLOBAL_PENCHOOSE = 'rectangle'
    #撤销实现
    if pressed_keys[306] and pressed_keys[122]:
        if not ctrlZ_flag and len(globalList.GLOBAL_MAINSCREEN_LIST) > 0:
            globalList.GLOBAL_MAINSCREEN = globalList.GLOBAL_MAINSCREEN_LIST[-1]
            globalList.GLOBAL_MAINSCREEN_LIST.pop()
            ctrlZ_flag = True
    if not pressed_keys[306] and not pressed_keys[122]:
        if ctrlZ_flag:
            ctrlZ_flag = False
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
    if pygame.mouse.get_pressed()[0] and functions.pointInRect((x,y),(75,50,575,550)):
        if rectangle_flag == False:
            globalList.GLOBAL_RECTANGLE_START_POS = (x-75,y-50)
            print globalList.GLOBAL_RECTANGLE_START_POS
            globalList.GLOBAL_RECTANGLE_SCREEN_TMP.blit(globalList.GLOBAL_MAINSCREEN,(0,0))
            rectangle_flag = True
        p = functions.setTools()
        if not globalList.GLOBAL_PEN_FLAG:
            globalList.GLOBAL_PEN_LASTPOS = pygame.mouse.get_pos()
            globalList.GLOBAL_PEN_LASTPOS = (globalList.GLOBAL_PEN_LASTPOS[0]-75,globalList.GLOBAL_PEN_LASTPOS[1]-50)
            globalList.GLOBAL_PEN_FLAG = True
            tmp = Surface((500, 500))
            tmp.blit(globalList.GLOBAL_MAINSCREEN, (0, 0))
            globalList.GLOBAL_MAINSCREEN_LIST.append(tmp)
        p.draw()
    elif not pygame.mouse.get_pressed()[0]:
        if rectangle_flag == True:
            rectangle_flag = False
        if globalList.GLOBAL_PEN_FLAG == True:
            globalList.GLOBAL_PEN_FLAG = False

    screen.blit(globalList.GLOBAL_MAINSCREEN,(75,50))
    #修改标题
    pygame.display.set_caption("Paint - pensize:" + str(globalList.GLOBAL_PENSIZE) + "px RGB:" + str(globalList.GLOBAL_RGB) + " tools: " + str(globalList.GLOBAL_PENCHOOSE))
    pygame.display.update()
