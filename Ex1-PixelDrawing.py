import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Define colors:
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

# Some useful methods:
def drawPixel(surface, color, pos):
    surface.fill(color, (pos, (1,1)))
    
# Initialize pygame:
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ex.1 A Pixel Drawing Example")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Initialize the screen:
screen.fill(WHITE)
pygame.display.flip()

running = True

while running:

    clock.tick(FPS)
    
    # Process inputs:
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update:
    all_sprites.update()

    # Draw / render:
    all_sprites.draw(screen)
    
    # Draw a pixel at a random position in every frame:
    drawPixel(screen, GREEN, (random.randit(0, WIDTH), random.randit(0, HEIGHT)))
    pygame.display.flip()

pygame.quit()
