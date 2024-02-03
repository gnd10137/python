##cut=0
##n=int(input('정수 입력:'))
##while n>0:
##    cut+=1
##    n//=10
##print('자릿수:%d'%cut)

##cut=0
##n=int(input('정수 입력:'))
##while True:
##    cut+=1
##    n//=10
##print('자릿수:%d'%cut)

import pygame
from pygame.locals import*

pygame.init

screen=pygame.display.set_mode((400,300))
pygame.display.set_saption('Tick tock,Timer')

while True:
    for event in pygame.event.get():

import sys
for event in pygame.event.get():
    if event.type==QUIT:
        pygame.quit()
        sys.exit()

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

pygame.diplay.update()

CLOCK=pygame.time.Clock()
CLOCK.tick(t)

screen.fill((255,255,255))

sysfont=pygame.font.SysFont(None,36)
txt_img=sysfont.rander(Timer:%d'%timer,True,
(255,255,255))
screen.Bilt(txt_img,((50,50))

import sys
import pygame
from pygame.locals import*

pygame.init()
screen=pygame.display.set_mode((400,300))
