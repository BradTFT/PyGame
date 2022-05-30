import pygame
from sys import exit
pygame.init()
#import/initiate pygame

#display surface(window)
screen = pygame.display.set_mode((800,400))
#                     window width^    ^height of the window

#draw all elements
#runs window forever
while True:
   #loops thru all events
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             #sys exit to stop pygame error (video system not initalized)
             exit()
     #puts everything onto the display
     pygame.display.update()