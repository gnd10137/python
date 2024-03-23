##add=lambda x,y:x+y
##print(add(10,100))

##from tkinter import*
##def Click(n):
##    if n==1:
##        lbl['text']='First button clicked.'
##    elif n==2:
##        lbl['text']='Second button clicked.'
##    else:
##        lbl['text']='Third button clicked.'
##win=Tk()
##lbl=Label(win,text='이름')
##btn1=Button(win,text='First',command=lambda:Click(1))
##btn2=Button(win,text='Second',command=lambda:Click(2))
##btn3=Button(win,text='Third',command=lambda:Click(3))
##lbl.grid(row=0,column=0,columnspan=3)
##btn1.grid(row=1,column=0)
##btn2.grid(row=1,column=1)
##btn3.grid(row=1,column=2)
##win.mainloop()

##from tkinter import*
##def Click(shape):
##    if shape=='circle':
##        img=PhotoImage(file='circle.png')
##    elif shape=='triangle':
##        img=PhotoImage(file='triangle.png')
##    else:
##        img=PhotoImage(file='star.png')
##    lbl['image']=img
##    lbl.image=img
##win=Tk()
##img=PhotoImage(file='circle.png')
##lbl=Label(win,image=img)
##btn1=Button(win,text='circle',command=lambda:Click('circle'))
##btn2=Button(win,text='triangle',command=lambda:Click('triangle'))
##btn3=Button(win,text='star',command=lambda:Click('star'))
##lbl.grid(row=0,column=0,columnspan=3)
##btn1.grid(row=1,column=0)
##btn2.grid(row=1,column=1)
##btn3.grid(row=1,column=2)
##win.mainloop
