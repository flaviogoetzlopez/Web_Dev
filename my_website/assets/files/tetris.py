"""
when a line si full of cubes then dissappear all cubes in he line and make everythig fall 1 block down while guranteein that same colored shpes stay togethr and dont separate


Solo nos quedan 3 cosas por resolver.
Musica, next piece, score, double screen, colors correct etc.

"""

class block():
    def __init__(self):
        self.number_square = random.randint(1, 7)
        self.x = 4 * square_size
        self.y = 0
        self.timer = time.time()
        self.piece_orientation = random.randint(1, 4)
        self.color = random.randint(0, 10)



    def define_block(self):
        if self.number_square == 1:
            #cuadrado
            self.block_placement = (pygame.Rect(self.x, self.y, 2 * square_size, 2 * square_size), pygame.Rect(self.x, self.y, 2 * square_size, 2 * square_size))
        elif self.number_square == 2:
            # Linea
            if self.piece_orientation == 1 or self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x, self.y, square_size * 4, square_size), pygame.Rect(self.x, self.y, square_size * 4, square_size))
            else:
                self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 4 * square_size), pygame.Rect(self.x + square_size, self.y, square_size, 4 * square_size))
        elif self.number_square == 3:
            #   |
            #  |||
            if self.piece_orientation == 1:
                self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
            elif self.piece_orientation == 2:
                self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y + square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
            elif self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x + square_size, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
            elif self.piece_orientation == 4:
                self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
        elif self.number_square == 4:
            # ele izq
            if self.piece_orientation == 1:
                self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size), pygame.Rect(self.x + 2 * square_size, self.y, square_size, square_size))
            elif self.piece_orientation == 2:
                self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size), pygame.Rect(self.x + 2 * square_size, self.y + 2 * square_size, square_size, square_size))
            elif self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size), pygame.Rect(self.x, self.y + 2 * square_size, square_size, square_size))
            elif self.piece_orientation == 4:
                self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size), pygame.Rect(self.x, self.y, square_size, square_size))
        elif self.number_square == 5:
            # ele der
            if self.piece_orientation == 1:
                self.block_placement = (pygame.Rect(self.x, self.y, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
            elif self.piece_orientation == 2:
                self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
            elif self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
            elif self.piece_orientation == 4:
                self.block_placement = (pygame.Rect(self.x, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
        elif self.number_square == 6:
            # Cuello chueco izq
            if self.piece_orientation == 1 or self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size, 2 * square_size), pygame.Rect(self.x + square_size, self.y, square_size, 2 * square_size))
            elif self.piece_orientation == 2 or self.piece_orientation == 4:
                self.block_placement = (pygame.Rect(self.x, self.y, 2 * square_size, square_size), pygame.Rect(self.x + square_size, self.y + square_size, 2 * square_size, square_size))
        elif self.number_square == 7:
            # Cuello chueco der
            if self.piece_orientation == 1 or self.piece_orientation == 3:
                self.block_placement = (pygame.Rect(self.x, self.y, square_size, 2 * square_size), pygame.Rect((self.x + square_size, self.y + square_size, square_size , 2 * square_size))) # 5-14=6-15
            elif self.piece_orientation == 2 or self.piece_orientation == 4:
                self.block_placement = (pygame.Rect(self.x, self.y + square_size, 2 * square_size, square_size), pygame.Rect((self.x + square_size, self.y, 2 * square_size , square_size))) # 5-14=6-15



    def draw_block(self):
        pygame.draw.rect(win, farben[self.color], self.block_placement[0])
        pygame.draw.rect(win, farben[self.color], self.block_placement[1])



    def change_pos(self):
        if pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(self.block_placement[0]) and pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(self.block_placement[1]):
            if Fast:
                self.y += square_size
            elif 0.5 <= time.time() - self.timer:
                self.timer = time.time()
                self.y += square_size



def draw_screen():

    draw_background()
    draw_pieces()
    draw_grid()
    clock.tick(10)
    pygame.display.update()

def draw_background():
    win.fill(farben["blue"])
def draw_grid():
    for width_pos in range(1, 10):
        pygame.draw.line(win, farben["white"], (square_size * width_pos, 0), (square_size * width_pos, HEIGHT))

    for height_pos in range(1, 20):
        pygame.draw.line(win, farben["white"], (0, square_size * height_pos), (WIDTH, square_size * height_pos))

def draw_pieces():
    current_block.define_block()
    current_block.draw_block()
    for block in block_list:                                                            # if there aint none we gonn do shit
        block.define_block()
        block.draw_block()


import pygame
import random
import time
WIDTH, HEIGHT = 300, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
square_size = WIDTH // 10
block_list = []
farben = {"black": (0, 0, 0), "white": (255, 255, 255), "blue": (0, 0, 255), 0: (255, 0, 0), 1: (0, 255, 255), 2: (0, 255, 0), 3:(102, 0, 102), 4: (0, 153, 153), 5: (0, 128, 255), 6: (127, 0, 255), 7: (76, 153, 0), 8: (255, 178, 102), 9: (153, 255, 153), 10: (204, 0, 102)}
clock = pygame.time.Clock()


current_block = block()
current_block.piece_orientation = random.randint(1, 4)
current_block.define_block()
current_block.draw_block()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_block.piece_orientation += 1
                # TODO: define experiment position
                current_block.define_block()





                if (pygame.Rect(0, 0, WIDTH, HEIGHT).contains(current_block.block_placement[0]) and pygame.Rect(0, 0, WIDTH, HEIGHT).contains(current_block.block_placement[1])): # experiment position
                    print("Estoy dentro de la pantalla")
                    for iteration_block in block_list:
                        if (iteration_block.block_placement[0].colliderect(current_block.block_placement[0]) or
                        iteration_block.block_placement[0].colliderect(current_block.block_placement[1]) or
                        iteration_block.block_placement[1].colliderect(current_block.block_placement[0]) or
                        iteration_block.block_placement[1].colliderect(current_block.block_placement[1])):



                            current_block.piece_orientation -= 1
                            break
                    if current_block.piece_orientation == 5:
                        current_block.piece_orientation = 1

                    """
                    Tengo que arreglar el peo de las piezas que se quedan atoradas en el costado de la pantalla y que no se giren cuando no se puede -> esotiene que ver con la rotacion de las piezas
                    las piezas no pueden girar si, caeran encima de una pared o si caeran encima de otro bloque.


                    Vamos a decir, que hay un evento, que define el turn, yo antes de ese evento, pondre las siguientes condiciones:
                    # lo que se va a volver la figura despues del turn = next_block
                    if next_block inside of screen then do
                    if next block not colliding with any other blocks, then do.

                    the only thing that i need, is to define next block, the rest is done easily
                    """





    keys = pygame.key.get_pressed()
    Fast = False
    if keys[pygame.K_DOWN]:
        Fast = True
    if keys[pygame.K_RIGHT]:
        if pygame.Rect(0, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[1])) and pygame.Rect(0, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[0])):
            if block_list != []:
                for iteration_block in block_list:
                    if (iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0] + square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
                            iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0] + square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3])) or
                            iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0] + square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
                            iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0] + square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3]))):
                        break
                else:
                    current_block.x += square_size
            else:
                current_block.x += square_size
    elif keys[pygame.K_LEFT]:
        if pygame.Rect(square_size, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[1])) and pygame.Rect(square_size, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[0])):
            if block_list != []:
                for iteration_block in block_list:
                    if (iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0] - square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
                            iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0] - square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3])) or
                            iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0] - square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
                            iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0] - square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3]))):
                        break
                else:
                    current_block.x -= square_size
            else:
                current_block.x -= square_size







    if not (pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(current_block.block_placement[0]) and pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(current_block.block_placement[1])):
        block_list.append(current_block)
        current_block = block()
        current_block.define_block()


    for iteration_block in block_list:
        if iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0], current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3] + square_size)) or\
                iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0], current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3] + square_size)) or\
                iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0], current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3] + square_size)) or\
                iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0], current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3] + square_size)):

            block_list.append(current_block)
            current_block = block()
            current_block.define_block()



    current_block.change_pos()
    draw_screen()





# """
# when a line si full of cubes then dissappear all cubes in he line and make everythig fall 1 block down while guranteein that same colored shpes stay togethr and dont separate
#
#
# Solo nos quedan 3 cosas por resolver.
# Musica, next piece, score, double screen, colors correct etc.
#
# """
#
# class block():
#     def __init__(self):
#         self.number_square = random.randint(1, 7)
#         self.x = 4 * square_size
#         self.y = 0
#         self.timer = time.time()
#         self.piece_orientation = random.randint(1, 4)
#         self.color = random.randint(0, 10)
#
#
#
#     def define_block(self):
#         if self.number_square == 1:
#             #cuadrado
#             self.points = [(150, 150), (200, 120), (210, 150), (260, 140), (210, 250)]
#         elif self.number_square == 2:
#             # Linea
#             if self.piece_orientation == 1 or self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x, self.y, square_size * 4, square_size), pygame.Rect(self.x, self.y, square_size * 4, square_size))
#             else:
#                 self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 4 * square_size), pygame.Rect(self.x + square_size, self.y, square_size, 4 * square_size))
#         elif self.number_square == 3:
#             #   |
#             #  |||
#             if self.piece_orientation == 1:
#                 self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
#             elif self.piece_orientation == 2:
#                 self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y + square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
#             elif self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x + square_size, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
#             elif self.piece_orientation == 4:
#                 self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
#         elif self.number_square == 4:
#             # ele izq
#             if self.piece_orientation == 1:
#                 self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size), pygame.Rect(self.x + 2 * square_size, self.y, square_size, square_size))
#             elif self.piece_orientation == 2:
#                 self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size), pygame.Rect(self.x + 2 * square_size, self.y + 2 * square_size, square_size, square_size))
#             elif self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size), pygame.Rect(self.x, self.y + 2 * square_size, square_size, square_size))
#             elif self.piece_orientation == 4:
#                 self.block_placement = (pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size), pygame.Rect(self.x, self.y, square_size, square_size))
#         elif self.number_square == 5:
#             # ele der
#             if self.piece_orientation == 1:
#                 self.block_placement = (pygame.Rect(self.x, self.y, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
#             elif self.piece_orientation == 2:
#                 self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
#             elif self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x + 2 * square_size, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x, self.y + square_size, square_size * 3, square_size))
#             elif self.piece_orientation == 4:
#                 self.block_placement = (pygame.Rect(self.x, self.y + 2 * square_size, square_size, square_size), pygame.Rect(self.x + square_size, self.y, square_size, 3 * square_size))
#         elif self.number_square == 6:
#             # Cuello chueco izq
#             if self.piece_orientation == 1 or self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x, self.y + square_size, square_size, 2 * square_size), pygame.Rect(self.x + square_size, self.y, square_size, 2 * square_size))
#             elif self.piece_orientation == 2 or self.piece_orientation == 4:
#                 self.block_placement = (pygame.Rect(self.x, self.y, 2 * square_size, square_size), pygame.Rect(self.x + square_size, self.y + square_size, 2 * square_size, square_size))
#         elif self.number_square == 7:
#             # Cuello chueco der
#             if self.piece_orientation == 1 or self.piece_orientation == 3:
#                 self.block_placement = (pygame.Rect(self.x, self.y, square_size, 2 * square_size), pygame.Rect((self.x + square_size, self.y + square_size, square_size , 2 * square_size))) # 5-14=6-15
#             elif self.piece_orientation == 2 or self.piece_orientation == 4:
#                 self.block_placement = (pygame.Rect(self.x, self.y + square_size, 2 * square_size, square_size), pygame.Rect((self.x + square_size, self.y, 2 * square_size , square_size))) # 5-14=6-15
#
#
#
#     def draw_block(self):
#         self.shape = pygame.draw.polygon(win, farben[self.color], self.points)
#
#
#
#     def change_pos(self):
#         if pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(self.block_placement[0]) and pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(self.block_placement[1]):
#             if Fast:
#                 self.y += square_size
#             elif 0.5 <= time.time() - self.timer:
#                 self.timer = time.time()
#                 self.y += square_size
#
#
#
# def draw_screen():
#     draw_background()
#     draw_pieces()
#     draw_grid()
#     # points = [(150, 150), (200, 120), (210, 150), (260, 140), (210, 250)]
#     # polygon = pygame.draw.polygon(win, (0,0,0), points)
#
#     clock.tick(10)
#     pygame.display.update()
#
# def draw_background():
#     win.fill(farben["blue"])
# def draw_grid():
#     for width_pos in range(1, 10):
#         pygame.draw.line(win, farben["white"], (square_size * width_pos, 0), (square_size * width_pos, HEIGHT))
#
#     for height_pos in range(1, 20):
#         pygame.draw.line(win, farben["white"], (0, square_size * height_pos), (WIDTH, square_size * height_pos))
#
# def draw_pieces():
#     current_block.define_block()
#     current_block.draw_block()
#     for block in block_list:                                                            # if there aint none we gonn do shit
#         block.define_block()
#         block.draw_block()
#
#
# import pygame
# import random
# import time
# WIDTH, HEIGHT = 300, 600
# win = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tetris")
# square_size = WIDTH // 10
# block_list = []
# farben = {"black": (0, 0, 0), "white": (255, 255, 255), "blue": (0, 0, 255), 0: (255, 0, 0), 1: (0, 255, 255), 2: (0, 255, 0), 3:(102, 0, 102), 4: (0, 153, 153), 5: (0, 128, 255), 6: (127, 0, 255), 7: (76, 153, 0), 8: (255, 178, 102), 9: (153, 255, 153), 10: (204, 0, 102)}
# clock = pygame.time.Clock()
#
#
# current_block = block()
# current_block.piece_orientation = random.randint(1, 4)
# current_block.define_block()
# current_block.draw_block()
#
#
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 current_block.piece_orientation += 1
#                 # TODO: define experiment position
#                 current_block.define_block()
#
#
#
#
#
#                 if (pygame.Rect(0, 0, WIDTH, HEIGHT).contains(current_block.block_placement[0]) and pygame.Rect(0, 0, WIDTH, HEIGHT).contains(current_block.block_placement[1])): # experiment position
#                     print("Estoy dentro de la pantalla")
#                     for iteration_block in block_list:
#                         if (iteration_block.block_placement[0].colliderect(current_block.block_placement[0]) or
#                                 iteration_block.block_placement[0].colliderect(current_block.block_placement[1]) or
#                                 iteration_block.block_placement[1].colliderect(current_block.block_placement[0]) or
#                                 iteration_block.block_placement[1].colliderect(current_block.block_placement[1])):
#
#
#
#                             current_block.piece_orientation -= 1
#                             break
#                     if current_block.piece_orientation == 5:
#                         current_block.piece_orientation = 1
#
#                     """
#                     Tengo que arreglar el peo de las piezas que se quedan atoradas en el costado de la pantalla y que no se giren cuando no se puede -> esotiene que ver con la rotacion de las piezas
#                     las piezas no pueden girar si, caeran encima de una pared o si caeran encima de otro bloque.
#
#
#                     Vamos a decir, que hay un evento, que define el turn, yo antes de ese evento, pondre las siguientes condiciones:
#                     # lo que se va a volver la figura despues del turn = next_block
#                     if next_block inside of screen then do
#                     if next block not colliding with any other blocks, then do.
#
#                     the only thing that i need, is to define next block, the rest is done easily
#                     """
#
#
#
#
#
#     keys = pygame.key.get_pressed()
#     Fast = False
#     if keys[pygame.K_DOWN]:
#         Fast = True
#     if keys[pygame.K_RIGHT]:
#         if pygame.Rect(0, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[1])) and pygame.Rect(0, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[0])):
#             if block_list != []:
#                 for iteration_block in block_list:
#                     if (iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0] + square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
#                             iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0] + square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3])) or
#                             iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0] + square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
#                             iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0] + square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3]))):
#                         break
#                 else:
#                     current_block.x += square_size
#             else:
#                 current_block.x += square_size
#     elif keys[pygame.K_LEFT]:
#         if pygame.Rect(square_size, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[1])) and pygame.Rect(square_size, 0, WIDTH - square_size, HEIGHT).contains((current_block.block_placement[0])):
#             if block_list != []:
#                 for iteration_block in block_list:
#                     if (iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0] - square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
#                             iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0] - square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3])) or
#                             iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0] - square_size, current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3])) or
#                             iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0] - square_size, current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3]))):
#                         break
#                 else:
#                     current_block.x -= square_size
#             else:
#                 current_block.x -= square_size
#
#
#
#
#
#
#
#     if not (pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(current_block.block_placement[0]) and pygame.Rect(- square_size, 0, WIDTH + 3 * square_size, HEIGHT - square_size).contains(current_block.block_placement[1])):
#         block_list.append(current_block)
#         current_block = block()
#         current_block.define_block()
#
#
#     for iteration_block in block_list:
#         if iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[0][0], current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3] + square_size)) or \
#                 iteration_block.block_placement[0].colliderect(pygame.Rect(current_block.block_placement[1][0], current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3] + square_size)) or \
#                 iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[0][0], current_block.block_placement[0][1], current_block.block_placement[0][2], current_block.block_placement[0][3] + square_size)) or \
#                 iteration_block.block_placement[1].colliderect(pygame.Rect(current_block.block_placement[1][0], current_block.block_placement[1][1], current_block.block_placement[1][2], current_block.block_placement[1][3] + square_size)):
#
#             block_list.append(current_block)
#             current_block = block()
#             current_block.define_block()
#
#
#
#     current_block.change_pos()
#     draw_screen()
#
