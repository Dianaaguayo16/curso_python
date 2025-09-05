def check_bullet_alien_collisions(self):
    collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
    if collisions:
        self._update_score(collisions)
    if not self.aliens:
        self._start_new_level()

def _update_score(self, collisions):
    for aliens in collisions.values():
        self.stats.score += self.settings.alien_points * len(aliens)
    self.sb.prep_score()
    self.sb.check_high_score()

def _start_new_level(self):
    self.bullets.empty()
    self._create_fleet()
    self.settings.increase_speed()
    self.stats.level += 1
    self.sb.prep_level()
