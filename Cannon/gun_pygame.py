import math
import time
from math import sin as sin
from math import cos as cos
from random import randrange as rnd, choice

import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
GAME_COLORS_for_ball = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, kind, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        kind - объект выпустивший снаряд
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.kind = kind
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS_for_ball)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 0.85
        if self.y >= 597 - self.r and self.vy < 0:
            self.vy *= -0.6
            self.vx *= 0.8
        if self.y <= self.r and self.vy > 0:
            self.vy *= -0.6
            self.vx *= 0.8
        if self.x >= 800 - self.r and self.vx > 0:
            self.vx *= -0.6
            self.vy *= 0.8
        if self.x <= self.r and self.vx < 0:
            self.vx *= -0.6
            self.vy *= 0.8
        if abs(self.vx) < 0.85 and abs(self.vy) < 0.85:
            self.vx = 0
            self.vy = 0
            self.live -= 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        distans = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2
        if obj.time_space > 0 or (self.kind is obj):
            return False
        elif distans > (self.r + obj.r) ** 2:
            return False
        else:
            obj.live -= 1
            return True

    def destruction(self):
        ...


class Roket(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, kind, x=40, y=450, angle=math.radians(0), v=20):
        """
        Конструктор
        :param screen:
        :param kind: объект выстелевший
        :param x: начальное положение
        :param y: начальное положение
        :param angle: угол полета
        :param v: скорость
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.kind = kind
        print(self.kind)
        self.angle = angle
        self.s = 78
        self.h = 22
        self.R = 80
        self.vx = v * math.cos(self.angle)
        self.vy = v * math.sin(self.angle)
        self.live = 1
        self.rocket = pygame.Surface((20, 20))
        self.rect = self.rocket.get_rect()

    def move(self):
        """
        прередвигает рокеты в соответствие со скоростью и взрывает при попадание в стену
        """
        self.x += self.vx
        self.y -= self.vy
        if self.y >= HEIGHT - 3 and self.vy < 0:
            self.vy *= -1
            self.vx *= 1
            self.angle *= -1
            self.live -= 1
        if self.y <= 0 and self.vy > 0:
            self.vy *= -1
            self.vx *= 1
            self.angle *= -1
            self.live -= 1
        if self.x >= WIDTH and self.vx > 0:
            self.vx *= -1
            self.vy *= 1
            self.angle = math.radians(180) - self.angle
            self.live -= 1
        if self.x <= 0 and self.vx < 0:
            self.vx *= -1
            self.vy *= 1
            self.angle = math.radians(180) - self.angle
            self.live -= 1

    def draw(self):
        self.rocket = pygame.image.load('Roket.bmp')
        self.rocket = pygame.transform.scale(self.rocket, (self.s, self.h))
        self.rocket = pygame.transform.rotate(self.rocket, math.degrees(self.angle))
        self.rect = self.rocket.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.screen.blit(self.rocket, (self.x, self.y))

    def detonation(self):
        """
        прокручивает анимацию взырыва
        сделано на коленке
        когда писал еще не работал над проектом
        """
        detonation = pygame.image.load('detonation.bmp')
        r = (self.s ** 2 + self.h ** 2 / 4) ** 0.5
        x0 = math.cos(self.angle) * r + self.x
        y0 = math.sin(-self.angle) * r + self.y
        detonation = pygame.transform.scale(detonation, (int(0.5 * self.R), int(0.5 * self.R)))
        self.screen.blit(detonation, (x0 - 0.25 * self.R, y0 - 0.25 * self.R))
        pygame.display.update()
        #time.sleep(1)
        detonation = pygame.transform.scale(detonation, (int(self.R), int(self.R)))
        self.screen.blit(detonation, (x0 - 0.5 * self.R, y0 - 0.5 * self.R))
        pygame.display.update()
        #time.sleep(1)
        detonation = pygame.transform.scale(detonation, (int(2 * self.R), int(2 * self.R)))
        self.screen.blit(detonation, (x0 - self.R, y0 - self.R))
        pygame.display.update()
        #time.sleep(1)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        x = self.rect.center
        x0 = x[0]
        y0 = x[1]
        distans = (x0 - obj.x) ** 2 + (y0 - obj.y) ** 2
        if obj.time_space > 0 or (self.kind is obj):
            return False
        elif distans > obj.r ** 2:
            return False
        else:
            self.live -= 1
            obj.live -= 3
            return True

    def destruction(self):
        self.detonation()


class Gun:
    def __init__(self, screen: pygame.Surface, x=20, y=450):
        """
        Конструктор
        :param screen:
        :param x: начальное положение
        :param y: начальное положение
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = x
        self.y = y
        self.an = 1
        self.color = BLACK

    def fire_ball_start(self, event):
        self.f2_on = 1

    def fire_rocket_start(self, event):
        self.f2_on = 1

    def fire_ball_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball(self.screen, self, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_ball

    def fire_rocket_end(self, event):
        """Выстрел рокетой.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.an = -math.atan2((event.pos[1]-self.y), (event.pos[0]-self.x))
        new_rocket = Roket(self.screen, self, self.x, self.y, self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_rocket

    def fire_emeny_rocket_end(self, y, x):
        """Выстрел рокетой. Функция для выстела бота
        """
        self.an = -math.atan2((y-self.y), (x-self.x))
        new_rocket = Roket(self.screen, self, self.x, self.y, self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_rocket

    def refresh(self):
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-self.x == 0:
                if event.pos[1]-self.y > 0:
                    self.an = math.radians(-90)
                else:
                    self.an = math.radians(90)
            else:
                if event.pos[0]-self.x > 0:
                    self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
                else:
                    self.an = math.radians(180) - math.atan((-event.pos[1] + self.y) / (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK

    def targetting_hero(self, x, y):
        """
        прицеливание бота в точку x, y
        """
        if x - self.x == 0:
            if y - self.y > 0:
                self.an = math.radians(-90)
            else:
                self.an = math.radians(90)
        else:
            if x - self.x > 0:
                self.an = math.atan((y - self.y) / (x - self.x))
            else:
                self.an = math.radians(180) - math.atan((-y + self.y) / (x - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = BLACK

    def draw_gun(self):
        x = self.x
        y = self.y
        l = max(self.f2_power, 20)
        h = 5
        pygame.draw.polygon(self.screen,
                            self.color,
                            ((x, y),
                             (x + l * math.cos(self.an), y - l * math.sin(-self.an)),
                             (x + l * math.cos(-self.an) - h * math.sin(-self.an),
                              y - l * math.sin(-self.an) - h * math.cos(-self.an)),
                             (x - h * math.sin(-self.an), y - h * math.cos(-self.an)),
                             (x, y)))


class Track:
    def __init__(self, screen: pygame.Surface, v=5, x=20, y=450, width=50, height=40, angle=0):
        """
        конструктор
        :param screen:
        :param v: скорость движеня полная
        :param x: начальное положение
        :param y: начальное положение
        :param width: ширина
        :param height: высота
        :param angle: начальныйугол поворота
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.v = v
        self.vx = 0
        self.vy = 0
        self.movement = 0
        self.a = width
        self.b = height
        self.r = 40
        self.color_track = GREEN

    def start_move(self, event):
        if event.key == pygame.K_w:
            self.angle = 90
            self.movement = 1
        if event.key == pygame.K_s:
            self.angle = -90
            self.movement = 1
        self.vx = self.v * math.cos(math.radians(self.angle))
        self.vy = self.v * math.sin(math.radians(-self.angle))

    def move(self):
        if self.movement:
            self.x += self.vx
            self.y += self.vy

    def end_move(self):
        self.movement = 0
        self.vx = 0
        self.vy = 0

    def draw_track(self):
        x = self.x
        y = self.y
        a = self.a
        b = self.b
        angle = math.radians(self.angle)
        pygame.draw.polygon(self.screen,
                            self.color_track,
                            ((x + 0.5*(b*sin(angle)-a*cos(angle)), y + 0.5*(a*sin(angle)+b*cos(angle))),
                             (x - 0.5*(b*sin(angle)+a*cos(angle)), y + 0.5*(a*sin(angle)-b*cos(angle))),
                             (x - 0.5*(b*sin(angle)-a*cos(angle)), y - 0.5*(a*sin(angle)+b*cos(angle))),
                             (x + 0.5*(b*sin(angle)+a*cos(angle)), y - 0.5*(a*sin(angle)-b*cos(angle))),))


class Tank(Track, Gun):
    def __init__(self, screen: pygame.Surface, x=20, y=450):
        """
        конструкор танка
        :param screen:
        :param x: начальное положение
        :param y: начальное положение
        """
        Track.__init__(self, screen, v=5, x=x, y=y, width=50, height=40, angle=0)
        Gun.__init__(self, screen, x=x, y=y)
        self.live = 3
        self.time_space = 0
        self.last_fire = 0


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.points = 0
        self.time_space = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(30, 40)
        self.vx = 0
        self.vy = rnd(10, 20)
        self.color = RED
        self.live = 1

    def move(self):
        """Переместить цель по прошествии единицы времени."""
        self.x += self.vx
        self.y -= self.vy
        #self.vy -= 0.85
        if self.y >= 597 - self.r and self.vy < 0:
            self.vy *= -1
            self.vx *= 1
        if self.y <= self.r and self.vy > 0:
            self.vy *= -1
            self.vx *= 1
        if self.x >= 800 - self.r and self.vx > 0:
            self.vx *= -1
            self.vy *= 1
        if self.x <= self.r and self.vx < 0:
            self.vx *= -1
            self.vy *= 1

    def hit(self, points=1):
        """Попадание снаряда в цель."""
        self.points += points
        self.time_space = 40

    def draw(self):
        if self.time_space > 0:
            self.time_space -= 1
        else:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )
            pygame.draw.circle(
                self.screen,
                BLACK,
                (self.x, self.y),
                self.r,
                2
            )


class Bomb:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.time_space = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(40, 45)
        self.vx = 0
        self.vy = 0
        self.live = 1

    def move(self):
        """Переместить цель по прошествии единицы времени."""
        self.x += self.vx
        self.y -= self.vy
        #self.vy -= 0.85
        if self.y >= 597 - self.r and self.vy < 0:
            self.vy *= -1
            self.vx *= 1
        if self.y <= self.r and self.vy > 0:
            self.vy *= -1
            self.vx *= 1
        if self.x >= 800 - self.r and self.vx > 0:
            self.vx *= -1
            self.vy *= 1
        if self.x <= self.r and self.vx < 0:
            self.vx *= -1
            self.vy *= 1

    def hit(self, points=1):
        """Попадание снаряда в цель."""
        self.points -= points
        self.time_space = 40

    def draw(self):
        if self.time_space > 0:
            self.time_space -= 1
        else:
            bomb = pygame.image.load('Bomb2.bmp')
            bomb = pygame.transform.scale(bomb, (2*self.r, 2*self.r))
            self.screen.blit(bomb, (self.x - self.r, self.y - self.r))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
topic = "Name: "
Text = topic

clock = pygame.time.Clock()
tank = Tank(screen)
tank_enemy = Tank(screen, 400, 400)
tank_enemy1 = Tank(screen, 500, 200)
target = []
target += [Target(screen)]
target += [Bomb(screen)]
finished = False
point = 0
enemy = []
enemy += [tank_enemy]
enemy += [tank_enemy1]
while not finished:
    screen.fill(WHITE)
    Points = str(point)
    for t in target:
        t.draw()
        t.move()
    textsurface = myfont.render(Points, False, (0, 0, 0))
    point = 0
    screen.blit(textsurface, (10, 10))

    tank.move()
    tank.draw_track()
    tank.draw_gun()
    for t in enemy:
        t.draw_track()
        t.draw_gun()
    for b in balls:
        if b.live <= 0:
            b.destruction()
            balls.remove(b)

    for b in balls:
        b.draw()
        b.move()

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            tank.fire_rocket_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            if tank.f2_power > 80:
                balls.append(tank.fire_rocket_end(event))
                bullet += 1
            else:
                tank.f2_on = 0
                tank.f2_power = 10
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            tank.fire_ball_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            balls.append(tank.fire_ball_end(event))
            bullet += 1
        elif event.type == pygame.MOUSEMOTION:
            tank.targetting(event)
        elif event.type == pygame.KEYDOWN:
            tank.start_move(event)
        elif event.type == pygame.KEYUP:
            tank.end_move()

    point = 0
    for t in target:
        for b in balls:
            if b.hittest(t) and t.live:
                t.hit()
                t.new_target()
        point += t.points

    for t in enemy:
        for b in balls:
            if b.hittest(t) and t.live > 0:
                b.destruction()
                balls.remove(b)
                b.draw()
    tank.power_up()
    for t in enemy:
        t.targetting_hero(tank.x, tank.y)
        now = pygame.time.get_ticks()
        if now - t.last_fire > 6000:
            balls.append(t.fire_emeny_rocket_end(tank.y, tank.x))
            t.last_fire = now
        if t.live <= 0:
            enemy.remove(t)

    for b in balls:
        if b.hittest(tank) and tank.live > 0:
            b.destruction()
            balls.remove(b)
            b.draw()

    if tank.live <= 0:
        finished = True
        textsurface = myfont.render('GAME OVER', False, (0, 0, 0))
        screen.blit(textsurface, (100, 100))
        pygame.display.update()
        time.sleep(4)



pygame.quit()
