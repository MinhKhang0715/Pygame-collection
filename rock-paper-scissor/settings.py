import sys
from pygame import font

font.init()
game_font = font.Font('Pixeltype.ttf', 50)
SCREEN_WITDH = 1200
SCREEN_HEIGHT = 800
IMAGE_SIZE_DEFAULT = 200
root_dir = sys.path[0]
FRAME_RATE = 10