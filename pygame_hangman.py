import random
import pygame
import time

pygame.init()

#Drawing variables examples
#pygame.draw.line(gameDisplay, black, (100,150), (200,300), 5)
#                 where display, color, start, end,      thickness
#Drawing circles
#pygame.draw.circle(gameDisplay, black, (300,400), 75)
#                   where,       color, center,     radius

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#Colors we will use

display_width = 800
display_height = 600
#dimesnsions

basePole = pygame.image.load('/Users/peterdunbar/hangman/pictures_pygame/hangmanPole.png')
basePole = pygame.transform.scale(basePole, (800,500))
#loads the image, left the bottom 100 pixels for the word

gameDisplay = pygame.display.set_mode((display_width, display_height))
#Now, gameDisplay is the screen we will be working with


def add_body_parts():
    if count == 1: #head
        pygame.draw.circle(gameDisplay, black, (634, 106), 50)
        pygame.display.update()
    if count == 2: #body
        pygame.draw.line(gameDisplay, black, (634,156), (634,256), 5)
        pygame.display.update()
    if count == 3:#left leg
        pygame.draw.line(gameDisplay, black, (634,256), (552, 352), 5)
        pygame.display.update()
        #start where body finished
    if count == 4:#right leg
        pygame.draw.line(gameDisplay, black, (634,256), (716,352), 5)
        pygame.display.update()
        #start where body finished
    if count == 5:#left arm
        pygame.draw.line(gameDisplay, black, (634,206), (584,206), 5)
        pygame.display.update()
        #start at middle of body
    if count == 6:#right arm
        pygame.draw.line(gameDisplay, black, (634,206), (684, 206), 5)
        pygame.display.update()
    


gameDisplay.blit(basePole, (0,0))
#displays background image once

count = 0
gameExit = False

while not gameExit: #while True
    for event in pygame.event.get():
        print(event) #prints events in the game

        if event.type == pygame.QUIT: #checks if we want to quit
            gameExit = True
            pygame.QUIT
            quit()

        if event.type == pygame.KEYDOWN:#checks if key is pressed down
            if event.key == pygame.K_p: #checks what key (K_s), s is key
                
                count = count + 1
                add_body_parts()
                    
                

    pygame.display.update() #updates the screen so we can see it

    
