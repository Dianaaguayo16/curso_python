import pygame
import sys

class Character:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # Create a simple character using shapes instead of an image
        self.rect = pygame.Rect(0, 0, 50, 80)  # Character dimensions
        self.rect.center = self.screen_rect.center
        self.color = (255, 165, 0)  # Orange color for the character

    def draw(self):
        # Draw the character body (rectangle)
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        # Draw the character head (circle)
        head_center = (self.rect.centerx, self.rect.top - 20)
        pygame.draw.circle(self.screen, (255, 218, 185), head_center, 25)  # Skin color
        
        # Draw eyes
        left_eye = (head_center[0] - 8, head_center[1] - 5)
        right_eye = (head_center[0] + 8, head_center[1] - 5)
        pygame.draw.circle(self.screen, (0, 0, 0), left_eye, 3)   # Black eyes
        pygame.draw.circle(self.screen, (0, 0, 0), right_eye, 3)
        
        # Draw arms
        left_arm = pygame.Rect(self.rect.left - 15, self.rect.top + 20, 15, 8)
        right_arm = pygame.Rect(self.rect.right, self.rect.top + 20, 15, 8)
        pygame.draw.rect(self.screen, self.color, left_arm)
        pygame.draw.rect(self.screen, self.color, right_arm)
        
        # Draw legs
        left_leg = pygame.Rect(self.rect.left + 5, self.rect.bottom, 15, 20)
        right_leg = pygame.Rect(self.rect.right - 20, self.rect.bottom, 15, 20)
        pygame.draw.rect(self.screen, (139, 69, 19), left_leg)   # Brown pants
        pygame.draw.rect(self.screen, (139, 69, 19), right_leg)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character - Press ESC or X to close")
bg_color = (135, 206, 235)  # Sky blue background

character = Character(screen)

print("🎮 Game Character program started!")
print("👤 A simple character is displayed in the center")
print("⌨️  Press ESC key or close the window to exit")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(bg_color)
    character.draw()
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

print("👋 Closing Game Character program...")
pygame.quit()
print("✅ Program closed successfully!")