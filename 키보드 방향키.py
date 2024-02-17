##import sys
##import pygame
##from pygame.locals import*
##
##pygame.init()
##SCREEN=pygame.display.set_mode((300,300))
##CLOCK=pygame.time.Clock()
##
##BLACK=(0,0,0)
##WHITE=(255,255,255)
##
##sysfont=pygame.font.SysFont(None,36)
##txt=sysfont.render('',True,BLACK)
##
##while True:
##     SCREEN.fill(WHITE)
##
##     for event in pygame.event.get():
##          if event.type==QUIT:
##               sys.exit()
##
##          if event.type==KEYDOWN:
##               if event.key==K_UP:
##                    txt=sysfont.render('UP',True,BLACK)
##               if event.key==K_DOWN:
##                    txt=sysfont.render('DOWN',True,BLACK)
##               if event.key==K_LEFT:
##                    txt=sysfont.render('LEFT',True,BLACK)
##               if event.key==K_RIGHT:
##                    txt=sysfont.render('RIGHT',True,BLACK)
##               if event.key==K_ESCAPE:
##                    pygame.quit()
##                    sys.exit()
##
##     SCREEN.blit(txt,(100,120))
##     pygame.display.update()
##     CLOCK.tick(60)

##import sys
##import pygame
##from pygame.locals import*
##
##pygame.init()
##SCREEN=pygame.display.set_mode((600,600))
##CLOCK=pygame.time.Clock()
##
##sysfont=pygame.font.SysFont(None,36)
##txt=sysfont.render('',True,(0,0,0))
##coord=sysfont.render('',True,(0,0,0))
##x,y=0,0
##
##while True:
##     SCREEN.fill((255,255,255))
##
##     for event in pygame.event.get():
##          if event.type==QUIT:
##               pygame.quit()
##               sys.exit()
##
##          if event.type==MOUSEBUTTONDOWN:
##               x,y=event.pos[0],event.pos[1]
##               coord=sysfont.render('(%d,%d)'%(x,y),True,(0,0,0))
##               if event.button==1:
##                    txt=sysfont.render('1',True,(0,0,0))
##               if event.button==2:
##                    txt=sysfont.render('2',True,(0,0,0))
##               if event.button==3:
##                    txt=sysfont.render('3',True,(0,0,0))
##               if event.button==4:
##                    txt=sysfont.render('4',True,(0,0,0))
##               if event.button==5:
##                    txt=sysfont.render('5',True,(0,0,0))
##
##     SCREEN.blit(txt,(285,220))
##     SCREEN.blit(coord,(x,y))
##     pygame.display.update()
##     CLOCK.tick(60)

##import sys
##import pygame
##from pygame.locals import*
##
##pygame.init()
##SCREEN=pygame.display.set_mode((300,300))
##CLOCK=pygame.time.Clock()
##
##sysfont=pygame.font.SysFont(None,36)
##txt=sysfont.render('0',True,(0,0,0))
##n=0
##
##while True:
##     SCREEN.fill((255,255,255))
##
##     for event in pygame.event.get():
##          if event.type==QUIT:
##               pygame.quit()
##               sys.exit()
##
##          if  event.type==KEYDOWN:
##               if event.key==K_UP:
##                    n+=10
##               if event.key==K_DOWN:
##                    n-=10
##               if event.key==K_LEFT:
##                    n*=10
##               if event.key==K_RIGHT:
##                    n//=10
##
##          if event.type==MOUSEBUTTONDOWN:
##               if event.button==1:
##                    n=0
##
##     txt=sysfont.render('%d'%n,True,(0,0,0))
##     SCREEN.blit(txt,(100,120))
##     pygame.display.update()
##     CLOCK.tick(60)

##for i in range(1,11):
##     print(i,end=' ')

a=int(input())
for i in range(1,a):
     print(i,end=' ')
