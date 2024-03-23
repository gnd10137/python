##from tkinter import*
##win=Tk()
##btn=Button(win,text='Button')
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##img=PhotoImage(file= 'pizza.png')
##lbl=Label(win,text='pizza',bg='yellow',fg='red')
##lbl1=Label(win,image=img)
##lbl1.pack()
##lbl.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##def click():
##     if lbl['text']=='hello':
##          lbl['text']='python'
##          lbl['bg']='green'
##          lbl['fg']='white'
##     else:
##          lbl['text']='hello'
##          lbl['bg']='orange'
##          lbl['fg']='white'
##lbl=Label(win,text='hello',bg='orange',fg='white')
##btn=Button(win,text='button',command=click)
##lbl.pack()
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##win.title('grid')
##label1=Label(win,width=10,height=5,bg='red')
##label2=Label(win,width=10,height=5,bg='orange')
##label3=Label(win,width=10,height=5,bg='yellow')
##label4=Label(win,width=10,height=5,bg='green')
##label5=Label(win,width=10,height=5,bg='blue')
##label6=Label(win,width=10,height=5,bg='purple')
##label1.grid(row=3,column=3)
##label2.grid(row=0,column=2)
##label3.grid(row=2,column=2)
##label4.grid(row=4,column=1)
##label5.grid(row=3,column=0)
##label6.grid(row=1,column=5)
##win.mainloop()

##add=lambda x,y:x+y
##print(add(10,100))

##remains=lambda a,b:a%b
##print(remains(8,3))

##say=lambda name:print('Hello'+name)
##say('날두야!')

from tkinter import*
def Click(shape):
     if shape=='circle':
          img=PhotoImage(file='circle.png')
     elif shape=='triangle':
          img=PhotoImage(file='triangle.png')
     else:
          img=PhotoImage(file='star.png')
     lbl['image']=img
     lbl.image=img
win=Tk()
img=PhotoImage(file='circle.png')
lbl=Label(win,image=img)
btn1=Button(win,text='circle',command=lambda:Click('circle'))
btn2=Button(win,text='triangle',command=lambda:Click('triangle'))
btn3=Button(win,text='star',command=lambda:Click('star'))
lbl.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
win.mainloop()
