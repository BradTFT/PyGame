import pygame
from sys import exit
pygame.init()
#import/initiate pygame

#display surface(window)
screen = pygame.display.set_mode((800,400))
#                     window width^    ^height of the window
#sets window name
pygame.display.set_caption('Game title here')
#set framerate
clock = pygame.time.Clock()

#create a surface(line 26)
testSurface = pygame.Surface((100, 200))
testSurface.fill('Red')

#draw all elements
#runs window forever
while True:
    #loops thru all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys exit to stop pygame error (video system not initalized)
            exit()

    #!code to display assets/objects

    #display surface(line 14)
    #coordinates are "reversed" (picture a grid graph)
    #origin point(0,0) is top left
    screen.blit(testSurface,(0,0))

    #puts everything onto the display
    pygame.display.update()
    #adds framerate to game
    clock.tick(60)

