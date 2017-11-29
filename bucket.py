# -*- coding:utf-8 -*-
# @Time    : 2017/11/28 14:16
# @Author  : leolee
# @File    : bucket.py
import pygame
import globalList

class Bucket:
    def flood(self,x,y,newColor,oldColor):
        t = 0
        a = 0
        if newColor == oldColor:
            return
        stack = []
        dx = [0,1,0,-1]
        dy = [-1,0,1,0]
        stack.append([x,y])
        while len(stack) != 0:
            tmp = stack.pop()
            t += 1
            x = tmp[0]
            y = tmp[1]
            globalList.GLOBAL_MAINSCREEN.set_at(tuple(tmp),newColor)
            for i in range(4):
                a += 1
                nx = x+dx[i]
                ny = y+dy[i]
                if [nx,ny] not in stack and 0 < nx < globalList.GLOBAL_MAINSCREEN_WIDTH \
                        and globalList.GLOBAL_MAINSCREEN_HEIGHT > ny > 0 \
                        and globalList.GLOBAL_MAINSCREEN.get_at((nx,ny)) == oldColor:
                    stack.append([nx,ny])
        print t,a

    def draw(self):
        a = pygame.mouse.get_pos()
        a = (a[0] - 75, a[1] - 50)
        if 0 < a[0] < globalList.GLOBAL_MAINSCREEN_WIDTH and 0 < a[1] < globalList.GLOBAL_MAINSCREEN_HEIGHT:
            self.flood(a[0],a[1],globalList.GLOBAL_RGB,globalList.GLOBAL_MAINSCREEN.get_at(a))

