class AlienBullet(pygame.sprite.Sprite):
    def __init__(self, alien):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()

if random.randint(0, 100) < 2:
    for alien in self.aliens.sprites():
        self.alien_bullets.add(AlienBullet(alien))

class Shield(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
