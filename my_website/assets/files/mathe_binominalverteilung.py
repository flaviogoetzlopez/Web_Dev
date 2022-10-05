n = 20
p = 0.2



n = int(input("Type the amout of possible cases 'n': "))
# k_gross = bool(input("True oder False: "))
# k = int(input("Grosse oder Kleine Wert: "))
p = float(input("Type the probability 'p' of a successful event: "))

import pygame
import time
pygame.font.init()
pygame.display.set_caption("Binomial Distribution")


class binominalverteilung(object):
    def __init__(self, n, pgut):
        self.n = n
        self.pgut = pgut
        self.pschlecht = 1 - pgut

    def formel(self, k):
        import math
        self.k = k
        self.times = self.n - self.k
        self.x = math.factorial(self.n) / (math.factorial(self.k) * math.factorial(self.times))
        self.y = self.pgut ** self.k * self.pschlecht ** self.times
        self.ergebnis = self.x * self.y


class column(object):
    def __init__(self):
        self.width = (WIDTH - 50) / (n + 1)
        self.height = instance_1.ergebnis * (HEIGHT - 100)


def draw_screen():
    text = font.render(str(round(instance_1.ergebnis, 3)), True, colors["yellow"])
    pygame.draw.rect(win, colors["red"], pygame.Rect(width_coordinate + x_level, HEIGHT - size_column.height, size_column.width, size_column.height)) # (x, y, width, height)
    if n <= 50:
        # win.blit(text, (width_coordinate + x_level, HEIGHT - size_column.height - 15)) # (x, y) # pygame.transform.rotozoom(text, 90, 1)
        win.blit(pygame.transform.rotozoom(text, 90, 1), (width_coordinate + x_level, HEIGHT - size_column.height - 100))
    pygame.display.update()

def draw_coordinates():
    pass



# Variables
clock = pygame.time.Clock()
colors = {"green": (0, 255, 255), "red": (255, 0, 0), "yellow": (0, 255, 0)}
WIDTH = 1000
HEIGHT  = 600
FPS = 5
win = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.draw.rect(win, colors["red"], (0, HEIGHT, 20, 20))

instance_1 = binominalverteilung(n, p)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if run == False:
            pygame.quit()

    x_level = 0
    y_factor = HEIGHT - 1

    instance_1.formel(0)
    size_column = column()
    font = pygame.font.SysFont("Arial", 20)

    width_coordinate = 50
    for i in range(11):
        pygame.draw.line(win, colors["yellow"], (10, y_factor), (width_coordinate, y_factor))

        text = font.render(str(i * 10), True, (200, 200, 200))
        win.blit(text, (width_coordinate - 30, y_factor - 20))
        y_factor -= (HEIGHT - 100) / 10


    tamanio_fuente = int(round(500 / n, 0))

    if n < 10:
        tamanio_fuente = 50


    font = pygame.font.SysFont("Arial", tamanio_fuente)


    for k in range(0, instance_1.n + 1):
        instance_1.formel(k)
        size_column = column()
        print(k, instance_1.ergebnis)
        draw_screen()
        x_level += size_column.width

        if k == instance_1.n:
            time.sleep(120)
            run = False
