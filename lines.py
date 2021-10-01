import pygame
from pygame.draw import *
import math

def angle(A, B, aspectRatio):
    x = B[0] - A[0]
    y = B[1] - A[1]
    angle = math.atan2(-y, x / aspectRatio)
    return angle

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
C = [300, 300]
A = [200, 400]
B = [400, 500]
line(screen, [255, 0, 0], C, A)
line(screen, [255, 0, 0], C, B)
a1 = angle(C, A, 600/600)
a2 = angle(C, B, 600/600)

pygame.draw.arc(screen, [255, 255, 255], (0, 0, 400, 500), a1, a2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()