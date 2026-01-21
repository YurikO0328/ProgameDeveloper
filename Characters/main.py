import pygame
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((600,400))

x=300
y=200
speed=1

running=True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys=pygame.key.get_pressed()

    if keys [K_UP]:
        y== speed
    if keys[K_DOWN]:
        y+=speed
    if keys[K_LEFT]:
        x-=speed
    if keys[K_RIGHT]:
        x+=speed

    pygame.draw.rect(screen, (255,0,0), (x,y,40,40))
    pygame.display.update()

pygame.quit()
