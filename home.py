import pygame
from pygame.draw import *

def house(x, y):
    Surf = pygame.Surface((x, y), pygame.SRCALPHA)
    rect(Surf, [120, 80, 0], (0, y / 2, x, y / 2))
    rect(Surf, [0, 0, 0], (0, y / 2, x, y / 2), 2)
    polygon(Surf, (230, 10, 0), [(0, y / 2), (x / 2, 0), (x, y / 2), (0, y / 2)])
    polygon(Surf, (0, 0, 0), [(0, y / 2), (x / 2, 0), (x, y / 2), (0, y / 2)], 2)
    rect(Surf, [65, 105, 255], (x / 3, 2 * y / 3, x / 3, y / 6))
    rect(Surf, [65, 105, 255], (x / 3, 2 * y / 3, x / 3, y / 6), 2)
    return (Surf)

def round(Color, radius):
    Surf = pygame.Surface((2* radius, 2* radius), pygame.SRCALPHA)
    circle(Surf, Color, (radius, radius), radius)
    circle(Surf, [0, 0, 0], (radius, radius), radius, 1)
    return (Surf)

def tree(radius, a, h):
    x = 4 * radius + a
    y = 4 * radius + h
    Surf = pygame.Surface((x, y), pygame.SRCALPHA)
    rect(Surf, [0, 0, 0], ((x - a) / 2, y - h, a, h))
    Surf.blit(round([0, 105, 0], radius), (x / 2 - radius, radius))
    Surf.blit(round([0, 105, 0], radius), (x / 2 - 2.2*radius, 2*radius))
    Surf.blit(round([0, 105, 0], radius), (x / 2 + 0.2*radius, 2*radius))
    Surf.blit(round([0, 105, 0], radius), (x / 2 - radius, 2.5*radius))
    Surf.blit(round([0, 105, 0], radius), (x / 2, 3.2*radius + 4))
    Surf.blit(round([0, 105, 0], radius), (x / 2 - 2*radius, 3.2*radius))
    return (Surf)

"""облако с задоным радиусом отдельного подоблочка"""
def clouds(radius):
    Surf = pygame.Surface((6*radius, 4*radius), pygame.SRCALPHA)
    Surf.blit(round([255, 255, 255], radius), (radius, 2*radius))
    Surf.blit(round([255, 255, 255], radius), (2*radius, 2 * radius))
    Surf.blit(round([255, 255, 255], radius), (3*radius, 2 * radius))
    Surf.blit(round([255, 255, 255], radius), (4*radius, 2 * radius))
    Surf.blit(round([255, 255, 255], radius), (3*radius, radius))
    Surf.blit(round([255, 255, 255], radius), (2*radius, radius))
    return Surf

"""Хотел нарисовать красивое солнышко"""
def sun(x):
    Surf = pygame.Surface((x, x), pygame.SRCALPHA)

    return Surf

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
#rect(screen, [255, 255, 255], (0, 0, 800, 600))
rect(screen, [175, 238, 238], (0, 0, 800, 300))
rect(screen, [0, 238, 0], (0, 300, 800, 300))
"""Просто рисуем нужные нам объекты в нужных точках"""
screen.blit(house(150, 150), (420, 350))
screen.blit(house(200, 200), (80, 320))
screen.blit(tree(10, 5, 40), (600, 330))
screen.blit(tree(20, 10, 80), (300, 350))
screen.blit(clouds(20), (200, 100))
screen.blit(clouds(20), (300, 80))
screen.blit(clouds(20), (400, 120))
screen.blit(round([224, 112, 124], 30), (50, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()