import pygame

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#loading images
bg = pygame.image.load('Images/Bg6.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (700, 800))
screen.blit(bg, (0, 0))
trophy = pygame.image.load('Images/trophy.png').convert_alpha()
trophy = pygame.transform.scale(trophy, (100, 100))

S=[]
def image(name):
    temp = pygame.image.load('Photos/'+name).convert_alpha()
    temp = pygame.transform.scale(temp, (350, 800))    
    S.append(temp)
image('side1.png')
image('side2.png')


#Loading texts
SfRegular = pygame.font.Font('Fonts/SpotifyMix-RegularItalic.ttf', 25)
def comp(screen, y):
    bits = ['Music', 'Western Music', 'Thiruvathira', 'Dance', 'Pencil Drawing', 'Story writing', 'Mime', 'One Act Play', 'Versification', 'Presentation', 'Safar', 'Sports']
    for i in range(len(bits)):
        temp = SfRegular.render(bits[i], True, '#000000')
        rect = temp.get_rect()
        rect.centerx, rect.centery = 350, y+(i*30)
        screen.blit(temp, rect)

Sfc = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = Sfc.render('-Click Space-', True, 'black')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/CountingStars.wav')

def S6(screen):
    pygame.mixer.music.play(-1)
    screen.blit(bg, (0, 0))
    screen.blit(trophy, (350-50, 400-50))
    pygame.display.flip()
    clock.tick(60)

    y=0
    z=900
    fps = 400
    while z >= 300:
        screen.blit(bg, (0, 0))
        screen.blit(trophy, (350-50, 400-50-y))
        comp(screen, z)
        pygame.display.flip()
        y = min(200, y+1)
        z-=2
        fps = max(180, fps-1)
        clock.tick(fps)

    x1, x2 = -350, 700
    while x1 < -50 and x2 > 400:
        screen.blit(bg, (0, 0))
        screen.blit(trophy, (350-50, 400-50-y))
        comp(screen, z)
        screen.blit(S[0], (x1, 0))
        screen.blit(S[1], (x2, 0))

        x1 = x1+1
        x2 = x2-1

        pygame.display.flip()
        clock.tick(120)

    running = True
    p=0
    n=1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.blit(bg, (0, 0))
        screen.blit(trophy, (350-50, 400-50-y-p))
        comp(screen, z-p)
        screen.blit(S[0], (x1, p))
        screen.blit(S[1], (x2, p))
        screen.blit(cmd, cmd_rect)

        p+=n
        if p == 10: n=-1
        if p == -10: n=1
        pygame.display.flip()
        clock.tick(40)

    screen.blit(bg, (0, 0))
    pygame.display.flip()

    pygame.mixer.music.stop()

S6(screen)