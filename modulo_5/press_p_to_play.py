def _start_game(self):
    self.stats.reset_stats()
    self.stats.game_active = True
    self.aliens.empty()
    self.bullets.empty()
    self._create_fleet()
    self.ship.center_ship()
    pygame.mouse.set_visible(False)

def _check_keydown_events(self, event):
    if event.key == pygame.K_p and not self.stats.game_active:
        self._start_game()

def _check_play_button(self, mouse_pos):
    if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
        self._start_game()
