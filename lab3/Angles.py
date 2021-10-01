import pygame
from pygame.draw import *

def draw_rect_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def draw_rect_angle1( color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, (0, 0, *target_rect.size), width)
    surface = pygame.transform.rotate(shape_surf, angle)
    return(surface)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
rect(screen, (255, 255, 255), (0, 0, 600, 600))

surf = pygame.Surface((60, 80))
surf2 = pygame.Surface((100, 100))
color_red = (255, 0, 0)
rect_1 = (0, 0, 60, 80)
angel = 45

surf1 = draw_rect_angle1( color_red, rect_1, angel)
#draw_ellipse_angle(surf2, color_red, rect_1, angel)
screen.blit(surf1, (300, 300))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()