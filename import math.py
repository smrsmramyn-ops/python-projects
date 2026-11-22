import math
import random
import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beating Heart Animation")
clock = pygame.time.Clock()

# Heart shape mathematical equation
def heart_shape(t):
    x = 16 * (math.sin(t) ** 3)
    y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
    return x, y

# Generate base heart points
heart_points = []
dt = 0.02
t = 0
while t < 2 * math.pi:
    x, y = heart_shape(t)
    heart_points.append((x, y))
    t += dt

# Main loop
running = True
scale_time = 0

while running:
    screen.fill((10, 10, 15))  # Dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pulsing effect using Sine wave
    scale_time += 0.1
    pulse = 1.0 + 0.1 * math.sin(scale_time)

    # Center of the screen
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    # Draw glowing spark heart particles
    for x, y in heart_points:
        px = int(center_x + x * 15 * pulse + random.uniform(-2, 2))
        py = int(center_y + y * 15 * pulse + random.uniform(-2, 2))

        # Random colors between red and orange for glowing spark effect
        color = (random.randint(200, 255), random.randint(50, 100), random.randint(50, 100))
        
        pygame.draw.circle(screen, color, (px, py), random.randint(1, 3))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()