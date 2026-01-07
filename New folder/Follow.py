import pygame
pygame.init()

screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Circle follow the mouse")

WHITE=(255,255,255)
BLUE=(0,128,155)

running=True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    mouse_x,mouse_y = pygame.mouse.get_pos()
    pygame.draw.circle(screen, BLUE, (mouse_x,mouse_y), 30)

    pygame.display.update()

pygame.quit()