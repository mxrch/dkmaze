import pygame
from pygame import *

pygame.init()

size = (450, 450)

select1 = pygame.image.load("resources/select1.png")
select2 = pygame.image.load("resources/select2.png")
select1b = pygame.image.load("resources/select1b.png")
select2b = pygame.image.load("resources/select2b.png")

dkdown = pygame.image.load("resources/dk-sprites/dk_down.png")
dkleft = pygame.image.load("resources/dk-sprites/dk_left.png")
dkright = pygame.image.load("resources/dk-sprites/dk_right.png")
dkup = pygame.image.load("resources/dk-sprites/dk_up.png")
dkwin1 = pygame.image.load("resources/dk-sprites/dk_win1.png")
dkwin2 = pygame.image.load("resources/dk-sprites/dk_win2.png")
dkwin3 = pygame.image.load("resources/dk-sprites/dk_win3.png")
dkwin4 = pygame.image.load("resources/dk-sprites/dk_win4.png")

start = pygame.image.load("resources/start.png")
brick = pygame.image.load("resources/brick.png")
end = pygame.image.load("resources/end.png")

home = pygame.image.load("resources/home.png")
background = pygame.image.load("resources/background.jpg")

success = pygame.image.load("resources/success.png")

icon = pygame.image.load("resources/icon.png")

confirmsound = pygame.mixer.Sound("resources/sounds/confirm.wav")
wonsound = pygame.mixer.Sound("resources/sounds/won.wav")