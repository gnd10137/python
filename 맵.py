##a=int(input('몇 단?'))
##for i in range(1,10):
##    print(i*a)
##
##a=int(input('정수입력')
##for i in range(1,a):
##      print()
##
##for i in range(10)
##a=int(input('정수입력'))

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=200,height=100,bg='white')
##canvas.pack()
##
##canvas.create_oval(10,10,60,60,fill='blue')
##canvas.create_rectangle(100,10,160,60,fill='yellow',outline='red')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=400,height=400,bg='white')
##canvas.pack()
##
##canvas.create_oval(10,10,60,60,fill='blue')
##canvas.create_rectangle(100,10,160,60,fill='yellow',outline='red')
##canvas.create_polygon(100,110,30,190,160,190,fill='red')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##x1,y1,x2,y2=0,0,0,100
##
##for i in range(10):
##     canvas.create_line(x1,y1,x2,y2)
##     canvas.create_line(y1,x1,y2,x2)
##     x1+=10
##     x2=x1
##
##canvas.create_polygon(20,90,20,10,80,90,fill='red')
##win.mainloop()

from tkinter import*
from random import*

def draw_shape(event):
    color=['black','white','blue','red','green','yellow']
    x1,y1=event.x,event.y
    x2,y2=x1+randint(10,70),y1+randint(10,70)
    canvas.create_rectangle(x1,y1,x2,y2,fill=color[randint(0,5)])

win=Tk()
canvas=Canvas(win,width=300,height=300,bg='white')
canvas.pack()

canvas.bind('<Double-Button-1>',draw_shape)
win.mainloop()
