import pygame
pygame.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Mouse Click Sample")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            print("Mouse Down Pressed")

pygame.quit()