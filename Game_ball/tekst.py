import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

clock = pygame.time.Clock()
finished = False
name_get = False

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
Name = "Name: "

pygame.display.update()

while not finished and not name_get:
    clock.tick(FPS)
    textsurface = myfont.render(Name, False, (100, 100, 0))
    screen.blit(textsurface, (110, 110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                name_get = True
            elif event.key == pygame.K_BACKSPACE:
                Name = Name[:-1]
            else:
                Name = Name + event.unicode

    pygame.display.update()
    screen.fill([0, 0, 0])

pygame.quit()
print(Name)