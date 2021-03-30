"""
Created on Tue Oct 27 17:21:27 2020
"""

import pygame
import math
import random
import sys



#Game SetUp
pygame.init()
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,720))

#Game variables
bg_surface = pygame.image.load('Assets/menu_bg.jpeg').convert()
#floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0
game_active = True

"""
BASIC FUNCTION DEFINITION
"""
def quitGame(): #Closes game and logs a message about it
    print("Cerrando juego")
    pygame.quit()
    sys.exit()

def playGame():
    print("PlayGame")
    

def showScore():
    print("ShowScore")
    
def mainMenu():
    while True:
        screen.blit(bg_surface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    playGame()
                if event.key == pygame.K_q and game_active:
                    quitGame()
                if event.key == pygame.K_s and game_active:
                    showScore()
            
            
            
"""
Functionality
"""
mainMenu()