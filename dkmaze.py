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

pygame.key.set_repeat(400, 30) # Keys can be repeated if they are kept pressed and held down
run = 1
ingame = 0
level = 1
MOVESELECT = USEREVENT + 1
WIN = USEREVENT + 1
pygame.time.set_timer(MOVESELECT, 250)
Game.select(1)

while run:
    # The main loop

    while ingame == 0:
        # The loop of the home screen

        pygame.time.Clock().tick(30) # Avoid overheating the processor
        for event in pygame.event.get():
            # We're tracking all events
            if event.type == QUIT:
                exit()
            if event.type == MOVESELECT:
                Game.select(level, True)
            if event.type == KEYDOWN:
                if event.key == K_RETURN: # If we select a level, we make an instance of Donkey and initialize the level
                    confirmsound.play()
                    Donkey = classes.Donkey(window, level)
                    Game.initlevel(level)
                    pos_donkey = [0, 0]
                    home = 0
                    ingame = 1
                    Game.level()
                    pygame.time.set_timer(MOVESELECT, 0)
                if event.key == K_DOWN or event.key == K_UP: # The arrows are moved by pressing the Down or Up key
                    if level == 1:
                        level = 2
                    else:
                        level = 1
                    Game.select(level)
                if event.key == K_ESCAPE:
                    exit()


    while ingame:
        # The in-game loop

        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN: # We move Donkey
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
                if Donkey.success(pos_donkey) == True: # We check if we are on the arrival square
                    wonsound.play()
                    pygame.time.set_timer(WIN, 100)
                    while ingame:
                        pygame.time.Clock().tick(30)
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                            if event.type == WIN:
                                Game.level(True)
                                Donkey.winmove(pos_donkey) # We start the victory animation
                            if event.type == KEYDOWN:
                                if event.key == K_RETURN:
                                    ingame = 0
                                    pygame.time.set_timer(MOVESELECT, 500)
                                    Game.select(1)
                                if event.key == K_ESCAPE:
                                    exit()
