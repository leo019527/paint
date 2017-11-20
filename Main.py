# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *

# INIT
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("paint")


# <editor-fold desc="varibles">
# COLOR
color_bottle_background = (189, 189, 189)
color_menu_tools = (255, 255, 255)

# LOCATION (resizable)
location_menu = (0, 0, 650, 60)
location_tool = (0, 70, 70, 430)

# SUBSURFACE
sub_menu = screen.subsurface(location_menu)
sub_tool = screen.subsurface(location_tool)
# </editor-fold>



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    screen.fill(color_bottle_background)
    sub_menu.fill(color_menu_tools)
    sub_tool.fill(color_menu_tools)
    pygame.display.update()
