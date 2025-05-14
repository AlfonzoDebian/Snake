import pygame
import random
import os

# Inicio
pygame.init()
pygame.mixer.init()

# Colores y constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
WHITE, RED, BLACK, SNAKE_GREEN = (255, 255, 255), (255, 0, 0), (0, 0, 0), (35, 45, 40)
INIT_VELOCITY, SNAKE_SIZE, FPS = 5, 30, 60

# Recursos
BG_INTRO = pygame.image.load("Screen/Intro1.png")
BG_GAME = pygame.image.load("Screen/bg2.png")
BG_OUTRO = pygame.image.load("Screen/outro.png")
MUSIC_BGM = 'Music/bgm.mp3'
MUSIC_GAMEOVER = 'Music/bgm2.mp3'

# Fuente personalizada
FONT_PATH = "Pixellari.ttf"  # Asegúrate de que este archivo exista
font = pygame.font.Font(FONT_PATH, 35)

# Ventana
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Snake")
clock = pygame.time.Clock()

def text_screen(text, color, x, y):
    gameWindow.blit(font.render(text, True, color), (x, y))

def plot_snake(gameWindow, snk_list, direction):
    now = pygame.time.get_ticks()
    tongue_show = (now // 3000) % 2 == 0 and now % 3000 < 300

    for i, pos in enumerate(snk_list):
        x, y = pos
        body_color = (34, 139, 34) if i % 2 == 0 else (0, 100, 0)

        if i == len(snk_list) - 1:  # Cabeza de la serpiente
            pygame.draw.rect(gameWindow, body_color, (x, y, SNAKE_SIZE, SNAKE_SIZE))

            eye_radius = 6
            pupil_radius = 2

            if direction in ("UP", "DOWN"):
                eye1_pos = (x + 8, y + 5) if direction == "UP" else (x + 8, y + 20)
                eye2_pos = (x + 22, y + 5) if direction == "UP" else (x + 22, y + 20)
                pupil_offset = (0, -2) if direction == "UP" else (0, 2)
                tongue_start = (x + 15, y) if direction == "UP" else (x + 15, y + SNAKE_SIZE)
                tongue_dir = (0, -1) if direction == "UP" else (0, 1)
            elif direction in ("LEFT", "RIGHT"):
                eye1_pos = (x + 5, y + 8) if direction == "LEFT" else (x + 20, y + 8)
                eye2_pos = (x + 5, y + 22) if direction == "LEFT" else (x + 20, y + 22)
                pupil_offset = (-2, 0) if direction == "LEFT" else (2, 0)
                tongue_start = (x, y + 15) if direction == "LEFT" else (x + SNAKE_SIZE, y + 15)
                tongue_dir = (-1, 0) if direction == "LEFT" else (1, 0)
            else:
                eye1_pos, eye2_pos = (x + 8, y + 8), (x + 20, y + 8)
                pupil_offset = (0, 0)
                tongue_start = (x + 15, y)
                tongue_dir = (0, -1)

            # Ojos y pupilas
            pygame.draw.circle(gameWindow, WHITE, eye1_pos, eye_radius)
            pygame.draw.circle(gameWindow, WHITE, eye2_pos, eye_radius)
            pygame.draw.circle(gameWindow, BLACK, (eye1_pos[0] + pupil_offset[0], eye1_pos[1] + pupil_offset[1]), pupil_radius)
            pygame.draw.circle(gameWindow, BLACK, (eye2_pos[0] + pupil_offset[0], eye2_pos[1] + pupil_offset[1]), pupil_radius)

            # Brillo de ojos
            pygame.draw.circle(gameWindow, WHITE, (eye1_pos[0] - 2, eye1_pos[1] - 2), 1)
            pygame.draw.circle(gameWindow, WHITE, (eye2_pos[0] - 2, eye2_pos[1] - 2), 1)

            # Boca
            pygame.draw.line(gameWindow, BLACK, (x + 12, y + 27), (x + 18, y + 27), 2)

            # Lengua
            if tongue_show:
                t1 = (tongue_start[0] + tongue_dir[0] * 10, tongue_start[1] + tongue_dir[1] * 10)
                t2 = (t1[0] + 4, t1[1] + 4)
                t3 = (t1[0] - 4, t1[1] + 4)
                pygame.draw.line(gameWindow, RED, tongue_start, t1, 2)
                pygame.draw.line(gameWindow, RED, t1, t2, 2)
                pygame.draw.line(gameWindow, RED, t1, t3, 2)
        else:
            pygame.draw.rect(gameWindow, body_color, (x, y, SNAKE_SIZE, SNAKE_SIZE))

def read_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read())
    return 0

def update_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def welcome():
    pygame.mixer.music.load(MUSIC_BGM)
    pygame.mixer.music.play(-1)

    while True:
        gameWindow.blit(BG_INTRO, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameloop()

        pygame.display.update()
        clock.tick(FPS)

def gameloop():
    snake_x, snake_y = 45, 55
    velocity_x, velocity_y = INIT_VELOCITY, 0
    snk_list = [(snake_x, snake_y - SNAKE_SIZE), (snake_x, snake_y)]
    snk_length = 2
    score, highscore = 0, read_highscore()
    food_x, food_y = random.randint(20, SCREEN_WIDTH // 2), random.randint(20, SCREEN_HEIGHT // 2)
    last_direction = "RIGHT"

    # Statusimg = pygame.image.load("sprite/Status.png")
    # Statusimg = pygame.transform.scale(Statusimg, (160, 160))

    while True:
        gameWindow.blit(BG_GAME, (0, 0))
        text_screen(f"Puntos: {score}  Record: {highscore}", WHITE, 5, 5)
        pygame.draw.rect(gameWindow, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                new_direction = None
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    new_direction = "RIGHT"
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    new_direction = "LEFT"
                if event.key in (pygame.K_UP, pygame.K_w):
                    new_direction = "UP"
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    new_direction = "DOWN"

                if new_direction and not (last_direction == "LEFT" and new_direction == "RIGHT" or 
                                          last_direction == "RIGHT" and new_direction == "LEFT" or
                                          last_direction == "UP" and new_direction == "DOWN" or
                                          last_direction == "DOWN" and new_direction == "UP"):
                    last_direction = new_direction
                    if new_direction == "RIGHT":
                        velocity_x, velocity_y = INIT_VELOCITY, 0
                    elif new_direction == "LEFT":
                        velocity_x, velocity_y = -INIT_VELOCITY, 0
                    elif new_direction == "UP":
                        velocity_x, velocity_y = 0, -INIT_VELOCITY
                    elif new_direction == "DOWN":
                        velocity_x, velocity_y = 0, INIT_VELOCITY

        snake_x += velocity_x
        snake_y += velocity_y
        snk_list.append((snake_x, snake_y))

        if len(snk_list) > snk_length:
            snk_list.pop(0)

        if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
            score += 10
            food_x, food_y = random.randint(20, SCREEN_WIDTH // 2), random.randint(20, SCREEN_HEIGHT // 2)
            snk_length += 5
            highscore = max(highscore, score)

        if (snake_x < 0 or snake_x > SCREEN_WIDTH or 
            snake_y < 0 or snake_y > SCREEN_HEIGHT or 
            (snake_x, snake_y) in snk_list[:-1]):
            update_highscore(highscore)
            gameWindow.blit(BG_OUTRO, (0, 0))
            text_screen(f"Puntuación: {score}", WHITE, 385, 350)
            pygame.mixer.music.load(MUSIC_GAMEOVER)
            pygame.mixer.music.play(-1)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        welcome()
                pygame.display.update()

        plot_snake(gameWindow, snk_list, last_direction)
      #  gameWindow.blit(Statusimg, (0, 420))
        pygame.display.update()
        clock.tick(FPS)

welcome()
