#установки игры

GAMETILE = "Прыгающий чичан"

WIDTH= 480
HEIGHT= 600
FPS= 60
FONT_NAME = "arial"

#Установки движения игрока

PLAYER_ACC = 0.5
PLAYER_FRICTION= -0.1
PLAYER_GRAV = 0.8
PLAYER_JUMP = -25

#Платформы
PLATFORM_LIST = [(0, HEIGHT-40, WIDTH, 40),
                 (WIDTH//2 - 50, int(HEIGHT * 0.75), 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
YELLOW = (255, 255, 0)