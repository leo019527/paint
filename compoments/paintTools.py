# -*- coding:utf-8 -*-
# @Time    : 2017/11/20 11:07
# @Author  : leolee
# @File    : paintTools.py

#画图工具的父类
import pygame
import globalList

def text(say):
    screen = globalList.GLOBAL_MAINSCREEN
    width = screen.get_width()
    height = screen.get_height()
    text = pygame.font.Font("arial", "16").render(say, True, (0, 0, 0))
    textWidth = text.get_width()
    textHeight = text.get_height()
    screen.blit(text, ((width - textWidth) / 2, (height - textHeight) / 2))

class paintTools:
    #画图设置
    def drawSet(self):
        text("You haven't choose the tool")

    #画图
    def draw(self):
        text("You haven't set the tool")
