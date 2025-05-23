# The Snake by Alfonzo [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)





# 🐍 The Purple Snake

Este es un juego del tipo *Snake* (la serpiente), hecho con Python y Pygame. ¡Tú controlas una serpiente que crece cada vez que come comida! Pero si se choca con las paredes o consigo misma... ¡pierdes!

---

## 🎮 ¿Cómo funciona el juego?

- Usa las flechas o las teclas **W, A, S, D** para mover la serpiente.
- Cada vez que come una comida, ¡crece!
- Si te chocas con la pared o con tu cuerpo, se acaba el juego.
- Se guarda el **récord más alto** en un archivo para saber si logras superar tu mejor puntuación.

---

## 🧠 ¿Qué hace cada parte del código?

### 1. 🔧 Importar herramientas

```python
import pygame
import random
import os
```

- `pygame`: Librería para hacer videojuegos.
- `random`: Para que la comida aparezca en lugares al azar.
- `os`: Para guardar y leer el récord.

---

### 2. 📏 Configuraciones del juego

```python
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
INIT_VELOCITY = 5
SNAKE_SIZE = 30
FPS = 60
```

- Tamaño de la ventana, velocidad de la serpiente, tamaño de los bloques, y cuántas veces se actualiza por segundo.

---

### 3. 🎨 Colores y recursos

```python
WHITE, RED, BLACK, PURPLE, SNAKE_GREEN = ...
BG_INTRO = pygame.image.load("Screen/Intro1.png")
MUSIC_BGM = 'Music/bgm.mp3'
```

- Colores usados para el texto, la comida y la serpiente.
- Carga imágenes y música que se usan durante el juego.

---

### 4. 🖥️ Ventana y texto

```python
pygame.display.set_mode(...)
pygame.display.set_caption("The Purple Snake - The Snake")
font = pygame.font.SysFont('Harrington', 35)
```

- Crea la ventana del juego, le pone un título y define una fuente para el texto.

---

### 5. ✍️ Funciones importantes

```python
def text_screen(text, color, x, y):
```

- Muestra texto (como los puntos).

```python
def plot_snake(gameWindow, color, snk_list):
```

- Dibuja la serpiente, usando una lista de partes de su cuerpo.

```python
def read_highscore() / update_highscore(score):
```

- Leer y guardar el récord más alto del jugador.

---

### 6. 👋 Pantalla de inicio

```python
def welcome():
```

- Muestra una imagen de bienvenida y espera que presiones Enter para jugar.
- Comienza la música del juego.

---

### 7. 🐍 El juego en sí

```python
def gameloop():
```

- **Empieza el juego**: se crea la serpiente, la comida y la puntuación.
- **Teclado**: mueve la serpiente sin dejar girar en dirección contraria.
- **Comida**: si se acerca a la comida, gana puntos y crece.
- **Choques**:
  - Si toca las paredes → pierdes.
  - Si se toca a sí misma → pierdes.
- **Game Over**: muestra una imagen de fin de juego y espera que presiones Enter para volver a comenzar.

---

### 8. 🚀 Iniciar el juego

```python
welcome()
```

- Llama a la pantalla de inicio cuando abres el juego.

---

## ✅ Cosas necesarias para que funcione

- Python instalado
- Librería Pygame (`pip install pygame`)
- Carpetas:
  - `Screen/` con las imágenes (`Intro1.png`, `bg2.jpg`, `outro.png`)
  - `Music/` con las canciones (`bgm.mp3`, `bgm2.mp3`)
- Archivo `highscore.txt` (opcional, se crea solo)



![](./SN%20(5).png)


https://www.canva.com/design/DAGm9Mhfyn4/-YSF1QxNFA31cahiliXB7g/edit?utm_content=DAGm9Mhfyn4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

¡Y eso es todo! Ahora puedes leer el código, entenderlo paso a paso, y modificarlo para hacerlo aún más divertido. 🎉

