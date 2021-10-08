import pygame
from pygame.draw import *

pygame.init()

Width, Height = 600, 400
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
finished = False
FPS = 30

for i in range(0, 400, 1):
    rect(screen, (int(41 * i / 80), int(10 * i / 50), 0), (0, 399 - i, Width, 1))

pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()