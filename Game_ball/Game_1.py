import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
Points = 0

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return [x, y, r, color]

def Click(X, Y, circles):
    T = (X - circles[0]) ** 2 + (Y - circles[1]) ** 2
    if T <= circles[2] ** 2:
        return True
    else:
        return False

pygame.display.update()
clock = pygame.time.Clock()
finished = False

ball = []

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(ball)):
                if Click(event.pos[0], event.pos[1], ball[i]):
                    print("WoW!")
                    Points += 1

    for i in range(len(ball)):
        ball[i] = new_ball()
    if len(ball) < 5:
        ball = [0] + ball
        ball[0] = new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print(Points)