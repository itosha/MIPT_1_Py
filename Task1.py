import pygame
from pygame.draw import *

def draw_rect_angle1(color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, *target_rect.size), width)
    surface = pygame.transform.rotate(shape_surf, angle)
    return(surface)

def smile(screen):
    print("Start")
    rect(screen, (128, 128, 128), (0, 0, 600, 600))
    circle(screen, (255, 255, 0), (300, 300), 100)
    circle(screen, (0, 0, 0), (300, 300), 100, 2)
    circle(screen, (255, 0, 0), (257, 275), 20)
    circle(screen, (0, 0, 0), (257, 275), 20, 1)
    circle(screen, (0, 0, 0), (257, 275), 9)
    circle(screen, (255, 0, 0), (343, 275), 15)
    circle(screen, (0, 0, 0), (343, 275), 15, 1)
    circle(screen, (0, 0, 0), (343, 275), 7)
    rect(screen, (0, 0, 0), (257, 355, 86, 20))
    rect_1 = (0, 0, 100, 10)
    rect_2 = (0, 0, 80, 10)
    surf_1 = draw_rect_angle1([0, 0, 0], rect_1, -30)
    surf_2 = draw_rect_angle1([0, 0, 0], rect_2, 30)
    screen.blit(surf_1, (200, 210))
    screen.blit(surf_2, (320, 220))

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

smile(screen)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()