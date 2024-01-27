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

fruit=['사과','바나나','딸기','수박','만다린']
score=0
n=randint(3,5)

for i in range(n):
     s=choice(fruit)
     word=turtle.textinput('fruit','%s(%d/%d)'%(s,i+1,n))
     if s==word:
          score+=1

rate=score/n*100

g.penup()
g.goto(0,-50)
g.pendown()
g.write('%d/%d번 성공!'%(score,n),True, font=('Arial',15,'bold'))
g.penup()
g.goto(0,-100)
g.pendown()
g.write('정확도:%1f%%'%rate,True,font=('Arial',15,'bold'))

distance=t.distance(line)/100*rate
t.speed(1)
t.forward(distance)
if rate==100:
     t.write('집에 데려다줘서 고마워.',False,'center',font=('Arial',15,
                                            'normal'))
elif rate>=80:
     t.write('집이 코앞인데. 한 번만 더 시도해줘.',False,'center',
     font=('Arial',15,'normal'))

elif rate>=50:
     t.write('집에 가고 싶어.',False,'center',
     font=('Arial',15,'normal'))          

else:
     t.color('black')
     t.right(360)
     t.write('거북이가 쓰러졌어요.',False,'center',
     font=('Arial',15,'normal'))

turtle.done()
