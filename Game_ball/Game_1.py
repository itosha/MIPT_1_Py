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


def new_square():
    """
    создает новый квадрат
    :return: возврашает список характеризующий новый квадрат
    (координаты середины, ширина, цвет, скорость, угол, очки за попадание, угол поворота,
    количество попаданий требуемых для получения очков)
    """
    x = randint(100, 1100)
    y = randint(100, 900)
    a = randint(60, 80)
    v = randint(10, 30)
    tap = randint(1, 5)
    angle = randint(0, 360)
    d_angle = randint(1, 5)
    color = COLORS[randint(0, 5)]
    points = tap * (a // 5)
    rect(screen, color, (x - a / 2, y - a / 2, a, a))
    return [x, y, a, color, v, angle, points, d_angle, tap]


def traffic_square(square):
    """
    передвигает уже существующий квадрат согласно его скорости, углу движения и поворота + изменяет угол при ударе о стенку
    :param square: принимает список описывающий квадрат
    :return: возврашает список подвинутого шара
    """
    square[5] = square[5] + square[7]
    square[0] = square[0] + square[4] * math.cos(math.radians(square[5]))
    square[1] = square[1] + square[4] * math.sin(math.radians(square[5]))
    if (square[0] <= 0) or (square[0] >= 1200):
        square[5] = 180 - square[5]
        square[7] = 180 - square[7]
    elif (square[1] <= 0) or (square[1] >= 900):
        square[5] = -square[5]
        square[7] = -square[7]
    rect(screen, square[3], (square[0] - square[2] / 2, square[1] - square[2] / 2, square[2], square[2]))
    return square


def Click_square(X, Y, square):
    """
    детектирует попадание в квадрат
    :param X: координаты мыши по Х
    :param Y: координаты мыши по У
    :param square: список описывающий исследуемый квадрат
    :return: True или False в зависимости от того уничтожил ли пользователь квадрат или нет
    """
    if abs(X - square[0]) <= square[2] / 2 and abs(Y - square[1]) <= square[2] / 2:
        square[8] -= 1
        if square[8] == 0:
            return True
    else:
        return False


def new_ball():
    """
    создает новый шарик и возврашает список описывающий его
    :return: список описывающий полученный шар (координаты центра, радиус, скорость, угол движения)
    """
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    points = r // 10
    v = randint(10, 30)
    angle = randint(0, 360)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return [x, y, r, color, v, angle, points]


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
square = []
trigger_ball = False
trigger_square = False
name_get = False

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
topic = "Name: "
Name = ""
Text = topic + Name

while not finished and not name_get:
    clock.tick(FPS)
    Text = topic + Name
    textsurface = myfont.render(Text, False, (100, 100, 0))
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
    screen.fill(BLACK)


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(ball)):
                if Click(event.pos[0], event.pos[1], ball[i]):
                    delete = i
                    trigger_ball = True
                    Points += ball[i][6]
            for i in range(len(square)):
                if Click_square(event.pos[0], event.pos[1], square[i]):
                    delete = i
                    trigger_square = True
                    Points += square[i][6]

    if trigger_ball:
        ball.pop(delete)
        trigger_ball = False
    if trigger_square:
        square.pop(delete)
        trigger_square = False
    for i in range(len(ball)):
        ball[i] = traffic(ball[i])
    for i in range(len(square)):
        square[i] = traffic_square(square[i])
    if len(ball) < 3:
        ball = [0] + ball
        ball[0] = new_ball()
    if len(square) < 2:
        square = [0] + square
        square[0] = new_square()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

with open("Tries.txt", 'a') as f:
    f.write(Name + ": " + str(Points))
    f.write("\n")