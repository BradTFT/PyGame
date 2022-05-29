import pygame
from sys import exit
pygame.init()
#!view docs: python -m pygame.docs
#!import/initiate pygame

#!display surface(window)
screen = pygame.display.set_mode((800,400))
#                     window width^    ^height of the window
#sets window name
pygame.display.set_caption('Game title here')
#set framerate
clock = pygame.time.Clock()

#!fonts
test_font = pygame.font.Font('pygame asset zip/font/Pixeltype.ttf', 50)
#                   font type^,     ^ font size

#!import surfaces
sky_surface = pygame.image.load('pygame asset zip/graphics/Sky.png').convert()
ground_surface = pygame.image.load('pygame asset zip/graphics/ground.png').convert()
text_surface = test_font.render('text',False, 'Black' ).convert()
#                              text^    ^AA     ^color

snail_surface = pygame.image.load('pygame asset zip/graphics/snail/snail1.png').convert_alpha()
snail_x = 600

snail_rect = snail_surface.get_rect(midbottom = (150,300))
#! convert alpha is == to png (removes white and black bgrd)
player_surface = pygame.image.load('pygame asset zip/graphics/Player/player_walk_1.png').convert_alpha()

#!create a rectangle:
player_rect = player_surface.get_rect(midbottom = (80,300))
#marks which point of the rectange needs to be touching whatever coordinate (idk a better way to explain it)
#rects will be easier with classes 

#draw all element
#runs window forever
while True:
    #loops thru all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #sys exit to stop pygame error (video system not initalized)
            exit()

    #!code to display assets/objects


    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(350,50))

    #!blit with the rectangle
    screen.blit(player_surface,player_rect)
    #moves player same way as line 56
    player_rect.left += 1
    #!animated:
    #every second updates x position by 1
    screen.blit(snail_surface,snail_rect)
    snail_rect.left += 1

    #if snail X pos gets further than coord -100 it returns to coord 800
    '''
    if snail_x < -100:
        snail_x = 800
    
    screen.blit(snail_surface,(snail_x,200))
    '''


    #puts everything onto the display
    pygame.display.update()
    #adds framerate to game
    clock.tick(60)
