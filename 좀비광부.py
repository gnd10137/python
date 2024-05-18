##from tkinter import*
##pen_color='black'
##w=6
##
##def paint(event):
##     global pen_color
##     x1,y1=event.x,event.y
##     x2,y2=x1+5,y1+5
##     canvas.create_line(x1,y1,x2,y2,width=3,fill=pen_color)
##
##def change_color(color):
##     global pen_color
##     pen_color=color
##
##def clear_canvas():
##     canvas.delete('all')
##
##win=Tk()
##canvas=Canvas(win,bg='white',width=500,height=200)
##btn1=Button(win,text='white',width=w,bg='white',command=lambda:change_color('white'))
##btn2=Button(win,text='black',fg='white',width=w,bg='black',command=lambda:change_color('black'))
##btn3=Button(win,text='blue',fg='white',width=w,bg='blue',command=lambda:change_color('blue'))
##btn4=Button(win,text='green',fg='white',width=w,bg='green',command=lambda:change_color('green'))
##btn5=Button(win,text='yellow',width=w,bg='yellow',command=lambda:change_color('yellow'))
##btn6=Button(win,text='red',fg='white',width=w,bg='red',command=lambda:change_color('red'))
##btn7=Button(win,text='+',width=w,bg='white',command=change_color('red'))
##btn8=Button(win,text='-',width=w,bg='white',command=change_color)
##btn9=Button(win,text='clear',width=w,bg='white',command=clear_canvas)
##canvas.grid(row=0,column=0,columnspan=9)
##btn1.grid(row=1,column=0)
##btn2.grid(row=1,column=1)
##btn3.grid(row=1,column=2)
##btn4.grid(row=1,column=3)
##btn5.grid(row=1,column=4)
##btn6.grid(row=1,column=5)
##btn7.grid(row=1,column=6)
##btn8.grid(row=1,column=7)
##btn9.grid(row=1,column=8)
##win.bind('<B1-Motion>',paint)
##win.mainloop()

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

##from tkinter import*
##from random import*
##
##def draw_shape(event):
##     color=['black','white','blue','red','green','yellow']
##     x1,y1=event.x,event.y
##     x2,y2=x1+randint(10,70),y1+randint(10,70)
##     canvas.create_rectangle(x1,y1,x2,y2,fill=color[randint(0,5)])
##
##win=Tk()
##canvas=Canvas(win,width=300,height=300,bg='white')
##canvas.pack()
##canvas.bind('<Double-Button-1>',draw_shape)
##win.mainloop()

##n=int(input())
##for i in range(1,10):
##     print('%d*%d=%d'%(n,i,n*i))

n=int(input())
a=0
for i in range(1,n+1):
     a=a+i
print(a)
