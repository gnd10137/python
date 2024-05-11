##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=300,height=300)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='yellow',width=100,height=100)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.create_line(0,50,500,50,fill='blue',width=5)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.create_line(50,50,350,50,fill='green',width=1)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=500)
##canvas.create_line(250,100,250,400,fill='red',width=5)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.pack()
##
##x1,y1=0,0
##x2,y2=500,0
##
##for i in range(3):
##     y1+=30
##     y2=y1
##     canvas.create_line(x1,y1,x2,y2,fill='red',width=3)
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.pack()
##
##x1,y1=0,0
##x2,y2=0,100
##
##for i in range(10):
##     x1+=45
##     x2=x1
##     canvas.create_line(x1,y1,x2,y2,fill='red',width=3)
##win.mainloop()

##from tkinter import*
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=500)
##canvas.pack()
##
##x1,y1=10,10
##x2,y2=10,460
##
##for i in range(10):
##     canvas.create_line(x1,y1,x2,y2,fill='red',width=3)
##     x1+=50
##     x2=x1
##x1,y1=10,10
##x2,y2=460,10
##
##for i in range(10):
##     canvas.create_line(x1,y1,x2,y2,fill='blue',width=3)
##     y1+=50
##     y2=y1
##win.mainloop()

##from tkinter import*
##
##def paint(event):
##     x1,y1=event.x,event.y
##     x2,y2=x1+5,y1+5
##     canvas.create_line(x1,y1,x2,y2,width=3)
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=200)
##canvas.pack()
##
##win.bind('<B1-Motion>',paint)
##win.mainloop()

##from tkinter import*
##pen_color='black'
##
##def paint(event):
##     global pen_color
##     x1,y1=event.x,event.y
##     x2,y2=x1+5,y1+5
##     canvas.create_line(x1,y1,x2,y2,width=3,fill=pen_color)
##
##def change_color():
##     global pen_color
##     pen_color='red'
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=200)
##btn=Button(win,text='red',command=change_color)
##def change_color():
##     global pen_color
##     pen_color='black'
##btn1=Button(win,text='black',command=change_color)
##
##canvas.pack()
##btn.pack()
##btn1.pack()
##win.bind('<B1-Motion>',paint)
##win.mainloop()

from tkinter import*
pen_color='black'

def paint(event):
     global pen_color
     x1,y1=event.x,event.y
     x2,y2=x1+5,y1+5
     canvas.create_line(x1,y1,x2,y2,width=3,fill=pen_color)

def change_color():
     global pen_color
     pen_color='red'

win=Tk()
canvas=Canvas(win,text='white',bg='white',width=500,height=200)
btn1=Button(win,text='white',bg='white',command=change_color)
btn2=Button(win,text='black',bg='black',command=change_color)
btn3=Button(win,text='blue',bg='blue',command=change_color)
btn4=Button(win,text='green',bg='green',command=change_color)
btn5=Button(win,text='yellow',bg='yellow',command=change_color)
btn6=Button(win,text='red',bg='red',command=change_color)
btn7=Button(win,text='+',bg='white',command=change_color)
btn8=Button(win,text='-',bg='white',command=change_color)
btn9=Button(win,text='clear',bg='white',command=change_color)
win.bind('<B1-Motion>',paint)
win.mainloop()
