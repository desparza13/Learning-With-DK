#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:29:25 2020

@author: danielaesparza
"""
import pygame
#0 a 630
leftLimitsY = [541, 341]
rightLimitsY = [638, 438, 244]
#-----------------------------------------------------------------------------

#Variables for excel questions
cathegories = []
questions = []
optionA = []
optionB = []
optionC = []
correctAnswer = []
#-----------------------------------------------------------------------------
#Variables for Mario
    #Starting Coordinates
FloorY = 735
mX = 5
mY = 690
bX = 0
bY = 700
dkX = 0
dkY = 690
xMouse = 0
yMouse = 0
vel_y=9
jump=False
climb = False

    #Image initialization
marioStandingRight = pygame.image.load("Assets/mRight.png")
marioStandingLeft = pygame.image.load("Assets/mLeft.png")
marioRunningRight = pygame.image.load("Assets/mRunRight.png")
marioRunningLeft = pygame.image.load("Assets/mRunLeft.png")
marioClimbingLadder1 = pygame.image.load("Assets/mClimb1.png")
marioClimbingLadder2 = pygame.image.load("Assets/mClimb2.png")
barrelImage = pygame.image.load("Assets/barrel1.png")
donkeyKongClimbingImage1 = pygame.image.load("Assets/dkUp1.png")
donkeyKongClimbingImage2 = pygame.image.load("Assets/dkUp2.png")
donkeyKongWalkingRightImage = pygame.image.load("Assets/dkRight.png")
donkeyKongWalkingLeftImage = pygame.image.load("Assets/dkLeft.png")
donkeyKongFacingFront = pygame.image.load("Assets/dkForward.png")
levelToPlay = pygame.image.load("Assets/platform1.png")
levelWithLadders = pygame.image.load("Assets/withLadder.png")
peachStanding = pygame.image.load("Assets/pStanding.png")
peachCallingForHelp = pygame.image.load("Assets/pHelp.png")
ladder1 = pygame.image.load("Assets/ladder.png")
ladder2 = pygame.image.load("Assets/ladder2.png")
ladder3 = pygame.image.load("Assets/ladder2.png")
ladder4 = pygame.image.load("Assets/ladder2.png")
ladder5 = pygame.image.load("Assets/ladder2.png")

    #Variables initialization
marioImage = marioStandingRight
donkeyKongImage = donkeyKongClimbingImage1
scenarioImage = levelWithLadders
peachImage = peachStanding
gameRunning = False
intro = False
mXChange = 0
mYChange = 0
dkChangeX = 0
dkChangeY = 0
supportDkAnimation = 0
#-----------------------------------------------------------------------------
#Variables for barrel
    #Image initialization
barrelStack = pygame.image.load("Assets/barrelFour.png")
barrelDown = pygame.image.load("Assets/barrelDown.png")
barrel1 = pygame.image.load("Assets/barrel1.png")
barrel2 = pygame.image.load("Assets/barrel2.png")
barrel3 = pygame.image.load("Assets/barrel3.png")
barrel4 = pygame.image.load("Assets/barrel4.png")
barrelSequence = [barrel1, barrel2, barrel3, barrel4] #array used to display barrel movement animation
barrelPic = []

    #Starting coordinates
barrelX = [213, -50, -300, -700]
barrelY = [238, 238, 238, 238]
ladderX=[428,103,428,103,428]
ladderY=[275,360,450,550,650]
#-----------------------------------------------------------------------------
    #Points 
currentGamePoints = 0

