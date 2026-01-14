import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=300

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birtday Greeting Card")

img=pygame.image.load("firstbground.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while(True):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    font=pygame.font.SysFont("Times New Roman", 72)
    text=font.render("Happy",True, (0,0,0))
    text2=font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    pygame.time.delay(4000)

    image2=pygame.image.load("backgroundtwo.jpg")
    font2=pygame.font.SysFont("Ariel",36)
    text3=font2.render("Wish You A Bright Future Ahead.",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image2,(0,0))
    display_surface.blit(text3,(30,30))
    pygame.display.update()
    pygame.time.delay(4000)

    image3=pygame.image.load("backgroundthree.jpg")
    display_surface.fill((255,255,255))
    display_surface.blit(image3,(0,0))
    pygame.display.update()
    pygame.time.delay(4000)