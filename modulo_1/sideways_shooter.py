import pygame
import sys

class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Bullet:
    def __init__(self, screen, ship):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 4)
        self.rect.midleft = ship.rect.midright
        self.color = (255, 0, 0)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sideways Shooter")
bg_color = (30, 30, 30)
ship = Ship(screen)
bullets = []

while True:
    screen.fill(bg_color)
    keys = pygame.key.get_pressed()
    ship.move(keys)
    ship.draw()

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw()
        if bullet.rect.left > 800:
            bullets.remove(bullet)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(screen, ship))
