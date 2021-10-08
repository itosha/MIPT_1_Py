import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
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
    """
    создает новый шарик и возврашает список описывающий его
    :return: список описывающий полученный шар (координаты центра, радиус, скорость, угол движения)
    """
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    v = randint(10, 50)
    angle = randint(0, 360)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return [x, y, r, color, v, angle]


def traffic(ball):
    """
    передвигает уже существующий шарик согласно его скорости и углу движения + изменяет угол при ударе о стенку
    :param ball: принимает список описывающий шар (координаты центра, радиус, скорость, угол движения)
    :return: возврашает список подвинутого шара (новые координаты центра, радиус, скорость, новый угол движения)
    """
    ball[0] = ball[0] + ball[4] * math.cos(math.radians(ball[5]))
    ball[1] = ball[1] + ball[4] * math.sin(math.radians(ball[5]))
    if (ball[0] <= 0) or (ball[0] >= 1200):
        ball[5] = 180 - ball[5]
    elif (ball[1] <= 0) or (ball[1] >= 900):
        ball[5] = -ball[5]
    circle(screen, ball[3], (ball[0], ball[1]), ball[2])
    return ball


def Click(X, Y, circles):
    """

    :param X:
    :param Y:
    :param circles:
    :return:
    """
    T = (X - circles[0]) ** 2 + (Y - circles[1]) ** 2
    if T <= circles[2] ** 2:
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

ball = []
triger = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(ball)):
                if Click(event.pos[0], event.pos[1], ball[i]):
                    print("WoW!")
                    delet = i
                    triger = True
                    Points += 1

    if triger:
        ball.pop(delet)
        triger = False
    for i in range(len(ball)):
        ball[i] = traffic(ball[i])
    if len(ball) < 5:
        ball = [0] + ball
        ball[0] = new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print(Points)