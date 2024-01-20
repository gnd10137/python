##import random
##
##com=random.randint(1, 2)
##user=int(input('odd:1,even:2\n'))
##print('COM(%d):USER(%d)'%(com,user))
##if com==user:
##     print('Correct')
##else:
##      print('Incorrect')
##import random
##List=['월','화','수','목','금','토','일']
##a=random.randint(0,6)
##print(List[a])
##from random import *
##a=['월','화','수','목','금',]
##print(choice([True, False]))
##print(choices(a))
##from random import*
##a=[1,2,3,4,5]
##print(choices(a,[1,1,10,1,1],k=3))
##from random import*
##a=[1,2,3,4,5]
##print(choices(a,k=3))
##from random import*
##a=[0,1,2,3,4,5]
##b=choice(a)
##if b==0:
##     print('Loss!')
##else:
##     print('No.%d spot!'%b)
from random import*
import turtle

house=turtle.Turtle()
house.penup()
house.goto(300,-100)
house.pendown()
house.fillcolor('skyblue')
house.begin_fill()
house.forward(70)
house.left(90)
house.forward(70)
house.left(90)
house.forward(70)
house.left(90)
house.forward(70)
house.end_fill()

house.fillcolor('royalblue')
house.begin_fill()
house.backward(70)
house.left(90)
house.left(90)
house.right(30)
house.forward(70)
house.right(120)
house.forward(70)
house.right(120)
house.forward(70)
house.end_fill()

line=turtle.Turtle()
line.penup()
line.goto(-380,-100)
line.fillcolor('black')
line.pendown()
line.write(0)
line.forward(360)
line.write(50)
line.forward(320)
line.write(100)

t=turtle.Turtle(shape='turtle')
t.penup()
t.goto(-400,-100)
t.color('black','white')
t.penup()

g=turtle.Turtle()
g.write('호날두의 타자 실력',True,font=('Arial',20,'bold'))
turtle.done()
