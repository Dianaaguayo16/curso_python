class Alien:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() - self.rect.width
        self.rect.y = randint(0, screen.get_height() - self.rect.height)
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)

aliens = [Alien(screen) for _ in range(5)]

# Inside game loop
for alien in aliens[:]:
    alien.update()
    alien.draw()
    if alien.rect.right < 0:
        aliens.remove(alien)

# Bullet collision
for bullet in bullets[:]:
    for alien in aliens[:]:
        if bullet.rect.colliderect(alien.rect):
            bullets.remove(bullet)
            aliens.remove(alien)