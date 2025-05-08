import pygame
import random
import os

# Inicialización
pygame.init()
pygame.mixer.init()

# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
WHITE, RED, BLACK, PURPLE, SNAKE_GREEN = (255, 255, 255), (255, 0, 0), (120, 0, 120), (128, 0, 128), (35, 45, 40)
INIT_VELOCITY, SNAKE_SIZE, FPS = 5, 30, 60

# Archivos y recursos
BG_INTRO = pygame.image.load("Screen/Intro1.png")
BG_GAME = pygame.image.load("Screen/bg2.jpg")
BG_OUTRO = pygame.image.load("Screen/outro.png")
MUSIC_BGM = 'Music/bgm.mp3'
MUSIC_GAMEOVER = 'Music/bgm2.mp3'

# Configuración de ventana
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Purple Snake - The Snake")

# Fuente y reloj
font = pygame.font.SysFont('Harrington', 35)
clock = pygame.time.Clock()

def text_screen(text, color, x, y):
    gameWindow.blit(font.render(text, True, color), (x, y))

def plot_snake(gameWindow, color, snk_list):
    for pos in snk_list:
        pygame.draw.rect(gameWindow, color, (*pos, SNAKE_SIZE, SNAKE_SIZE))

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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gameloop()

        pygame.display.update()
        clock.tick(FPS)

def gameloop():
    snake_x, snake_y = 45, 55
    velocity_x, velocity_y = 0, 0
    snk_list, snk_length = [], 1
    score, highscore = 0, read_highscore()
    food_x, food_y = random.randint(20, SCREEN_WIDTH // 2), random.randint(20, SCREEN_HEIGHT // 2)
    last_direction = None  # Para evitar movimientos opuestos inmediatos

    Statusimg = pygame.image.load("Screen/Status.png")

    while True:
        gameWindow.blit(BG_GAME, (0, 0))
        text_screen(f"Puntos: {score}  Record: {highscore}", SNAKE_GREEN, 5, 5)
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

        # Actualizar posición de la serpiente
        snake_x += velocity_x
        snake_y += velocity_y
        snk_list.append((snake_x, snake_y))

        if len(snk_list) > snk_length:
            snk_list.pop(0)

        # Verificar colisión con comida
        if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
            score += 10
            food_x, food_y = random.randint(20, SCREEN_WIDTH // 2), random.randint(20, SCREEN_HEIGHT // 2)
            snk_length += 5
            highscore = max(highscore, score)

        # Verificar colisión con bordes o consigo misma
        if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT or (snake_x, snake_y) in snk_list[:-1]:
            update_highscore(highscore)
            gameWindow.blit(BG_OUTRO, (0, 0))
            text_screen(f"Puntuacion: {score}", WHITE, 385, 350)
            pygame.mixer.music.load(MUSIC_GAMEOVER)
            pygame.mixer.music.play(-1)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        welcome()
                pygame.display.update()

        plot_snake(gameWindow, BLACK, snk_list)
        pygame.display.update()
        clock.tick(FPS)

welcome()
