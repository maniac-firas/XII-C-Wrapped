import pygame

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Loading images
bg = pygame.image.load('Images/Bg7.png').convert_alpha()
bg = pygame.transform.scale(bg, (700, 800))
bg1 = pygame.image.load('Images/Bg8.png').convert_alpha()
bg1 = pygame.transform.scale(bg1, (700, 800))

#Numbers and things
Sfn = pygame.font.Font('Fonts/SpotifyMix-Bold.ttf', 50)
Sfs = pygame.font.Font('Fonts/SpotifyMix-Bold.ttf', 30)
num = ['10', '78', '91', '1', '2', '59', '8']
sta = ["months spent together", "fines paid", "late attendances", "tragedy accident", "people cried", "wrong uniforms", "assemblies conducted"]

head = Sfn.render('Our Year in Numbers', True, '#375D49')
hrec = head.get_rect()
hrec.centerx, hrec.centery = 350, -100

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = SfRegular.render('-Click Space-', True, 'white')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

numtxt, statxt = [], []
for i in range(len(num)):
    numtxt.append(Sfn.render(num[i], True, '#000000'))
    statxt.append(Sfs.render(sta[i], True, '#000000'))

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/Ilavanka.wav')


def S7(screen):
    pygame.mixer.music.play(-1)
    y=0
    fps=1000
    while y < 800:
        screen.blit(bg, (0, 800-y))
        pygame.display.flip()
        clock.tick(fps)
        y+=1
        fps-=1

    y=hrec.centery
    fps=300
    x=750
    while y <=100:
        screen.blit(bg, (0, 0))
        screen.blit(head, hrec)
        for i in range(len(num)+1):
            pygame.draw.circle(screen, '#51ADAF', (x, 200+75*i), 30)
        pygame.display.flip()
        clock.tick(fps)
        hrec.centery+=1
        y=hrec.centery
        fps-=1
        x = max(600, x-1)

    l = len(num)
    i=0
    y=200
    while i < l:
        y1 = 800
        while y1 >= y:
            screen.blit(bg, (0, 0))
            screen.blit(head, hrec)
            for k in range(len(num)+1):
                pygame.draw.circle(screen, '#51ADAF', (x, 200+75*k), 30)
            for j in range(i):
                screen.blit(numtxt[j], (50, 200+(75)*j))
                screen.blit(statxt[j], (120, 210+(75)*j))
            screen.blit(numtxt[i], (50, y1))
            screen.blit(statxt[i], (120, y1+10))
            y1-=1
            pygame.display.flip()
            clock.tick(360)
        i+=1
        y+=75

    screen.blit(cmd, cmd_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

    end = False
    bgy = 800
    x=600
    z=1
    fps=400
    while not(end):
        screen.blit(bg1, (0, 0))
        screen.blit(bg, (0, 800-bgy))
        screen.blit(head, hrec)
        for i in range(len(num)+1):
            pygame.draw.circle(screen, '#51ADAF', (x, 200+75*i), 30)
        for j in range(i):
            screen.blit(numtxt[j], (50, 200+(75)*j+z))
            screen.blit(statxt[j], (120, 210+(75)*j+z))
        pygame.display.flip()
        clock.tick(fps)
        hrec.centery-=1
        x = min(900, x+1)
        bgy-=1
        z+=1

        if bgy <= -100:  end = True
    pygame.mixer.music.stop()

S7(screen)
