import pygame
import random

WIDTH = 640
HEIGHT = 480
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
#sprite bank

rightWalk = pygame.surface.Surface((32,32))
leftwalk = pygame.surface.Surface((32,32))
background = pygame.image.load('background.png')

temp = pygame.image.load('right.png')
rightWalk.blit(temp,(0,0))
rightWalk.convert_alpha()
temp = pygame.image.load('left.png')
leftwalk.blit(temp,(0,0))
leftwalk.convert_alpha()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('rock.png')
        self.rect = self.image.get_rect()
        #self.rect.center = (WIDTH/2, HEIGHT/2)
        #uncomment this for ROCK

class Player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rightWalk
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.direction = EAST
        self.cycle = 0

    def update(self):
        def cycle_update(self):
            self.cycle +=1
            if self.cycle>=20:
                self.cycle=0
        def goright(self):
            self.image = rightWalk
            self.rect.x += 5
            cycle_update(self)

        def goleft(self):
            self.image = leftwalk
            self.rect.x-=5
            cycle_update(self)
        def goUp(self):
            self.rect.y+=5
            cycle_update(self)
        def goDown(self):
            self.rect.y-=5
            cycle_update(self)
        if self.cycle ==19 :
            self.direction = random.randint(0,3)

        if self.direction == EAST:
            goright(self)
            if self.rect.right>=WIDTH:
                self.direction=WEST
        elif self.direction == WEST:
            goleft(self)
            if self.rect.left <= 0:
                self.direction= EAST
        elif self.direction == SOUTH:
            goDown(self)
            if self.rect.bottom<=0:
                self.direction = NORTH
        elif self.direction == NORTH:
            goUp(self)
            if self.rect.top>=HEIGHT:
                self.direction=SOUTH




clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
rock = Rock()
all_sprites.add(player)
all_sprites.add(rock)
#game loop
running = True
while running:
    clock.tick(FPS)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update
    all_sprites.update()
    #draw
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    # AFTER drawing everything
    pygame.display.flip()

pygame.quit
