ship_hits = 0
alien_hits = 0
max_ship_hits = 3

# Alien hits ship
for alien in aliens[:]:
    if alien.rect.colliderect(ship.rect):
        ship_hits += 1
        aliens.remove(alien)

# Bullet hits alien
for bullet in bullets[:]:
    for alien in aliens[:]:
        if bullet.rect.colliderect(alien.rect):
            alien_hits += 1
            bullets.remove(bullet)
            aliens.remove(alien)

# End game condition
if ship_hits >= max_ship_hits:
    print("Game Over! The ship was hit too many times.")
    pygame.quit()
    sys.exit()
