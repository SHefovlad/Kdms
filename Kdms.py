import pygame, os

WIDTH = 1280
HEIGHT = 720
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 130, 255)
CK = (0, 255, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KDMS")
clock = pygame.time.Clock()

custle_img = pygame.image.load('pl-1.png').convert()

x = 0
y = 0

class Custle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = custle_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

all_sprites = pygame.sprite.Group()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GREEN)
    all_sprites.remove()
    all_sprites.update()
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()