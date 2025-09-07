import pygame
import sys

class Star:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("star.bmp")  # Use a small bitmap star image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.screen.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Grid")
bg_color = (0, 0, 20)

# Create grid of stars
stars = []
star_width = 40
star_height = 40
cols = screen.get_width() // star_width
rows = screen.get_height() // star_height

for row in range(rows):
    for col in range(cols):
        x = col * star_width
        y = row * star_height
        stars.append(Star(screen, x, y))

while True:
    screen.fill(bg_color)
    for star in stars:
        star.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
