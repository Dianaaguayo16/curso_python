import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket Game")
bg_color = (0, 0, 0)
rocket = Rocket(screen)

while True:
    screen.fill(bg_color)
    keys = pygame.key.get_pressed()
    rocket.move(keys)
    rocket.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()