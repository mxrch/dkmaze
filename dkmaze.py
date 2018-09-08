import pygame
import constants
import classes
from pygame import *
from constants import *

pygame.init()

pygame.display.set_icon(icon)
pygame.display.set_caption("DK's Maze !")

window = pygame.display.set_mode(size)
Game = classes.Game(window)

pygame.key.set_repeat(400, 30)
run = 1
ingame = 0
level = 1
MOVESELECT = USEREVENT + 1
WIN = USEREVENT + 1
pygame.time.set_timer(MOVESELECT, 250)
Game.select(1)
while run:
    while ingame == 0:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOVESELECT:
                Game.select(level, True)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    confirmsound.play()
                    Donkey = classes.Donkey(window, level)
                    Game.initlevel(level)
                    pos_donkey = [0, 0]
                    home = 0
                    ingame = 1
                    Game.level()
                    pygame.time.set_timer(MOVESELECT, 0)
                if event.key == K_DOWN or event.key == K_UP:
                    if level == 1:
                        level = 2
                    else:
                        level = 1
                    Game.select(level)
                if event.key == K_ESCAPE:
                    exit()


    while ingame:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Game.level()
                    Donkey.move("up", pos_donkey)
                if event.key == K_DOWN:
                    Game.level()
                    Donkey.move("down", pos_donkey)
                if event.key == K_LEFT:
                    Game.level()
                    Donkey.move("left", pos_donkey)
                if event.key == K_RIGHT:
                    Game.level()
                    Donkey.move("right", pos_donkey)
                if event.key == K_ESCAPE:
                    ingame = 0
                    pygame.time.set_timer(MOVESELECT, 500)
                    Game.home()
                    Game.select(1)
                if Donkey.success(pos_donkey) == True:
                    wonsound.play()
                    pygame.time.set_timer(WIN, 100)
                    while ingame:
                        pygame.time.Clock().tick(30)
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                            if event.type == WIN:
                                Game.level(True)
                                Donkey.winmove(pos_donkey)
                            if event.type == KEYDOWN:
                                if event.key == K_RETURN:
                                    ingame = 0
                                    pygame.time.set_timer(MOVESELECT, 500)
                                    Game.select(1)
                                if event.key == K_ESCAPE:
                                    exit()