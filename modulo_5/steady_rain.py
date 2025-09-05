import pygame
import sys

class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("raindrop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Raindrop Grid")
bg_color = (30, 30, 30)

raindrops = []
drop_width = 40
drop_height = 40
cols = screen.get_width() // drop_width
rows = screen.get_height() // drop_height

for row in range(rows):
    for col in range(cols):
        x = col * drop_width
        y = row * drop_height
        raindrops.append(Raindrop(screen, x, y))

while True:
    screen.fill(bg_color)
    for drop in raindrops[:]:
        drop.update()
        drop.draw()
        if drop.rect.top > screen.get_height():
            raindrops.remove(drop)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Add new row when drops are removed
if len(raindrops) < cols * rows:
    for col in range(cols):
        x = col * drop_width
        y = 0  # Top of screen
        raindrops.append(Raindrop(screen, x, y))
