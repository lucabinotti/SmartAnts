import sys
import time
import random
import pygame
from pygame.locals import *
from simulation import Simulation


GAME_X1 = 0
GAME_Y1 = 0
GAME_X2 = 800
GAME_Y2 = 800

# Layout 1
# POPULATION_SIZE = 1000
# DOT_LIFE = 600
# TARGET = [GAME_X2 / 2, GAME_Y1 + 50]
# SPAWN = [GAME_X2 / 2, GAME_Y2 - 50]
# WALLS = [
#     # x, y, w, h
#     [GAME_X1, GAME_Y2 / 2, GAME_X2 * 3/5, 10]
# ]

# Layout 2
POPULATION_SIZE = 50
DOT_LIFE = 800
TARGET = [GAME_X2 - 40, 40]
SPAWN = [40, GAME_Y2 - 40]
WALLS = [
    # x, y, w, h
    [80*i, GAME_Y2 - 80 - 80*i, 80, 10] for i in range(0, 9)
] + [[80 + 80*i, GAME_Y2 - 80*i, 80, 10] for i in range(1, 9)] + \
    [[80 + 80*i, GAME_Y2 - 160 - 80*i, 10, 80] for i in range(0, 9)] + \
    [[160 + 80*i, GAME_Y2 - 80 - 80*i, 10, 80] for i in range(0, 9)]

# Layout 3
# POPULATION_SIZE = 1000
# DOT_LIFE = 1500
# TARGET = [GAME_X2 - 60, 60]
# SPAWN = [60, GAME_Y2 - 60]
# WALLS = [
#     # Outer walls
#     [50, 50, 700, 10], [50, 750, 700, 10], [50, 50, 10, 700], [750, 50, 10, 700],
#
#     # Inner walls - Horizontal layers
#     [100, 150, 600, 10], [150, 250, 500, 10], [100, 350, 600, 10],
#     [150, 450, 500, 10], [100, 550, 600, 10], [150, 650, 500, 10],
#
#     # Inner walls - Vertical layers
#     [150, 150, 10, 600], [250, 100, 10, 600], [350, 150, 10, 600],
#     [450, 100, 10, 600], [550, 150, 10, 600], [650, 100, 10, 600]
# ]



if __name__ == "__main__":
    Simulation(simulation_display=[GAME_X1, GAME_Y1, GAME_X2, GAME_Y2], population_size=POPULATION_SIZE, target=TARGET, dot_life=DOT_LIFE, spawn=SPAWN, walls=WALLS)
