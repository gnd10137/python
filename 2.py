##cut=0
##n=int(input('정수 입력:'))
##while True:
##    cut+=1
##    n//=10
##    if n<=0:
##         break
##print('자릿수:%d'%cut)

##import sys
##import pygame
##from pygame.locals import*
##
##pygame.init()
##screen=pygame.display.set_mode((400,300))
##pygame.display.set_caption('Tick Tock Timer')
##CLOCK=pygame.time.Clock()
##sysfont=pygame.font.SysFont(None,36)
##timer=0
##
##while True:
##     for event in pygame.event.get():
##          if event.type==QUIT:
##               pygame.quit()
##               sys.exit()
##
##     timer+=1
##     screen.fill((255,255,255))
##     cnt_txt=sysfont.render('Timer:%d'%timer,True,(0,0,0))
##     screen.blit(cnt_txt,(140,140))
##     pygame.display.update()
##     CLOCK.tick(1)

##import pygame
##from pygame.locals import*
##
##pygame.init
##
##screen=pygame.display.set_mode((400,300))
##pygame.display.set_saption('Tick tock,Timer')
##
##while True:
##    for event in pygame.event.get():
##
##import sys
##for event in pygame.event.get():
##    if event.type==QUIT:
##        pygame.quit()
##        sys.exit()
##
##BLACK=(0,0,0)
##WHITE=(255,255,255)
##GREEN=(0,255,0)
##RED=(255,0,0)
##BLUE=(0,0,255)
##
##pygame.diplay.update()
##
##CLOCK=pygame.time.Clock()
##CLOCK.tick(t)
##
##screen.fill((255,255,255))
##
##sysfont=pygame.font.SysFont(None,36)
##txt_img=sysfont.rander(Timer:%d'%timer,True,
##(255,255,255))
##screen.Bilt(txt_img,((50,50))

##List=['a','b','c']
##for s in List:
##     print(s)

##num_list=[1,2,3,4,5]
##sum=0
##for num in num_list:
##     sum+=num
##print('avg:%d'%(sum//5))

##aList=[1,2,3]
##bList=[10,100,1000]
##for a in aList:
##     for b in bList:
##          print(a*b,end=' ')
##     print()

##for i in range(10):
##     print(i,end=' ')

##for i in range(10,21):
##     print(i,end=' ')

##for i in range(1,10,2):
##     print(i, end=' ')

##List=['Noah','Minsu','keily','Yuri']
##for name in List:
##     print('%s,Congratulation.'%name)

##n=int(input('몇 단?'))
##for i in range(1,10):
##     print('%d*%d=%d'%(n,i,n*i))

##for i in range(1,11):
##     print(i,end=' ')

##a=int(input())
##for i in range(1,a+1):
##     print(i,end=' ')

##for i in range(1,101):
##     if i%2==0:
##          print(i,end=' ')

##a=input()
##for i in range(5):
##     print(a,end='')

##a=int(input())
##for i in range(a,51):
##     print(i,end=' ')

##sum=0
##h_list=[159,163,173,158,169]
##for h in h_list:
##     sum+=h
##print('sum:%d'%sum)
##print('avg:%.2f'%(sum/len(h_list)))

##sum=0
##for i in range(5):
##     a=int(input())
##     sum+=a
##print('총합은:%d'%sum)
##print('평균은:%.2f'%(sum/5))
