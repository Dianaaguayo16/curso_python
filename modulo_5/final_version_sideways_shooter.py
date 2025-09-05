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

def increase_difficulty(self):
    self.settings.ship_speed *= 1.1
    self.settings.bullet_speed *= 1.1
    self.settings.alien_speed *= 1.1

self.stats.score += 10
self.sb.prep_score()

def run_game(self):
    while True:
        self._check_events()
        if self.stats.game_active:
            self.ship.update()
            self.bullets.update()
            self.aliens.update()
            self._check_collisions()
        self._update_screen()
