# -*- coding:utf-8 -*-
# @Time    : 2017/11/28 10:38
# @Author  : leolee
# @File    : spray.py
import pygame
import globalList
import numpy as np
from numpy.linalg import cholesky
import math
import time

class Spray:
    def dis(self,x,y):
        return math.sqrt(x*x+y*y)
    def drawDot(self,x,y):
        mu = np.array([[0, 0]])
        Sigma = np.array([[0.1, 0], [0, 0.1]])
        R = cholesky(Sigma)
        s = np.dot(np.random.randn(150, 2), R) + mu
        for i in range(len(s)):
            if self.dis(s[i][0]*5,s[i][1]*5) <= globalList.GLOBAL_PENSIZE:
                globalList.GLOBAL_MAINSCREEN.set_at((int(x+s[i][0]*50),int(y+s[i][1]*50)),globalList.GLOBAL_RGB)


    def draw(self):
        if time.time() - globalList.GLOBAL_SPRAY_TIME >= 0.015:
            a = pygame.mouse.get_pos()
            a = (a[0] - 75, a[1] - 50)
            self.drawDot(a[0],a[1])
            globalList.GLOBAL_SPRAY_TIME = time.time()
