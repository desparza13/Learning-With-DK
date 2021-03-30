#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:50:43 2020

@author: danielaesparza
"""
import pygame
import config as c

#Donkey Kong barrels basic functioning

def collide(): #checks whether or not Mario collides with a barrel
    global collition
    for i in range(0,4,1):
        if c.mX+20 >= c.barrelX[i] and c.mX <= c.barrelX[i]+26 and c.mY+30 >= c.barrelY[i] and c.mY <= c.barrelY[i]+20:
            collition = True
            c.barrelX[i] -= 100
            break
        else:
            collition = False
            
    return collition
        



