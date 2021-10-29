import math
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
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
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
        if distans > (self.r + obj.r) ** 2:
            return False
        else:
            return True


class Gun:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.x = 100
        self.y = 450
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
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

        #print(math.degrees(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = BLACK

    def draw(self):
        x = self.x
        y = self.y
        l = max(self.f2_power, 20)
        h = 5
        pygame.draw.polygon(self.screen,
                            self.color,
                            ((x, y),
                             (x + l * math.cos(self.an), y - l * math.sin(-self.an)),
                             (x + l * math.cos(-self.an) - h * math.sin(-self.an), y - l * math.sin(-self.an) - h * math.cos(-self.an)),
                             (x - h * math.sin(-self.an), y - h * math.cos(-self.an)),
                             (x, y)))


class Target:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = 0
        self.vy = rnd(10, 20)
        color = self.color = RED

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
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
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


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
topic = "Name: "
Text = topic

clock = pygame.time.Clock()
gun = Gun(screen)
target = []
for i in range(2):
    target += [Target(screen)]
finished = False
point = 0

while not finished:
    screen.fill(WHITE)
    Points = str(point)
    for t in target:
        t.draw()
        t.move()
    textsurface = myfont.render(Points, False, (0, 0, 0))
    point = 0
    screen.blit(textsurface, (10, 10))

    gun.draw()

    for b in balls:
        if b.live < 0:
            balls.remove(b)
        b.draw()
        b.move()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for t in target:
        for b in balls:
            if b.hittest(t) and t.live:
                t.hit()
                t.new_target()
        point += t.points

    gun.power_up()


pygame.quit()
