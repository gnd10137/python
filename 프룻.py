from random import*
import turtle

house=turtle.Turtle()
house.penup()
house.goto(300,-100)
house.pendown()
house.fillcolor('blue')
house.begin_fill()
house.forward(70)
house.left(90)
house.forward(70)
house.left(90)
house.forward(70)
house.left(90)
house.forward(70)
house.end_fill()

house.fillcolor('red')
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

house.fillcolor('black')
house.begin_fill()
house.right(60)
house.forward(70)
house.right(120)
house.forward(70)
house.end_fill

line=turtle.Turtle()
line.penup()
line.goto(-380,-100)
line.fillcolor('yellow')
line.pendown()
line.write(0)
line.forward(360)
line.write(50)
line.forward(320)
line.write(100)

t=turtle.Turtle(shape='turtle')
t.penup()
t.goto(-400,-100)
t.color('pink','royalblue')
t.penup()

g=turtle.Turtle()
g.write('호날두의 타자 실력',True,font=('Arial',20,'bold'))
turtle.done()

a=[1,2,3,4,5,6,7,8,9,10]
b=choices(a,[2,2,2,2,2,2,1,2,2,2],k=3)
print(b)
