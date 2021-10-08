import pygame
from pygame.draw import *
from models import Alien
from models import Ufo
from models import Clouds

def Draw_Alien(screen_UN, face_color, body_color, X, Y, k_Alien_UN, mirroring):
	"""
	Эта функция рисует пришельца, по заранее разработанной модельки, позволяя задать масштаб
	и при необходимости отзеркалить пришельца.
	:param screen_UN: поверхность где вы хотите нарисовать пришельца
	:param face_color цвет лица пришельца
	:param body_color цвет тела пришельца
	:param X: примерный центр шеи пришельца по X
	:param Y: примерный центр шеи пришельца по Y
	:param k_Alien_UN: масштаб, где значение '1' соответствует ширине картинки 367 и высоте 543.
	Если ширина с учетом масштаба получается нецелой, то она округляется. Аналогично с высотой.
	:param mirroring: True если отзеркаливание не требуеться. False если требуеться
	"""
	PlcA = pygame.Surface((S[0], S[1]), pygame.SRCALPHA, 32)
	Alien(PlcA, face_color, body_color, 0, 0)
	PlcA = pygame.transform.flip(PlcA, mirroring, False)
	x = int(k_Alien_UN*S[0])
	y = int(k_Alien_UN*S[1])
	screen_UN.blit(pygame.transform.scale(PlcA, (x, y)), (X - 2 * x / 3, Y - 5 * y / 13))

def Draw_UFO(screen_UN, color_frame, color_big_window, color_small_window, X, Y, k_Ufo_UN):
	"""
	Эта функция рисует летающую тарелку, по заранее разработанной модельки, позволяя менять масштаб
	:param screen_UN: поверхность на которой будет рисунок
	:param X: примерный центр кабины по X
	:param Y: примерный центр кабины по Y
	:param k_Ufo_UN:  масштаб, где значение '1' соответствует ширине картинки 373 и высоте 600.
	Если ширина с учетом масштаба получается нецелой, то она округляется. Аналогично с высотой.
	"""
	PlcU = pygame.Surface((S[2], S[3]), pygame.SRCALPHA, 32)
	Ufo(PlcU, color_frame, color_big_window, color_small_window, 0, 0)
	x = int(k_Ufo_UN*S[2])
	y = int(k_Ufo_UN*S[3])
	screen_UN.blit(pygame.transform.scale(PlcU, (x, y)), (X - x / 2, Y - 2 * y / 19))

pygame.init()

Width, Height = 600, 800
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
finished = False
FPS = 30

S = [367, 543, 373, 600, 794, 562]
k_x = Width / 794
k_y = Height / 1123
k = (k_x ** 2 + k_y ** 2) ** 0.5

# Background
rect(screen, (0, 34, 43), (0, 0, Width, Height / 2))
"""for i in range(0, 400, 1):
	rect(screen, (int(41 * i / 80) + 10, int(10 * i / 50) + 3, 0), (0, 399 - i, Width, 1))"""

rect(screen, (34, 43, 0), (0, Height/2, Width, Height / 2))
ellipse(screen, (242, 242, 242), (382 * k_x, 124 * k_y, 250*k, 250*k))
# Clouds
PlcC = pygame.Surface((S[4], S[5]), pygame.SRCALPHA, 32)
Clouds(PlcC, (102, 102, 102), (51,  51,  51))
screen.blit(pygame.transform.scale(PlcC, (int(k_x*S[4]), int(k_y*S[5]))), (0, 0))

x_ufo, y_ufo, k_Ufo = 160, 250, 0.8
Draw_UFO(screen, (120, 120, 120), (20, 20, 200), (255, 255,   0), x_ufo, y_ufo, k_Ufo)
x_ufo, y_ufo, k_Ufo = 500, 350, 0.4
Draw_UFO(screen, (120, 120, 120), (20, 20, 200), (255, 255,   0), x_ufo, y_ufo, k_Ufo)
x_ufo, y_ufo, k_Ufo = 410, 490, 0.3
Draw_UFO(screen, (120, 120, 120), (20, 20, 200), (255, 255,   0), x_ufo, y_ufo, k_Ufo)

x_alien, y_alien, k_Alien = 520, 680, 0.6
Draw_Alien(screen, (221, 223, 175), (221, 223, 175), x_alien, y_alien, k_Alien, True)
x_alien, y_alien, k_Alien = 150, 500, 0.6
Draw_Alien(screen, (221, 223, 175), (221, 223, 175), x_alien, y_alien, k_Alien, True)

pygame.display.update()

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()