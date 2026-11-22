import pygame
import math
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Love You Heart")

black = (0, 0, 0)
pink = (255, 105, 180)

font = pygame.font.SysFont("arial", 12, bold=True)
text_surface = font.render("LOVE YOU", True, pink)

points = []
for z in range(18, 0, -1):
    scale = z * 0.75
    i = 0
    while i < math.pi * 2:
        hx = 16 * (math.sin(i) ** 3)
        hy = -(13 * math.cos(i) - 5 * math.cos(2*i) - 2 * math.cos(3*i) - math.cos(4*i))
        x = hx * scale * 13 + width / 2
        y = hy * scale * 13 + height / 2
        points.append((x, y))
        i += 0.12

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    for pt in points:
        screen.blit(text_surface, pt)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()