import pygame
from pygame.locals import *
from time import *
pygame.init()

screen=pygame.display.set_mode((600,600))
player_x=200
player_y=200

keys=[False]
image1=pygame.image.load("rocket.png")
background=pygame.image.load("spacebg.png")


while True:
    screen.blit(background,(0,0))
    screen.blit(image1,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0]=True

        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False

    if keys[0]:
        if player_y > 0:
            player_y-=7



    sleep(0.05)

