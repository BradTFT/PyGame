import pygame
from sys import exit
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080,720))
black = 0,0,0

backgroundSurf = pygame.image.load('assets/graphics/background.png').convert()

font_ = pygame.font.Font('assets/fonts/Blippo Bold.ttf', 100)
text1 = font_.render('1', False, 'White')
text1Rect = text1.get_rect(center = (300,55))

text2 = font_.render('2', False, 'White')
text2Rect = text2.get_rect(center = (780, 55))

player1Surf = pygame.image.load('assets/graphics/player1.png').convert_alpha()
player1Rect = player1Surf.get_rect()

player2Surf = pygame.image.load('assets/graphics/player2.png').convert_alpha()
player2Rect = player2Surf.get_rect()

lineSurf = pygame.image.load('assets/graphics/line.png').convert()
lineRect = lineSurf.get_rect()

topLineSurf = pygame.image.load('assets/graphics/top.png').convert()
topRect = topLineSurf.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()


    screen.blit(backgroundSurf, (0,0))

    screen.blit(player1Surf, player1Rect)
    screen.blit(player2Surf,player2Rect)
    screen.blit(lineSurf, lineRect)
    screen.blit(topLineSurf, topRect)

    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    pygame.display.update()
    clock.tick(60)