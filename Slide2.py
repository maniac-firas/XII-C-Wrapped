import pygame, time

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Loading Original Image    
og = pygame.image.load('Images/Pallete2.png').convert_alpha()
imgd = pygame.transform.scale(og, (50, 200))
imgu = pygame.transform.rotate(imgd, 180)

#Loading Texts
SfPro = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 30)
SfLarge = pygame.font.Font('Fonts/SpotifyMix-Black.ttf', 33)
def createtext(message, size, color, x, y):
    SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', size)
    txt = SfRegular.render(message, True, color)
    txt_rect = txt.get_rect()
    txt_rect.centerx, txt_rect.centery = x, y
    txt_surf = txt.copy()
    alpha_surf = pygame.Surface(txt.get_size(), pygame.SRCALPHA)
    alpha = 0
    return txt_surf, txt_rect, alpha_surf, alpha

lasttxt_surf, lasttxt_rect, alpha_surf, alpha = createtext('And every ~minute~ was worth it...', 28, '#a6a6a6', 350, 450)

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = SfRegular.render('-Click Space-', True, 'white')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

#Functions
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

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/LoseMyself.wav')

def S2(screen):
    global alpha
    pygame.mixer.music.play(-1)
    # Drawing fade in and out of first pair
    pos1, pos2 = -200, 800
    pl1, pl2 = 0, 600
    fps=720
    while pos1 <= pl1 and pos2 >= pl2:
        screen.fill("#000000")
        x=0
        for k in range(14):
            screen.blit(imgd, (x, pos1))
            x+=50
        x=0
        for k in range(14):
            screen.blit(imgu, (x, pos2))
            x+=50               
        pos1+=1
        pos2-=1
        pygame.display.flip()
        clock.tick(fps)
        fps=max(360, fps-2)

    # Drawing fade in and out of first pair and second pair as well
    pos1, pos2 = 0, 600
    pl1, pl2 = 200, 400
    while pos1 <= pl1 and pos2 >= pl2:       

        # Drawing Second pair
        x=0
        for k in range(14):
            screen.blit(imgd, (x, pos1))
            x+=50
        x=0
        for k in range(14):
            screen.blit(imgu, (x, pos2))
            x+=50                
        pos1+=1
        pos2-=1
        pygame.display.flip()
        clock.tick(fps)
        fps=max(150, fps-1)

        # Redrawing top and bottom
        x=0
        for k in range(14):
            screen.blit(imgd, (x, 0))
            x+=50
        x=0
        for k in range(14):
            screen.blit(imgu, (x, 600))
            x+=50

    #Whole picture
    def blitwhole(n=[]): 
        x = 0
        for k in range(14): 
            if k not in n:  screen.blit(imgd, (x, 0))
            x+=50
        x = 0
        for k in range(14): 
            if k not in n:  screen.blit(imgu, (x, 600))
            x+=50
        x = 0
        for k in range(14): 
            if k not in n:  screen.blit(imgu, (x, 400))
            x+=50
        x = 0
        for k in range(14):
            if k not in n:  screen.blit(imgd, (x, 200))
            x+=50

    def movewhole(n=[], leng=1):
        a  = 1
        blitwhole(n)
        fps=720
        while True:
            screen.blit(imgd, (n[leng-2]*50, 0-a))
            screen.blit(imgd, (n[leng-2]*50, 200-a))
            screen.blit(imgu, (n[leng-2]*50, 400+a))
            screen.blit(imgu, (n[leng-2]*50, 600+a))
            screen.blit(imgd, (n[leng-1]*50, 0-a))
            screen.blit(imgd, (n[leng-1]*50, 200-a))
            screen.blit(imgu, (n[leng-1]*50, 400+a))
            screen.blit(imgu, (n[leng-1]*50, 600+a))
            pygame.display.flip()
            clock.tick(fps)
            fps-=15
            if a<=n[leng-2]*50+50:  a+=2
            else:   break
        return a

    #Redrawing Screen I
    pygame.time.delay(200)
    blitwhole()
    pygame.display.flip()
        
    #Central Parts
    m=list()
    pos=list()
    for i in range(6):    
        m.extend([6-i, 7+i])    
        item = movewhole(m, len(m))
        pos.append(item)
    del m
    pos.append(0)

    #Redrawing Screen II
    screen.fill('#000000')
    def relwhole(a=0):
        for i in range(7):
            screen.blit(imgd, ((6-i)*50, 200-pos[i]-a))
            screen.blit(imgd, ((7+i)*50, 200-pos[i]-a))

        for i in range(7):
            screen.blit(imgu, ((6-i)*50, 400+pos[i]+a))
            screen.blit(imgu, ((7+i)*50, 400+pos[i]+a))

        for i in range(3):
            screen.blit(imgd, ((i)*50, 0-pos[6-i]-a))
            screen.blit(imgd, ((13-i)*50, 0-pos[6-i]-a))
            screen.blit(imgu, ((i)*50, 600+pos[6-i]+a))
            screen.blit(imgu, ((13-i)*50, 600+pos[6-i]+a))
        
        pygame.display.flip()
        clock.tick(30)

    #Complete Background change
    bg = pygame.image.load("Images/P2bg.png")
    bg = pygame.transform.scale(bg, (700, 800))
    bg = pygame.transform.rotate(bg, 180)
    screen.blit(bg, (0, 0))
    pygame.time.delay(100)

    #Animation starts from here

    #Message printing
    z = 1
    i, n = 0, 1
    msg = ['We', 'We have', 'We have been', 'We have been together', 'We have been together for']
    while i <= 4:
        #Mesmerizing Movement
        screen.blit(bg, (0, 0))

        #Typewriter animation
        txt = SfPro.render(msg[i], True, '#ffffff')
        txt_rect = txt.get_rect()
        txt_rect.centerx, txt_rect.centery = 350, 350
        screen.blit(txt, txt_rect)
        n+=1
        if n % 13 == 0:  i+=1

        #Mesmerizing Movement
        relwhole(z)
        z+=1
        if z>=200:   z=0

    #Bits Printing
    i, n = 0, 1
    bits = ['10 months', '38 weeks', '289 days', '6,936 hours', '4,16,160 minutes']
    while i <= 4:

        #Mesmerizing Movement
        screen.blit(bg, (0, 0))

        #Typewriter animation
        txt = SfPro.render(msg[4], True, '#ffffff')
        screen.blit(txt, txt_rect)

        #Displaying Time spent
        timetxt = SfLarge.render(bits[i], True, '#ffffff')
        timetxt_rect = timetxt.get_rect()
        timetxt_rect.centerx, timetxt_rect.centery = 350, 400
        screen.blit(timetxt, timetxt_rect)
        n+=1
        if n % 12 == 0:  i+=1

        #Mesmerizing Movement
        relwhole(z)
        z+=1
        if z>=200:   z=0

    #Last Text Fade In
    while alpha < 255:

        #Mesmerizing Movement
        screen.blit(bg, (0, 0))

        #Texts
        txt = SfPro.render(msg[4], True, '#ffffff')
        screen.blit(txt, txt_rect)
        timetxt = SfLarge.render(bits[4], True, '#ffffff')
        screen.blit(timetxt, timetxt_rect)

        #Last text
        fadein(screen, alpha, alpha_surf, lasttxt_surf, lasttxt_rect)
        alpha = min(alpha+2, 255)

        #Mesmerizing Movement
        relwhole(z)
        z+=1
        if z>=200:   z=0

    #Loop
    on = True
    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on = False

        
        screen.blit(bg, (0, 0))

        #Texts
        screen.blit(txt, txt_rect)
        screen.blit(timetxt, timetxt_rect)
        screen.blit(lasttxt_surf, lasttxt_rect)
        screen.blit(cmd, cmd_rect)

        #Mesmerizing Movement
        relwhole(z)
        z+=1
        if z>=200:   z=0

        

    screen.fill('#000000')
    end = False
    while not(end):
        screen.fill('#000000')
        relwhole(z)
        z+=5

        pygame.display.flip()
        clock.tick(720)

        if z >= 400:
            end = True

    pygame.mixer.music.stop()

S2(screen)