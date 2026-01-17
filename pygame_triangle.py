import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sierpiński Triangle – Chaos Game")

# Three corners
corners = [(400, 50), (100, 650), (700, 650)]
current = [400, 350]  # start somewhere inside

BLACK = (0,0,0)
WHITE = (255,255,255)

screen.fill(BLACK)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Chaos game step
    corner = random.choice(corners)
    current[0] = (current[0] + corner[0]) // 2
    current[1] = (current[1] + corner[1]) // 2
    
    screen.set_at((current[0], current[1]), WHITE)
    
    pygame.display.flip()
    clock.tick(10000)  # as fast as possible

pygame.quit()
