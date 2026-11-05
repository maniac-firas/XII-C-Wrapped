import pygame

#Setup
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('XII-C Wrapped')
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
clock = pygame.time.Clock()

#Input text
COLOR_INACTIVE = '#0B1014'
COLOR_ACTIVE = '#2E3E4B'
FONT = pygame.font.Font('Fonts/Birds of Paradise.ttf', 35)
sfont = pygame.font.Font('Fonts/Birds of Paradise.ttf', 50)

SfRegular = pygame.font.Font('Fonts/SpotifyMix-Regular.ttf', 14)
cmd = SfRegular.render('-Click Space-', True, 'white')
cmd_rect = cmd.get_rect()
cmd_rect.centerx, cmd_rect.centery = 350, 700

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    with open('Images/Yearwords.txt', 'a') as f:
                        f.write(self.text)
                        f.write('\n')
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(400, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

#loading images
bg = pygame.image.load('Images/Bg8.png').convert_alpha()
bg = pygame.transform.scale(bg, (700, 800))

Sfn = pygame.font.Font('Fonts/SpotifyMix-Bold.ttf', 50)
Sfi = pygame.font.Font('Fonts/SpotifyMix-Bold.ttf', 25)
head = Sfn.render('Our Year in Three Words:', True, '#0F0649')
ins = Sfi.render('Enter return to save and Space if completed', True, '#0F0649')
hrect = head.get_rect()
hrect.centerx, hrect.centery = 350, -100

#Loading Music
pygame.mixer.init()
pygame.mixer.music.load('Music/WohDin.wav')

def S8(screen):
    pygame.mixer.music.play(-1)
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    hrect.centery = -100
    while hrect.centery <= 200:
        screen.blit(bg, (0, 0))
        screen.blit(head, hrect)
        hrect.centery += 1
        pygame.display.flip()
        clock.tick(180)

    with open('Images/Yearwords.txt', 'r') as f:
        data = f.readlines()
        if data == []:  on = True
        else:   on = False
    
    input_box1 = InputBox(350-200, 350-25, 500, 70)
    input_box2 = InputBox(350-200, 450-25, 500, 70)
    input_box3 = InputBox(350-200, 550-25, 500, 70)
    input_boxes = [input_box1, input_box2, input_box3]
    p, n = 0, 1
    while on:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()  
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    on = False

        for box in input_boxes:
            box.update()

        screen.blit(bg, (0, 0))
        screen.blit(head, hrect)
        screen.blit(ins, (100, 700))
        for box in input_boxes:
            box.draw(screen)
        
        hrect.centery += p
        p+=n
        if p == 5: n=-1
        if p == -5: n=1
        pygame.display.flip()
        clock.tick(30)

    n=0
    while n<=2: 
        screen.blit(bg, (0, 0))
        screen.blit(head, hrect)
        with open('Images/Yearwords.txt', 'r') as f:
            data = f.readlines()
        for i in data:
            txt = sfont.render(i, True, '#c1121f')
            txtrect = txt.get_rect()
            txtrect.centerx = 350
            txtrect.centery = 350 + n*100
            screen.blit(txt, txtrect)
            n += 1
        pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False

        screen.blit(cmd, cmd_rect)

    screen.fill('#000000')
    pygame.mixer.music.stop()

S8(screen)