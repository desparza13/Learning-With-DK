import pygame, sys
import random 
import config as c
import basicFunctions as bf
import barrels as ba
import Questions as q
import Score as ap
import math as m
BLACK = (0,0,0)
success, failures = pygame.init()
print("Initializing Donkey Kong: {0} successes and {1} failures".format(success,failures))

screen = pygame.display.set_mode((680,770))
clock = pygame.time.Clock()
FPS = 60


#Functions definition
def updateMario():
    screen.blit(c.marioImage, (c.mX, c.mY))

def updateScenario():
    screen.blit(c.scenarioImage, (0,0))
    screen.blit(c.donkeyKongImage, (c.dkX, c.dkY))
    if c.gameRunning == True:
        screen.blit(c.peachImage, (309,125))

def dkClimbingAnimation():
        if c.dkX < 320 and c.dkY > 175 :
            c.dkChangeX += 1
            c.donkeyKongImage = c.donkeyKongWalkingRightImage
        elif c.dkX > 320 and c.dkY > 175:
            c.dkChangeX = 0
            c.dkChangeY -= 1
            if c.supportDkAnimation == 0:
                c.donkeyKongImage = c.donkeyKongClimbingImage1
                c.supportDkAnimation =1
            elif c.supportDkAnimation == 1:
                c.donkeyKongImage = c.donkeyKongClimbingImage2
                c.supportDkAnimation = 0
        elif c.dkY < 175 and c.dkX >= 120:
            c.dkChangeY = 0 
            c.dkChangeX -= 1
            c.donkeyKongImage = c.donkeyKongWalkingLeftImage
        elif c.dkY < 175 and c.dkX < 120:
            c.donkeyKongImage = c.donkeyKongFacingFront
            c.gameRunning = True
            c.scenarioImage = c.levelToPlay
           
def moveBarrels():
    for i in range(0,4,1):
        if c.barrelY[i] == 238 and c.barrelX[i] < 430:
            c.barrelX[i] += 3
        elif (c.barrelY[i] < 312) and c.barrelX[i] >= 430:
            c.barrelY[i] += 2
        elif (c.barrelY[i] == 312) and c.barrelX[i] >= 100:
            c.barrelX[i] -= 3
        elif c.barrelX[i] < 100 and (c.barrelY[i] >= 312 and c.barrelY[i] <= 409):
            c.barrelY[i] += 2
        elif c.barrelY[i] == 410 and ( c.barrelX[i] <= 431 ):
            c.barrelX[i] += 3
        elif c.barrelX[i] > 431 and (c.barrelY[i] >= 409 and c.barrelY[i] <= 509):
            c.barrelY[i] += 2
        elif c.barrelY[i] == 510 and c.barrelX[i] > 100:
            c.barrelX[i] -= 3
        elif c.barrelX[i] <= 100 and (c.barrelY[i] >= 509 and c.barrelY[i] <= 609):
            c.barrelY[i] += 2
        elif c.barrelY[i] == 610 and c.barrelX[i] <= 431:
            c.barrelX[i] += 3
        elif c.barrelX[i] > 431 and (c.barrelY[i] >= 609 and c.barrelY[i] <= 709):
            c.barrelY[i] += 2
        elif c.barrelY[i] == 710 and c.barrelX[i] > 0:
            c.barrelX[i] -= 3
        elif c.barrelY[i] == 710 and c.barrelX[i] <= 0:
            c.barrelY[i] = 238
            c.barrelX[i] = -1000*(float(random.random()))

def drawLadders():
    screen.blit(c.ladder1, (c.ladderX[0], c.ladderY[0]))
    screen.blit(c.ladder2, (c.ladderX[1], c.ladderY[1]))
    screen.blit(c.ladder3, (c.ladderX[2], c.ladderY[2]))
    screen.blit(c.ladder4, (c.ladderX[3], c.ladderY[3]))
    screen.blit(c.ladder5, (c.ladderX[4], c.ladderY[4]))   

    
def updateBarrels():
    screen.blit(c.barrel1, (c.barrelX[0], c.barrelY[0]))
    screen.blit(c.barrel2, (c.barrelX[1], c.barrelY[1]))
    screen.blit(c.barrel3, (c.barrelX[2], c.barrelY[2]))
    screen.blit(c.barrel4, (c.barrelX[3], c.barrelY[3]))
    
def moveLeft():
    c.marioImage = c.marioRunningLeft
    c.peachImage = c.peachStanding
    c.mXChange = -5
    if c.mX < 0:
        c.mX -= c.mXChange
        c.mXChange = 0

def moveRight():
    c.marioImage = c.marioRunningRight
    c.peachImage = c.peachStanding
    c.mXChange = 5
    if c.mX > 630:
        c.mX -= c.mXChange
        c.mXChange = 0

def standRight():
    c.marioImage = c.marioStandingRight
    c.peachImage = c.peachCallingForHelp
    c.mXChange = 0
    
def standLeft():
    c.marioImage = c.marioStandingLeft
    c.peachImage = c.peachCallingForHelp
    c.mXChange = 0

def climbLadder():
    c.marioImage = c.marioClimbingLadder1
    c.mYChange -= 5
    
def standInLadder():
    c.marioImage = c.marioClimbingLadder1
    c.mYChange = 0
    
def jump():
    c.mY -= c.vel_y
    c.vel_y -= 1
    if c.vel_y < -9:
        c.jump = False
        c.vel_y = 9    

def obtainCoordinates():
    c.xMouse, c.yMouse = pygame.mouse.get_pos()

def goToFloorCoordinate():
    if (c.jump == False) and (c.climb == False):
        if c.mY < 630 and c.mY > 529:
            c.mY = 590
        elif c.mY < 529 and c.mY > 432:
            c.mY = 495
        elif c.mY < 432 and c.mY > 332:
            c.mY = 395
        elif c.mY < 332  and c.mY > 258:
            c.mY = 300
        elif c.mY < 259 and c.mY > 180:
            c.mY = 225
        
def printCoordinates():
    print("X:",c.xMouse,"Y:",c.yMouse) 
    print("Change:", c.mXChange) 
    print("Ladder status:", c.climb)
    
def checkClimbLadder():
    for i in range(0,4,1):
        if (c.mX > 103 and c.mX <138) and ( (c.mY > 500 and c.mY < 620) or (c.mY > 300 and c.mY < 420) ):
            c.climb = True
        elif (c.mX > 428 and c.mX < 461) and ( (c.mY > 620 and c.mY < 760 ) or (c.mY > 400 and c.mY < 530) or (c.mY > 230 and c.mY < 320) ):
            c.climb = True
        else:
            c.climb = False
            
def hitDK():
    if m.sqrt( (c.mX - c.dkX)**2 + (c.mY - c.dkY)**2 ) < 50:
        ap.addPoints("Puntajes.txt", c.currentGamePoints)
        ap.graphScore("Puntajes.txt")
        bf.quitGame()
        
def gameBegin():
    if (c.gameRunning == False) and c.intro == False:
        dkClimbingAnimation()
        pygame.time.delay(50)
        c.dkX += c.dkChangeX
        c.dkY += c.dkChangeY
        screen.fill(BLACK)          
        updateScenario()
        pygame.display.update()

def keyControlling():
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bf.quitGame()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        moveLeft()
                
                    elif event.key == pygame.K_d:
                        moveRight()
                    
                    elif event.key == pygame.K_w:
                        if c.climb == True:
                            climbLadder()
                            c.marioImage = c.marioClimbingLadder1
                        else:
                            c.jump = True
                            
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        standRight()
                        
                    elif event.key == pygame.K_a:
                        standLeft()
                        
                    elif event.key == pygame.K_w:
                        standInLadder()
                        
def gameFunctioning():
    if c.gameRunning == True:
            c.intro = True
            keyControlling()
            if c.jump == True:       
                jump()
            if ba.collide()==True:
                q.question()
                pygame.time.delay(1000)
            obtainCoordinates()
            pygame.time.delay(15)
            moveBarrels()
            checkClimbLadder()
            hitDK()
            goToFloorCoordinate()
            c.mX += c.mXChange
            c.mY += c.mYChange
            screen.fill(BLACK)
            updateScenario()
            drawLadders()
            updateMario()
            updateBarrels()
            pygame.display.update() 
            
def gameLoop():   
    #Game loop
    while True:
        time = clock.tick(FPS) / 1000
        gameBegin()
        gameFunctioning()
        
            
"""-------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------"""

gameLoop()
