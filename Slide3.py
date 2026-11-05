import pygame
from pygame.locals import *
from math import cos, radians

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Load Images
p1 = pygame.image.load('Images/Pallete3-1.png').convert()
p2 = pygame.image.load('Images/Pallete3-2.png').convert()
p3 = pygame.image.load('Images/Pallete3-3.png').convert()
bg3 = pygame.image.load('Images/Bg3.png').convert()
p1 = pygame.transform.scale(p3, (240, 800))
p2 = pygame.transform.scale(p2, (240, 800))
p3 = pygame.transform.scale(p1, (240, 800))
bg3 = pygame.transform.scale(bg3, (700, 800))

#Loading Texts
sta = ["Sleeper of XII-C", "Latecomer of XII-C", "Singer of XII-C", "Artist of XII-C", "Dancer of XII-C", "Presentee of XII-C", "Absentee of XII-C", "Non-Stop Talker of XII-C", "Co-ordinator of XII-C", "Silent person of XII-C", "Computer expert of XII-C", "Weirdest Kid of XII-C", "Sigma of XII-C",  "Fashionista of XII-C", "Diva of XII-C", "Enth pottatharam parnalum vishwasikkum", "Debate King", "Vaaya thoranal chali veruollu",  "Best Nickname given by Sathya Mam", "Best Class Teacher"]
l = len(sta)
Cat=[]
Cord=[]
SfPro = pygame.font.Font('Fonts/SpotifyMix-BoldItalic.ttf', 30)
for i in range(l):
    temp = SfPro.render(sta[i], True, '#ffffff')
    rect = temp.get_rect()
    rect.centerx = 360
    rect.centery = -100
    Cat.append(temp)
    Cord.append(rect)

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = SfRegular.render('-Click Space-', True, 'white')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

#Load card front images
Fs = []
def CardFront(name):
    F = pygame.image.load('Photos/'+name).convert_alpha()
    F = pygame.transform.scale(F, (330, 450))
    Fs.append(F)

CardFront('Card1.png')
CardFront('Card2.png')
CardFront('Card3.png')
CardFront('Card4.png')
CardFront('Card5.png')
CardFront('Card6.png')
CardFront('Card7.png')
CardFront('Card8.png')
CardFront('Card9.png')
CardFront('Card10.png')
CardFront('Card11.png')
CardFront('Card12.png')
CardFront('Card13.png')
CardFront('Card14.png')
CardFront('Card15.png')
CardFront('Card16.png')
CardFront('Card17.png')
CardFront('Card18.png')
CardFront('Card19.png')
CardFront('Card20.png')


#Background and Rocket
bg = pygame.image.load('Images/NightSky.jpeg').convert_alpha()
bg1 = pygame.transform.scale(bg, (700, 800))
bg1 = pygame.transform.rotate(bg1, 180)
rocket = pygame.image.load('Images/rocket.png').convert_alpha()
rocket = pygame.transform.scale(rocket, (64, 104))

#Card flip
back = pygame.image.load('Images/Back.png').convert_alpha()
back = pygame.transform.scale(back, (330, 450))

def flipCard(angle, front):
    global back
    cardSurface = pygame.Surface((330, 450), SRCALPHA) # creates surface

    w = 330 # Width of card
    cardSurface.blit(front, (0, 0)) # Blits the front of the card (white side)

    if angle < 90: # If the card is still turned over (or the back is still visible)
        cardSurface.blit(back, (0, 0)) # Draw back of card (red side)

        if angle > 0: # If not completely faced down
            # rotate
            w = cos(radians(angle)) * 330 # Work out the new width based on the angle and original width
            cardSurface = pygame.transform.scale(cardSurface, (int(w), 450)) # Scale the width

    elif angle == 90: # If exactly horizontal
        cardSurface.blit(back, (0, 0))
        w = 1 # DIsplay the back in a 1 pixel width surface
        cardSurface = pygame.transform.scale(cardSurface, (int(w), 450))

    elif angle > 90:
        cardSurface.blit(front, (0, 0))
        if angle < 180: # Same as before
            # rotate
            w = cos(radians(180 - angle)) * 330
            cardSurface = pygame.transform.scale(cardSurface, (int(w), 450))

    px = 355 - int(w/2)
    screen.blit(cardSurface, (px, 180))

def flip(front, Category, rect):
    z=-350
    fps=700
    while z<=190: 
        screen.blit(bg3, (0, 0))
        screen.blit(back, (z, 180))
        pygame.display.flip()
        clock.tick(fps)
        z+=1
        fps-=1

    u=-100
    fps=300
    z-=1
    flip = False
    while not(flip):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        flip = True

        
        screen.blit(bg3, (0, 0))
        screen.blit(back, (z, 180))
        screen.blit(Category, rect)
        screen.blit(cmd, cmd_rect)
        if u<= 100: rect.centery += 1
        u += 1
        pygame.display.flip()
        clock.tick(fps)
        fps-=1

    rect.centery -= 1

    d = 1
    speed = 3
    a = 0
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        over = False

        clock.tick(60)
        screen.blit(bg3, (0, 0))
        screen.blit(Category, rect)

        a += d * speed # Increases/Decreases angle
        if a >= 180: # If fully revealed
            screen.blit(cmd, cmd_rect)
        elif a <= 0: # If fully turned-over
            a = 0
            d = 1 # Switch direction

        flipCard(a, front)
        pygame.display.flip()

    fps=700
    while z<=700: 
        screen.blit(bg3, (0, 0))
        screen.blit(front, (z, 180))
        screen.blit(Category, rect)
        pygame.display.flip()
        clock.tick(fps)
        z+=1
        rect.centery-=1
        fps-=1

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/UpAndUp.wav')

#Draw Background
def S3():
    pygame.mixer.music.play(-1)
    n = 0
    fps = 800
    while n <= 700:
        screen.blit(p1, (480, -700+n))
        screen.blit(p2, (240, 700-n))
        screen.blit(p3, (0, -700+n))
        n+=1
        pygame.display.flip()
        clock.tick(fps)
        fps = max(360, fps-1)

    pygame.time.delay(1000)

    screen.blit(bg3, (0, 0))
    pygame.display.flip()

    pygame.time.delay(1000)

    for i in range(l):
        flip(Fs[i], Cat[i], Cord[i])

    #Moving Sideways
    on = True
    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on = False

    
    end = False
    a=800
    z=0
    fps=1700
    while not(end):
        screen.blit(bg1, (0, 0))
        screen.blit(bg3, (0, z))
        screen.blit(rocket, (350-32, a))
        pygame.display.flip()
        clock.tick(fps)
        a = max(a-4, (400-52))
        z+=4
        fps-=1

        if z > 800:
            end = True
    
    pygame.mixer.music.stop()

S3()