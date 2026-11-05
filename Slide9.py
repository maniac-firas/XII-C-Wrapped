import pygame

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

def rotate(im, angle, pivot):
    image = pygame.transform.rotate(im, angle)
    rect = image.get_rect()
    rect.center = pivot
    screen.blit(image, rect)

C = pygame.image.load('Images/c9.png').convert_alpha()
C = pygame.transform.scale(C, (300, 300))

Sfn = pygame.font.Font('Fonts/SpotifyMix-RegularItalic.ttf', 25)
a1 = Sfn.render('So, that\'s it.', True, '#000000')
a1r = a1.get_rect()
a1r.centerx, a1r.centery = 350, 0
a2 = Sfn.render('Just one more', True, '#000000')
a2r = a2.get_rect()
a2r.centerx, a2r.centery = 350, 0
a3 = Sfn.render('thing left', True, '#000000')
a3r = a3.get_rect()
a3r.centerx, a3r.centery = 350, 0

a4 = Sfn.render('Here\'s something', True, '#000000')
a4r = a4.get_rect()
a4r.centerx, a4r.centery = 350, 0
a5 = Sfn.render('for the instagrammers', True, '#000000')
a5r = a5.get_rect()
a5r.centerx, a5r.centery = 350, 0

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/end.wav')

#Stories
stories = []
rect = C.get_rect()
def imageload(name):
    global rect
    temp = pygame.image.load('Photos/'+name)
    temp = pygame.transform.scale(temp, (405, 720))
    rect = temp.get_rect()
    stories.append(temp)
imageload('Story1.JPEG')
imageload('Story2.JPEG')
imageload('Story3.JPEG')
imageload('Story4.JPEG')

rect.centerx, rect.centery = 350, 400

def S9(screen):
    pygame.mixer.music.play(-1)
    screen.fill('#000000')
    pygame.display.flip()
                    #Zooming In Effect
    s, a = 0, 1
    while s <= 180:
        screen.fill('#000000')
        img = pygame.transform.rotate(C, a)
        screen.blit(img, ((WIDTH-img.get_width())/2 , (HEIGHT-img.get_height())/2))
        screen.blit(a1, a1r)
        screen.blit(a2, a2r)
        screen.blit(a3, a3r)
        a1r.centery = min(350, a1r.centery+5)
        a2r.centery = min(400, a2r.centery+5)
        a3r.centery = min(450, a3r.centery+5)
        pygame.display.flip()
        a+=10
        s+=1
        clock.tick(30)

    s=1
    while s <= 180:
        screen.fill('#000000')
        img = pygame.transform.rotate(C, a)
        screen.blit(img, ((WIDTH-img.get_width())/2 , (HEIGHT-img.get_height())/2))
        screen.blit(a4, a4r)
        screen.blit(a5, a5r)
        a4r.centery = min(380, a4r.centery+5)
        a5r.centery = min(420, a5r.centery+5)
        pygame.display.flip()
        a+=10
        s+=1
        clock.tick(30)

    run = True
    i=0
    while run:
        screen.fill('#000000')
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and i>0:
                    i-=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and i<3:
                    i+=1
        
        screen.blit(stories[i], rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.mixer.music.stop()
    
S9(screen)