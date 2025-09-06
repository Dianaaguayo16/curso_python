import pygame
import sys

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create a rocket using shapes instead of an image
        self.rect = pygame.Rect(0, 0, 40, 60)  # Rocket dimensions
        self.rect.center = self.screen_rect.center
        self.speed = 5
        self.color = (255, 255, 255)  # White color for the rocket

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
        # Draw rocket body (main rectangle)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        # Draw rocket tip (triangle pointing up)
        tip_points = [
            (self.rect.centerx, self.rect.top - 20),
            (self.rect.left - 5, self.rect.top + 10),
            (self.rect.right + 5, self.rect.top + 10)
        ]
        pygame.draw.polygon(self.screen, (255, 0, 0), tip_points)  # Red tip
        
        # Draw rocket fins (triangles at bottom)
        left_fin = [
            (self.rect.left - 15, self.rect.bottom),
            (self.rect.left, self.rect.bottom - 20),
            (self.rect.left + 5, self.rect.bottom)
        ]
        right_fin = [
            (self.rect.right + 15, self.rect.bottom),
            (self.rect.right, self.rect.bottom - 20),
            (self.rect.right - 5, self.rect.bottom)
        ]
        pygame.draw.polygon(self.screen, (255, 0, 0), left_fin)   # Red fins
        pygame.draw.polygon(self.screen, (255, 0, 0), right_fin)
        
        # Draw rocket window (circle)
        window_center = (self.rect.centerx, self.rect.centery - 10)
        pygame.draw.circle(self.screen, (0, 150, 255), window_center, 8)  # Blue window
        
        # Draw rocket exhaust (small rectangles at bottom)
        exhaust_left = pygame.Rect(self.rect.centerx - 8, self.rect.bottom, 4, 8)
        exhaust_right = pygame.Rect(self.rect.centerx + 4, self.rect.bottom, 4, 8)
        pygame.draw.rect(self.screen, (255, 165, 0), exhaust_left)   # Orange exhaust
        pygame.draw.rect(self.screen, (255, 165, 0), exhaust_right)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket Game - Use Arrow Keys to Move, ESC to Exit")
bg_color = (0, 0, 0)  # Black space background

rocket = Rocket(screen)

print("🚀 Rocket Game started!")
print("🎮 Use Arrow Keys to move the rocket")
print("⌨️  Press ESC key or close the window to exit")
print("🌌 Navigate through space!")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(bg_color)
    keys = pygame.key.get_pressed()
    rocket.move(keys)
    rocket.draw()
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

print("👋 Closing Rocket Game...")
pygame.quit()
print("✅ Program closed successfully!")