import sys
import pygame
from pygame.locals import*

pygame.init()
SCREEN=pygame.display.set_mode((265,205))
CLOCK=pygame.time.Clock()

img=pygame.image.load('webp.jpg')

img_size=img.get_size()
print(img_size)

while True:
    SCREEN.fill((255.255.255))

    for i in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(img.(0,0))

    pygame.display.update()
    CLOCK.tick(1)

import sys
import pygame
from pygmae.locals import*

pygame.init()
SCREEN=pygame.display.set_mode((300.300))
CLOCK=pygame.font.SysFont(None,30)
txt='Wait...'
txt2='Key Down!'

while True:
    SCREEN.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit
            sys.exit()

    key_event=pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        txt='Left'+txt2
    if key_event[pygame.K_RIGHT]:
        txt='Right'+txt2
    if key_event[pygame.K_UP]:
        txt='up'+txt2
    if key_event[pygame.K_DOWN]:
        txt='Down'+txt2
    if key_event[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    msg=sysfont.render(txt,True,(0,0,0))
    SCREEN.blit(msg,(50,100))
    pygame.display.update()
    CLOCK.tick(60)

import sys
import pygame
from pygame.locals import*
import random

pygame.init()
SCREEN=pygame.display.set_mode((600,600))
CLOCK=pygame.time.Clock()

light_img=pygame.lmage.load('번개.webp')
Lx=[]
Lx=[]
cnt=0

while True:
    SCREEN.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygmae.quit()
            sys.exit()
