import pygame, time

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Loading Texts
def createtext(message, size, color, x, y):
    SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', size)
    txt = SfRegular.render(message, True, color)
    txt_rect = txt.get_rect()
    txt_rect.centerx, txt_rect.centery = x, y
    txt_surf = txt.copy()
    alpha_surf = pygame.Surface(txt.get_size(), pygame.SRCALPHA)
    alpha = 0
    return txt_surf, txt_rect, alpha_surf, alpha

txt1_surf, txt1_rect, alpha1_surf, alpha1 = createtext('It\'s the End of the Year.', 30, '#ffffff', 350, 380)
txt2_surf, txt2_rect, alpha2_surf, alpha2 = createtext('Let\'s take a look back.', 28, '#a6a6a6', 350, 420)

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = SfRegular.render('-Click Space-', True, 'white')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

#Functions
def rotate(im, angle, pivot):
    image = pygame.transform.rotate(im, angle)
    rect = image.get_rect()
    rect.center = pivot
    screen.blit(image, rect)

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

#Loading Background 
bg = pygame.image.load('Images/Bg1.png').convert()
bg = pygame.transform.scale(bg, (700, 800))

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/Maki.mp3')

stxt_surf, stxt_rect, salpha_surf, salpha = createtext('To start and switch between slides, press SPACE', 20, '#ffffff', 350, 400)

#Slide as functions
def S1(screen):
    global alpha1, alpha2, salpha
    
    on = True
    while on:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        on = False

        screen.fill('#000000')
        fadein(screen, salpha, salpha_surf, stxt_surf, stxt_rect)
        salpha = min(salpha+2, 255)
        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.play(-1)
    screen.blit(bg, (0, 0))
    pygame.display.flip()
                    #Zooming In Effect
    P1 = pygame.image.load('Images/Pallete1.png').convert_alpha()
    P1 = pygame.transform.scale(P1, (7, 8))
    time.sleep(2)
    P1 = pygame.transform.flip(P1, True, False)
    s, a = 1, 1
    while s < 20:
        screen.blit(bg, (0, 0))
        img = pygame.transform.rotozoom(P1, a, s)
        screen.blit(img, ((WIDTH-img.get_width())/2 , (HEIGHT-img.get_height())/2))
        pygame.display.flip()
        a+=5
        s+=0.5
        clock.tick(50)
    
                    #Placeholder 
    P1 = pygame.image.load('Images/Pallete1.png').convert_alpha()
    img = pygame.transform.scale(P1, (140, 160))

                    #Rotozoom towards different directions
    s, a = 1, 1
    y1, y2 = 0, 0
    while y1>=-570 or y2<=570:
        screen.blit(bg, (0, 0))
        imag1 = pygame.transform.rotozoom(img, a, s)        
        imag2 = pygame.transform.rotozoom(img, a, s)        
        screen.blit(imag1, ((WIDTH-imag1.get_width())/2, (HEIGHT-imag1.get_height())/2 + y1))
        screen.blit(imag2, ((WIDTH-imag2.get_width())/2, (HEIGHT-imag2.get_height())/2 + y2))
        pygame.display.flip()
        clock.tick(30)
        if a < 430:  a+=3
        y1-=15
        y2+=15
        if s < 4:   s+=0.1

                    #To get pivot so as to rotate around
    ir1 = imag1.get_rect(center = ((WIDTH-imag1.get_width())/2, (HEIGHT-imag1.get_height())/2 + y1 + 15))
    ir2 = imag2.get_rect(center = ((WIDTH-imag2.get_width())/2, (HEIGHT-imag2.get_height())/2 + y2 - 15))
    pivot1 = ir1.bottomright
    pivot2 = ir2.bottomright

    #Drawing First Text
    a=1
    while alpha1 < 255:
        #Rotating both images to different directions
        screen.blit(bg, (0, 0))
        rotate(imag1, a, pivot1)
        rotate(imag2, a, pivot2)

        #Fade In Text
        fadein(screen, alpha1, alpha1_surf, txt1_surf, txt1_rect)

        alpha1 = min(alpha1+2, 255)
        a+=0.02   
        pygame.display.flip()
        clock.tick(60)

    while alpha2 < 255:
        #Rotating both images to different directions
        screen.blit(bg, (0, 0))
        rotate(imag1, a, pivot1)
        rotate(imag2, a, pivot2)

        #Fade In Text
        screen.blit(txt1_surf, txt1_rect)
        fadein(screen, alpha2, alpha2_surf, txt2_surf, txt2_rect)

        alpha2 = min(alpha2+3, 255)
        a+=0.02   
        pygame.display.flip()
        clock.tick(60)

    #loop
    on = True
    while on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on = False

        #Rotating both images to different directions
        screen.blit(bg, (0, 0))
        rotate(imag1, a, pivot1)
        rotate(imag2, a, pivot2)

        screen.blit(txt1_surf, txt1_rect)
        screen.blit(txt2_surf, txt2_rect)

        #space command
        screen.blit(cmd, cmd_rect)   
        pygame.display.flip()
        clock.tick(60)

    end = False
    while not(end):
        screen.fill('#000000')

        fadein(screen, alpha1, alpha1_surf, txt1_surf, txt1_rect)
        alpha1 = max(alpha1-5, 0)

        fadein(screen, alpha2, alpha2_surf, txt2_surf, txt2_rect)
        alpha2 = max(alpha2-5, 0)

        pygame.display.flip()
        clock.tick(60)

        if alpha1 == 0 and alpha2 == 0:
            end = True

    pygame.mixer.music.stop()

S1(screen)
