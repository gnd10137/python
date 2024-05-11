##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=300,height=300)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='yellow',width=100,height=100)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.create_line(0,50,500,50,fill='blue',width=5)
##canvas.pack(fill='both',expand=True)
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.create_line(0,30,300,30,fill='green',width=2)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=300,height=300)
##canvas.create_line(0,30,300,30,fill='red',width=5)
##canvas.pack()
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=100)
##canvas.pack()
##
##x1,y1=0,0
##x2,y2=500,0
##
##for i in range(3):
##    y1+=30
##    y2=y1
##    canvas.create_line(x1,y1,x2,y2,fill='red',width=3)
##
##win.mainloop()

##from tkinter import*
##def paint(event):
##    x1,y1=event.x,event.y
##    x2,y2=x1+5,y1+5
##    canvas.create_line(x1,y1,x2,y2,width=3)
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=200)
##canvas.pack()
##
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
canvas=Canvas(win,bg='white',width=500,height=200)
btn=Button(win,text='red',command=change_color)

canvas.pack()
btn.pack()
win.bind('<B1-Motion>',paint)
win.mainloop()
