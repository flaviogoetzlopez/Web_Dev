def __main__():
    # Imports
    import pygame                                                          # Imports
    import time
    import random
    pygame.mixer.init()


    # Classes
    class sprites():                                                                            # OOP    Class Player/Enemy
        def __init__(self, x, y, width, height, vel, health, character_file_location):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = vel
            self.health = health
            self.num = 0
            self.Free = True
            image = pygame.image.load(character_file_location)
            self.character = pygame.transform.scale(image, (self.width, self.height))
            self.level_fuel = 0



        def move_char(self, keys):                                                                # Bewegung Spieler
            if keys[pygame.K_RIGHT]:
                if self.x + self.vel + self.width <= WIDTH:
                    self.x += self.vel
                    self.num = -90
            elif keys[pygame.K_LEFT]:
                if self.x - self.vel >= 0:
                    self.x -= self.vel
                    self.num = -270
            elif keys[pygame.K_UP]:
                if self.y - self.vel >= 0:
                    self.y -= self.vel
                    self.num = 0

            elif keys[pygame.K_DOWN]:
                if self.y + self.vel + self.height <= HEIGHT:
                    self.y += self.vel
                    self.num = -180

            if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                if self.y + self.vel + self.height <= HEIGHT and self.x + self.vel + self.width <= WIDTH:
                    self.y += self.vel
                    self.x += self.vel
                    self.num = -135

            elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                if self.y + self.vel + self.height <= HEIGHT and self.x - self.vel >= 0:
                    self.y += self.vel
                    self.x -= self.vel
                    self.num = -225


            elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                if self.y - self.vel >= 0 and self.x + self.vel + self.width <= WIDTH:
                    self.y -= self.vel
                    self.x += self.vel
                    self.num = -45

            elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                if self.y - self.vel >= 0 and self.x - self.vel >= 0:
                    self.y -= self.vel
                    self.x -= self.vel
                    self.num = -315


        def move_enemy(self):                                                                                      # Bewegung
            if self.x < spaceship.x:
                self.x += self.vel
            else:
                self.x -= self.vel

            if self.y < spaceship.y:
                self.y += self.vel
            else:
                self.y -= self.vel


        def enemy_remove(self):
            enemy.rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            spaceship.rect = pygame.Rect(spaceship.x, spaceship.y, spaceship.width, spaceship.height)
            if enemy.rect.colliderect(spaceship.rect) and self.Free:
                pygame.mixer.music.load("Assets/Explosion.mp3")
                enemy_list.remove(enemy)
                spaceship.health -= 1
                self.Free = False
                pygame.mixer.music.play()

            if not enemy.rect.colliderect(spaceship.rect):
                self.Free = True



    class bullets():                                                                           # Orientierung Spieler, richtung Kugel
        def __init__(self):
            self.x = spaceship.x
            self.y = spaceship.y
            self.height = 5
            self.width = 5
            self.vel = 10
            if spaceship.num == 0:
                self.velx = 0
                self.vely = -self.vel
            elif spaceship.num == -45:
                self.velx = self.vel
                self.vely = -self.vel
            elif spaceship.num == -90:
                self.velx = self.vel
                self.vely = 0
            elif spaceship.num == -135:
                self.velx = self.vel
                self.vely = self.vel
            elif spaceship.num == -180:
                self.velx = 0
                self.vely = self.vel
            elif spaceship.num == -225:
                self.velx = -self.vel
                self.vely = self.vel
            elif spaceship.num == -270:
                self.velx = -self.vel
                self.vely = 0
            elif spaceship.num == -315:
                self.velx = -self.vel
                self.vely = -self.vel

        def moving(self):
            self.x += self.velx
            self.y += self.vely


            self.active = True
            if self.y < 0 or self.y > HEIGHT or self.x < 0 or self.x > WIDTH:
                self.active = False


    # Functions
    def end_game():
        final_image = pygame.image.load("Assets/ending-screen.jpg")
        pygame.mixer.music.load("Assets/You-Won.mp3")
        pygame.mixer.music.play()
        final_image = win.blit(pygame.transform.scale(final_image, (WIDTH, HEIGHT)), (0, 0))
        pygame.display.update()
        time.sleep(5)
        win.fill(farben["blau"])
        restart()

    def restart():
        font = pygame.font.SysFont("Arial", 72)
        text = font.render("Nochmal Spielen? ", True, farben["orange"])
        text_Rect = text.get_rect()
        text_Rect.center = WIDTH // 2, HEIGHT // 2 - 100
        win.blit(text, text_Rect)


        # text = font.render("Nochmal Spielen? ", True, farben["orange"])
        # text_Rect.center = WIDTH // 2 - 30, HEIGHT // 2
        # win.blit(text, text_Rect)

        font = pygame.font.SysFont("Arial", 32)

        text = font.render("Ja!", True, farben["orange"])
        afirmation_Rect = text.get_rect()
        afirmation_Rect.center = WIDTH // 3, HEIGHT // 2 + 100
        Rect_ja = pygame.draw.rect(win, farben["magenta"], (afirmation_Rect.x, afirmation_Rect.y, 100, 100))
        win.blit(text, (WIDTH // 3 + 15, HEIGHT // 2 + 110))


        text = font.render("Nein!", True, farben["orange"])
        afirmation_Rect = text.get_rect()
        afirmation_Rect.center = WIDTH // 1.5, HEIGHT // 2 + 100
        Rect_Nein = pygame.draw.rect(win, farben["magenta"], (afirmation_Rect.x, afirmation_Rect.y, 100, 100))
        win.blit(text, (WIDTH // 1.5 - 10, HEIGHT // 2 + 110))

        pygame.display.update()
        time_wait = time.time() - 9
        pygame.mixer.music.load("Assets/Music Win.mp3")
        while True:
            pygame.display.update()
            pos = pygame.mouse.get_pos()
            pygame.event.get()


            if  time.time() - time_wait >= 9:
                time_wait = time.time()
                pygame.mixer.music.play()


            if Rect_ja.collidepoint(pos) and pygame.mouse.get_pressed(3)[0]:
                __main__()
            if Rect_Nein.collidepoint(pos) and pygame.mouse.get_pressed(3)[0]:
                pygame.quit()


    def draw_screen():
        if level == 1:
            clock.tick(50)
        elif level == 2:
            clock.tick(60)
        else:
            clock.tick(70)
        draw_background()
        draw_health()
        draw_level()
        draw_level_progress()
        for enemy in enemy_list:
            draw_enemy(enemy)
        draw_character()
        draw_gold()
        for bullet in bullet_list:
            draw_bullet(bullet)
        pygame.display.update()

    def draw_character():
        win.blit(pygame.transform.rotate(spaceship.character, spaceship.num), (spaceship.x, spaceship.y))

    def draw_health():
        pygame.draw.rect(win, farben["rot"], (WIDTH / 1.5, 12, 200, 30))
        pygame.draw.rect(win, farben["gruen2"], (WIDTH / 1.5, 12, spaceship.health * 20, 30))

        if spaceship.health == 0:
            time.sleep(2)
            Game_Over = pygame.image.load("Assets/Game Over Image.jpg")
            Game_Over = pygame.transform.scale(Game_Over, (WIDTH, HEIGHT))
            win.blit(Game_Over, (0, 0))
            pygame.display.update()
            pygame.mixer.music.load("Assets/Game-Over-Sound.mp3")
            pygame.mixer.music.play()
            time.sleep(5)
            win.fill(farben["schwarz"])
            restart()


    def draw_enemy(enemy):
        win.blit(enemy.character, (enemy.x, enemy.y))
    def draw_bullet(bullet):
        pygame.draw.rect(win, farben["magenta"], (bullet.x, bullet.y, bullet.width, bullet.height))
        pygame.display.update()
    def draw_background():
        background = pygame.image.load("Assets/Background_2.jpg")
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        win.blit(background, (0, 0))


    def draw_level():
        text = font.render("Level " + str(level), True, farben["gruen"])
        text_Rect = text.get_rect()
        text_Rect.center = (WIDTH // 2, 25)
        pygame.draw.rect(win, farben["lila"], (text_Rect.x, text_Rect.y, text_Rect.width, text_Rect.height))
        win.blit(text, text_Rect)

    def draw_level_progress():
        pygame.draw.rect(win, farben["lila"], (WIDTH // 10, 12, 200, 30))
        if level == 1:
            pygame.draw.rect(win, farben["gelb"], (WIDTH // 10, 12, 40 * spaceship.level_fuel, 30))
        elif level == 2:
            pygame.draw.rect(win, farben["gelb"], (WIDTH // 10, 12, 20 * spaceship.level_fuel, 30))
        elif level == 3:
            pygame.draw.rect(win, farben["gelb"], (WIDTH // 10, 12, 10 * spaceship.level_fuel, 30))

    def draw_gold():
        pygame.draw.rect(win, farben["gelb"], (x_dot, y_dot, 10, 10))

    def enemy_spawn():
        if level == 1:
            i = random.randint(1, 4)
            if i == 1:
                x = 0
                y = 0
            if i == 2:
                x = WIDTH
                y = 0
            if i == 3:
                x = 0
                y = HEIGHT
            if i == 4:
                x = WIDTH
                y = HEIGHT

        elif level == 2:
            ix = random.randint(1, WIDTH)
            iy = random.randint(1, HEIGHT)
            if ix % 2 == 0:
                if iy % 2:
                    x = 0
                    y = iy
                else:
                    x = WIDTH
                    y = iy
            else:
                if iy % 2:
                    x = ix
                    y = 0
                else:
                    y = HEIGHT
                    x = ix
        elif level == 3:
            x = random.randint(1, WIDTH)
            y = random.randint(1, HEIGHT)

        if level == 1:
            enemy = sprites(x, y, 10, 10, 0.7, 1, "Assets/Enemy.jpg")
        elif level == 2:
            enemy = sprites(x, y, 10, 10, random.randint(4, 10) / 10, 1, "Assets/Enemy.jpg")
        else:
            enemy = sprites(x, y, 10, 10, random.randint(1, 13) / 10, 1, "Assets/Enemy.jpg")


        enemy_list.append(enemy)



# Variables

    farben = {"schwarz": (0, 0, 0), "rot": (255, 0, 0), "gruen": (0, 255, 0), "gruen2": (34, 139, 34), "gelb": (255, 255, 0), "blau": (0, 0, 255), "lila": (128, 0, 128), "orange": (255, 165, 0), "grau": (128, 128, 128), "magenta": (255, 0, 255)}



    # Images and Display
    WIDTH = 1000
    HEIGHT = 600

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Games Talente Flavio Goetz")
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 32)


    clock = pygame.time.Clock()


    spaceship = sprites(WIDTH // 2, HEIGHT // 2, 50, 50, 2, 10, "Assets/Spaceship-Photoshop.png")
    spaceship.move_char(pygame.key.get_pressed())


    timer_set = time.time() - 10

    enemy_list = []
    bullet_list = []

    x_dot = WIDTH // 4
    y_dot = HEIGHT // 2

    # Time
    level = 1
    timer_level = time.time()

    # Main while loop

    win.fill(farben["blau"])
    font = pygame.font.SysFont("Arial", 72)
    text = font.render("Super Earth Guardian", True, farben["gruen2"])
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2 , HEIGHT // 2)
    win.blit(text, textRect)
    pygame.display.update()
    time.sleep(1)



    run = True
    while run:



        if level == 1:
            if spaceship.level_fuel >= 5:
                spaceship.level_fuel = 0
                level += 1
                enemy_list.clear()
                if level == 2 or level == 3:
                    pygame.mixer.music.load("Assets/Level-up-2.mp3")
                    pygame.mixer.music.play()
                    time.sleep(1)
        elif level == 2:
            if spaceship.level_fuel >= 10:
                spaceship.level_fuel = 0
                level += 1
                enemy_list.clear()
                if level == 2 or level == 3:
                    pygame.mixer.music.load("Assets/Level-up-2.mp3")
                    pygame.mixer.music.play()
                    time.sleep(1)
        elif level == 3:
            if spaceship.level_fuel >= 15:
                spaceship.level_fuel = 0
                level += 1
                enemy_list.clear()
                if level == 2 or level == 3:
                    pygame.mixer.music.load("Assets/Level-up-2.mp3")
                    pygame.mixer.music.play()
                    time.sleep(1)


        if level == 4:
            end_game()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = bullets()
                    bullet_list.append(bullet)
        keys = pygame.key.get_pressed()




        for bullet in bullet_list[:]:
            bullet_rect = pygame.Rect((bullet.x, bullet.y, bullet.width, bullet.height))
            enemy_list_2 = enemy_list[:]
            for enemy in enemy_list[:]:
                if bullet_rect.colliderect(enemy):

                    bullet_list.remove(bullet)
                    enemy_list.remove(enemy)
                    pygame.mixer.music.load("Assets/Tiro.mp3")
                    pygame.mixer.music.play()

        # for bullet in bullet_list[len(bullet_list):-1:-1]:
        #     bullet_rect = pygame.Rect((bullet.x, bullet.y, bullet.width, bullet.height))
        #     for enemy in enemy_list[len(bullet_list):-1:-1]:
        #         if bullet_rect.colliderect(enemy):
        #             bullet_list.remove(bullet)
        #             enemy_list.remove(enemy)
        #             pygame.mixer.music.load("Assets/Tiro.mp3")
        #             pygame.mixer.music.play()

            if bullet.y < 0 or bullet.y > HEIGHT or bullet.x < 0 or bullet.x > WIDTH:
                bullet_list.remove(bullet)
            bullet.moving()
            draw_bullet(bullet)


        # Add enemy
        if level == 1:
            if time.time() - timer_set >= 3:
                timer_set = time.time()
                enemy_spawn()
        if level == 2:
            if time.time() - timer_set >= 2:
                timer_set = time.time()
                enemy_spawn()
        if level == 3:
            if time.time() - timer_set >= 1.5:
                timer_set = time.time()
                enemy_spawn()

        for enemy in enemy_list:
            enemy.move_enemy()
            enemy.enemy_remove()




        if pygame.Rect(x_dot, y_dot, 10, 10).colliderect((spaceship.x, spaceship.y, spaceship.width, spaceship.height)):
            x_dot = random.randint(1, WIDTH - 50)
            y_dot = random.randint(1, HEIGHT - 50)
            spaceship.level_fuel += 1
            pygame.mixer.music.load("Assets/Gold Sound.mp3")
            pygame.mixer.music.play()

        # Moving
        spaceship.move_char(keys)

        # Draw screen
        draw_screen()

if __name__ == '__main__':
    __main__()