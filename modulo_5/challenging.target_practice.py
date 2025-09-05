class Target:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("target.bmp")
        self.rect = self.image.get_rect()
        self.rect.midright = screen.get_rect().midright
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= self.screen.get_height() or self.rect.top <= 0:
            self.speed *= -1

    def draw(self):
        self.screen.blit(self.image, self.rect)

self.settings.target_speed = self.settings.initial_target_speed
