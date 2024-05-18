##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=200,height=100,bg='white')
##canvas.pack()
##
##cavnas.create_oval(10,10,60,60,fill='blue')
##canvas.create_rectangle(100,10,160,60,fill='yellow',outline='red')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=200,height=100,bg='white')
##canvas.pack()
##canvas.create_polygon(100,10,30,90,160,90,fill='red')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_oval(30,30,70,70,fill='blue')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_oval(30,30,70,50,fill='blue')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_rectangle(10,10,80,50,fill='yellow')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_rectangle(30,10,60,90,fill='yellow')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_polygon(10,90,50,10,90,90,fill='red')
##win.mainloop()

##from tkinter import*
##
##win=Tk()
##canvas=Canvas(win,width=100,height=100,bg='white')
##canvas.pack()
##canvas.create_polygon(20,90,20,10,80,90,fill='red')
##win.mainloop()

##from tkinter import*
##from random import*
##
##def draw_shape(event):
##    color=['black','white','blue','red','green','yellow']
##    x1,y1=event.x,event.y
##    x2,y2=x1+randint(10,70),y1+randint(10,70)
##    canvas.create_rectangle(x1,y1,x2,y2,fill=color[randint(0,5)])
##
##win=Tk()
##canvas=Canvas(win,width=300,height=300,bg='white')
##canvas.pack()
##
##canvas.bind('<Double-Button-1>',draw_shape)
##win.mainloop()

##from tkinter import*
##from random import*
##
##def draw_shape(event):
##    color=['black','white','blue','red','green','yellow']
##    x1,y1=event.x,event.y
##    x2,y2=x1+randint(10,70),y1+randint(10,70)
##    canvas.create_oval(x1,y1,x2,y2,fill=color[randint(0,5)])
##
##win=Tk()
##canvas=Canvas(win,width=300,height=300,bg='white')
##canvas.pack()
##
##canvas.bind('<Double-Button-1>',draw_shape)
##win.mainloop()
