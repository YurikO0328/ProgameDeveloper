import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=500

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birtday Greeting Card")

image1=pygame.transform.scale(pygame.image.load("firstbground.jpg"),(WIDTH,HEIGHT))
image2=pygame.transform.scale(pygame.image.load("backgroundtwo.jpg"),(WIDTH,HEIGHT))
image3=pygame.transform.scale(pygame.image.load("backgroundthree.jpg"),(WIDTH,HEIGHT))


font1=pygame.font.SysFont("Times New Roman", 72)
font2=pygame.font.SysFont("Arial", 36)

text1= font1.render("Happy", True, (0,0,0))
text2=font1.render("Birthday", True, (0,0,0))
text3=font2.render("Wish you a bright future ahead", True, (0,0,0))

screen=1
last_time=pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    current_time=pygame.time.get_ticks()

    if screen==1:
        display_surface.blit(image1,(0,0))
        display_surface.blit(text1,(210,180))
        display_surface.blit(text2,(160,240))

        if current_time-last_time>4000:
            screen=2
            last_time=current_time
    elif screen==2:
         display_surface.blit(image2,(0,0))
         display_surface.blit(text2,(30,30))


         if current_time - last_time > 4000:
             screen=3
             last_time=current_time

    elif screen == 3:
        display_surface.blit(image3,(0,0))

        if current_time - last_time > 4000:
            screen=1
            last_time=current_time

    pygame.display.update()

         





