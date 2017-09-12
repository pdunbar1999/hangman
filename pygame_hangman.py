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

global lives_remaining
lives_remaining = 0 #number of lives

def add_body_parts():
    global lives_remaining #global so it knows its a global
    lives_remaining += 1 #adds 1 whenever the function is called
    if lives_remaining == 1: #head
        pygame.draw.circle(gameDisplay, black, (634, 106), 50)
        pygame.display.update()
    if lives_remaining == 2: #body
        pygame.draw.line(gameDisplay, black, (634,156), (634,256), 5)
        pygame.display.update()
    if lives_remaining == 3:#left leg
        pygame.draw.line(gameDisplay, black, (634,256), (552, 352), 5)
        pygame.display.update()
        #start where body finished
    if lives_remaining == 4:#right leg
        pygame.draw.line(gameDisplay, black, (634,256), (716,352), 5)
        pygame.display.update()
        #start where body finished
    if lives_remaining == 5:#left arm
        pygame.draw.line(gameDisplay, black, (634,206), (584,206), 5)
        pygame.display.update()
        #start at middle of body
    if lives_remaining == 6:#right arm
        pygame.draw.line(gameDisplay, black, (634,206), (684, 206), 5)
        pygame.display.update()


def ask_for_letter():
    #checks what key was pressed down
    if event.key == pygame.K_a: #checks what key (K_s), s is key
        letter_check('a') #passes the pressed key into letter_check
    elif event.key == pygame.K_b:
        letter_check('b')
    elif event.key == pygame.K_c:
        letter_check('c')
    elif event.key == pygame.K_d:
        letter_check('d')
    elif event.key == pygame.K_e:
        letter_check('e')
    elif event.key == pygame.K_f:
        letter_check('f')
    elif event.key == pygame.K_g:
        letter_check('g')
    elif event.key == pygame.K_h:
        letter_check('h')
    elif event.key == pygame.K_i:
        letter_check('i')
    elif event.key == pygame.K_j:
        letter_check('j')
    elif event.key == pygame.K_k:
        letter_check('k')
    elif event.key == pygame.K_l:
        letter_check('l')
    elif event.key == pygame.K_m:
        letter_check('m')
    elif event.key == pygame.K_n:
        letter_check('n')
    elif event.key == pygame.K_o:
        letter_check('o')
    elif event.key == pygame.K_p:
        letter_check('p')
    elif event.key == pygame.K_q:
        letter_check('q')
    elif event.key == pygame.K_r:
        letter_check('r')
    elif event.key == pygame.K_s:
        letter_check('s')
    elif event.key == pygame.K_t:
        letter_check('t')
    elif event.key == pygame.K_u:
        letter_check('u')
    elif event.key == pygame.K_v:
        letter_check('v')
    elif event.key == pygame.K_w:
        letter_check('w')
    elif event.key == pygame.K_x:
        letter_check('x')
    elif event.key == pygame.K_y:
        letter_check('y')
    elif event.key == pygame.K_z:
        letter_check('z')       
    
def letter_check(letter):
    guess = letter #whatever the key specified is
    check = 0 #checks if at least the letter is in the word once
    for x in range(0,len(word)):
        if word[x] == guess: 
            del string_word[x]
            string_word.insert(x, guess)
            check += 1
    if check == 0: #if its 0, means the letter wasn't right
        add_body_parts() #adds a body part


def display_word(): #displays the incompleted word at the bottom
    q = pygame.font.SysFont('none', 100) #specifes the font wanted and the font size
    x = q.render('  '.join(string_word), True, white) #.join turns the string into a list with spaces inbetween it.
    gameDisplay.blit(x, (100,500)) #displays the word onto the screen
    

gameDisplay.blit(basePole, (0,0))
#displays background image once

gameExit = False

word = 'mother' #TESTING PURPOSES ONLY
string_word = []#reserving an empty list to put the word in

for x in range(0,len(word)):
    string_word.append("_")
    #adds _ to however many letters are needed

while not gameExit: #while True
    for event in pygame.event.get():
        print(event) #prints events in the game

        if event.type == pygame.QUIT: #checks if we want to quit
            gameExit = True
            pygame.QUIT
            quit()

        if event.type == pygame.KEYDOWN:#checks if key is pressed down
            ask_for_letter()


    if lives_remaining == 6:
        print("You lost")
        gameExit = True
        pygame.QUIT
        quit()
            
               
    display_word()
    pygame.display.update() #updates the screen so we can see it

    
