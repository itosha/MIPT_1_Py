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

def new_trigon():
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    v = randint(10, 30)
    angle = randint(0, 360)
    color = COLORS[randint(0, 5)]
    p1 = (x - r * math.cos(math.radians(30)), y + r * math.sin(math.radians(30)))
    p2 = (x + r * math.cos(math.radians(30)), y + r * math.sin(math.radians(30)))
    polygon(screen, color, ((x, y - r), p1, p2, (x, y - r)))
    return [x, y, r, v, angle]


def new_ball():
    """
    создает новый шарик и возврашает список описывающий его
    :return: список описывающий полученный шар (координаты центра, радиус, скорость, угол движения)
    """
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    v = randint(10, 30)
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
    детектирует попадание в шар
    :param X: координаты мыши по Х
    :param Y: координаты мыши по У
    :param circles: список описывающий исследуемый шар (координаты центра, радиус, скорость, угол движения)
    :return: True или False в зависимости от того попал ли пользователь или нет
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
triger_ball = False

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
                    triger_ball = True
                    Points += 1

    if triger_ball:
        ball.pop(delet)
        triger_ball = False
    for i in range(len(ball)):
        ball[i] = traffic(ball[i])
    if len(ball) < 3:
        ball = [0] + ball
        ball[0] = new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

print(Points)