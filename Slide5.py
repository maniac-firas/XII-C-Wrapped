import pygame

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Loading Images
bg = pygame.image.load('Images/Bg5.png').convert_alpha()
bg = pygame.transform.scale(bg, (700, 800))
screen.blit(bg, (0, 0))
pygame.display.flip()
trophy = pygame.image.load('Images/trophy.png').convert_alpha()
trophy = pygame.transform.scale(trophy, (100, 100))
bg1 = pygame.image.load('Images/Bg6.jpg').convert_alpha()
bg1 = pygame.transform.scale(bg1, (700, 800))


#Loading texts
def createText(txtlist, rectlist, msg, y):
    temp = SfRegular.render(msg, True, '#000000')
    rect = temp.get_rect()
    rect.centery = y
    rect.centerx = 350
    txtlist.append(temp)
    rectlist.append(rect)

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Medium.ttf', 30)
msg1 = ['This year,', 'the Sahodaya Kalolstav', 'was conducted at', 'our school']
txts1, rcts1 = [], []
for i in range(len(msg1)):
    createText(txts1, rcts1, msg1[i], 340+(i*40))

msg2 = ['And many of our', 'XII-C talent gems', 'have participated', 'and came back', 'with glory']
txts2, rcts2 = [], []
for i in range(len(msg2)):
    createText(txts2, rcts2, msg2[i], 320+(i*40))

#loading music
pygame.mixer.init()
pygame.mixer.music.load('Music/Viva.wav')


def S5(screen):
    r=0
    fps=700
    pygame.mixer.music.play(0)
    while r <= 200:
        pygame.draw.circle(screen, '#f36f36', (350, 400), r)
        pygame.draw.circle(screen, '#000000', (350, 400), r, 1)
        r+=1
        fps=max(360, fps-2)
        pygame.display.flip()
        clock.tick(120)
    pygame.time.delay(1000)


    r=0
    fps=700
    while r <= 100:
        screen.blit(bg, (0, 0))
        pygame.draw.circle(screen, '#e97700', (350, 200), r)
        pygame.draw.circle(screen, '#e97700', (350, 600), r)
        pygame.draw.circle(screen, '#f36f36', (350, 400), 200)
        pygame.draw.circle(screen, '#000000', (350, 400), 200, 1)
        r += 1
        fps=max(360, fps-2)
        pygame.display.flip()
        clock.tick(180)


    r1, r2 = 100, 100
    n, z = 0, 1
    x = -700
    i=1
    while i <= 4:
        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, '#7500C3', (x, 50, 700, 10))
        pygame.draw.rect(screen, '#7500C3', (x, 750, 700, 10))
        pygame.draw.circle(screen, '#e97700', (350, 200), r1)
        pygame.draw.circle(screen, '#e97700', (350, 600), r2)
        pygame.draw.circle(screen, '#f36f36', (350, 400), 200)
        pygame.draw.circle(screen, '#000000', (350, 400), 200, 1)
        for j in range(i):
            screen.blit(txts1[j], rcts1[j])   
        r1+=z
        r2-=z
        n+=1
        if n%55 == 0: z *= -1
        if n%100 == 0 and i <= 4:  i+=1
        x+=4
        if x >= 700: x=-700
        pygame.display.flip()
        clock.tick(120)

    i=1
    while i <= 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, '#7500C3', (x, 50, 700, 10))
        pygame.draw.rect(screen, '#7500C3', (x, 750, 700, 10))
        pygame.draw.circle(screen, '#e97700', (350, 200), r1)
        pygame.draw.circle(screen, '#e97700', (350, 600), r2)
        pygame.draw.circle(screen, '#f36f36', (350, 400), 200)
        pygame.draw.circle(screen, '#000000', (350, 400), 200, 1)
        for j in range(i):
            screen.blit(txts2[j], rcts2[j])   
        r1+=z
        r2-=z
        n+=1
        if n%55 == 0: z *= -1
        if n%100 == 0 and i <= 5:  i+=1
        x+=4
        if x >= 700: x=-700
        pygame.display.flip()
        clock.tick(120)

    r=200
    n=0
    while r<=700:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, '#7500C3', (0, 50, 700, 10))
        pygame.draw.rect(screen, '#7500C3', (0, 750, 700, 10))
        pygame.draw.circle(screen, '#e97700', (350, 200), r1)
        pygame.draw.circle(screen, '#e97700', (350, 600), r2)
        pygame.draw.circle(screen, '#000000', (350, 400), 200, 1)
        pygame.draw.circle(screen, '#f36f36', (350, 400), r)
        screen.blit(trophy, (350-50, 400-50))
        if n >= 200:   r+=1
        n+=1
        pygame.display.flip()
        clock.tick(1040)
    
    screen.blit(bg1, (0, 0))
    pygame.display.flip()
    screen.blit(trophy, (350-50, 400-50))
    pygame.display.flip()
    pygame.mixer.music.stop()

S5(screen)