import pygame
import os 
pygame.font.init()
pygame.mixer.init()
WIDTH=900
HEIGHT=500
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invader")#naming the actual tab
WHITE=(255,255,255)#makes colors in variables so its easy to use
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)#finds the middle of the game

BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))#takes sound file
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
BULLET_HIT_SOUND.set_volume(0.5)#sets volume
BULLET_FIRE_SOUND.set_volume(0.5)
HEALTH_FONT=pygame.font.SysFont("comicans", 40)#font/text for the components of the game
WINNER_FONT=pygame.font.Sysfont("comicans", 100)
FPS=60 #speed of he game
VEL=5 #spaceships move 5 pixels/speed os spaceship
BULLET_VEL=7 #bullets speed 
MAX_BULLETS=3 #3 bullets max can be fired at a time
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40 #size of the spaceships

YELLOW_HIT = pygame.USEREVENT + 1#pygame.USEREVENT is a custome event
RED_HIT = pygame.USEREVENT + 2 #the =1/2 is the order
YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))#loads the image
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))#loads the image
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 270)
SPACE=pygame.transform.scale(pygame.image.load(os.path.join('Asstes', 'space.png')),(WIDTH, HEIGHT))
#*Above, loads and make background

def draw_window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):#gets everything you need
    window.blit(SPACE, (0,0))#Pastes the bg
    pygame.draw.rect(window, BLACK, BORDER)#bg color
    red_health=HEALTH_FONT.render("Health: "+ str(red_health), True, WHITE)#"health bar" of the ships
    yellow_health=HEALTH_FONT.render("Health: "+ str(yellow_health), True, WHITE)
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10,10))#places the font/text in the right place
    window.blit(yellow_health_text, (10,10))
    window.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))#############################?
    window.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(window, RED, bullet)##################################?

    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW, bullet)#########################################?

    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x-=VEL#going left 
    
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width < BORDER.X:
        yellow.x+=VEL#going right

    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y-=VEL#going up
    
    if keys_pressed[pygame.K_s] and yellow.y + yellow.width < HEIGHT-15:
        yellow.y+=VEL#goind down

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x >  BORER.x + BORDER.width:
        red.x-=VEL#going left 
    
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width < WIDTH:
        red.x+=VEL#going right

    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y-=VEL#going up
    
    if keys_pressed[pygame.K_DOWN] and red.y + red.width < HEIGHT-15:
        red.y+=VEL#goind down

def handle_bullets(yellow_bullets, red_bullets, yellow,red):
    for bullet in yellow_bullets:
        bullet.x == BULLET_VEL

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))##########################?
            yellow.bullets.remove(bullet)#reduce ammo




