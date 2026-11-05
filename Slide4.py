import pygame
import time

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#loading texts
def createtext(message, size, color, x, y):
    SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', size)
    txt = SfRegular.render(message, True, color)
    txt_rect = txt.get_rect()
    txt_rect.centerx, txt_rect.centery = x, y
    txt_surf = txt.copy()
    alpha_surf = pygame.Surface(txt.get_size(), pygame.SRCALPHA)
    alpha = 0
    return txt_surf, txt_rect, alpha_surf, alpha

def fadein(screen, alpha, alpha_surf, text, rect):
    txt_surf = text.copy()
    if alpha < 255:
        # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = min(alpha+2, 255)
        # Don't modify the original text surf.
        # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
        # To make the text surface transparent, blit the transparent
        # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(txt_surf, rect)

txt1_surf, txt1_rect, alpha1_surf, alpha1 = createtext('Let\'s take a walk down memory lane.', 28, '#ffffff', 350, 500)


#Loading Images
bg = pygame.image.load('Images/NightSky.jpeg').convert_alpha()
bg1 = pygame.transform.scale(bg, (700, 800))
bg1 = pygame.transform.rotate(bg1, 180)
brect1 = bg1.get_rect(x=0, y=0)
bg = pygame.image.load('Images/NightSky1.jpeg').convert_alpha()
bg2 = pygame.transform.scale(bg, (700, 800))
brect2 = bg2.get_rect(x=0, y=-800)
tran = pygame.image.load('Images/Bg4.png').convert_alpha()
tran = pygame.transform.scale(tran, (800, 1000))
trect = tran.get_rect(x=0, y=-1000)

rocket = pygame.image.load('Images/rocket.png').convert_alpha()
rocket = pygame.transform.scale(rocket, (64, 104))

#Loading Planets
planets=[]
rects=[]
def loadplanet(image, reverse = False):
    temp = pygame.image.load('Photos/'+image).convert_alpha()
    temp = pygame.transform.scale(temp, (600, 440))
    rect = temp.get_rect()
    if reverse: rect.x, rect.y = 300, -500
    else:   rect.x, rect.y = -200, -500
    planets.append(temp)
    rects.append(rect)

loadplanet('planet1.png')
loadplanet('planet2.png')
loadplanet('planet3.png', True)
loadplanet('planet4.png')
loadplanet('planet5.png')
loadplanet('planet6.png', True)

#loading music
pygame.mixer.init()
pygame.mixer.music.load('Music/Kabira.wav')

#Loop
def S4(screen):
    global alpha1

    pygame.mixer.music.play(0)

    screen.blit(bg1, brect1)
    screen.blit(rocket, (350-32, 400-52))
    pygame.display.flip()
    pygame.time.delay(500)

    while alpha1 < 255:
        screen.blit(bg1, brect1)
        screen.blit(bg2, brect2)
        brect1.y += 1
        brect2.y += 1
        if brect1.y == 800: brect1.y=-800
        if brect2.y == 800: brect2.y=-800

        fadein(screen, alpha1, alpha1_surf, txt1_surf, txt1_rect)
        alpha1 = min(alpha1+1, 255)

        screen.blit(rocket, (350-32, 400-52))
        pygame.display.flip()
        clock.tick(120)

    st = time.time()
    while alpha1 > 0:
        screen.blit(bg1, brect1)
        screen.blit(bg2, brect2)
        brect1.y += 1
        brect2.y += 1
        if brect1.y == 800: brect1.y=-800
        if brect2.y == 800: brect2.y=-800

        et=time.time()
        t = et-st
        if t >= 3:  
            fadein(screen, alpha1, alpha1_surf, txt1_surf, txt1_rect)
            alpha1 = max(alpha1-1, 0)
        else:
            screen.blit(txt1_surf, txt1_rect)

        screen.blit(rocket, (350-32, 400-52))
        pygame.display.flip()
        clock.tick(200)

    i = 0
    while i < len(planets):
        screen.blit(bg1, brect1)
        screen.blit(bg2, brect2)
        brect1.y += 1
        brect2.y += 1
        if brect1.y == 800: brect1.y=-800
        if brect2.y == 800: brect2.y=-800

        screen.blit(rocket, (350-32, 400-52))

        surf, rect = planets[i], rects[i]
        screen.blit(surf, rect)
        rect.y += 1
        rects[i] = rect
        if rect.y >= 800:   i+=1
        pygame.display.flip()
        clock.tick(250)
        
    end = False
    while not(end):
        screen.blit(bg1, brect1)
        screen.blit(bg2, brect2)
        brect1.y += 1
        brect2.y += 1
        if brect1.y == 800: brect1.y=-800
        if brect2.y == 800: brect2.y=-800

        screen.blit(rocket, (350-32, 400-52))

        screen.blit(tran, trect)
        trect.y += 1
        pygame.display.flip()
        clock.tick(300)

        if trect.y >= 0:    end = True
    pygame.mixer.music.stop()

S4(screen)