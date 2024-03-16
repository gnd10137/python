##def func_abs(n):
##    if n>0:
##        print(n)
##    elif n<0:
##        print(n*-1)
##n=int(input('tntwkfmf dlqfurgktpdy.(숫자를 입력하세요.)'))
##func_abs(n)

##from tkinter import*
##win=Tk()
##win.title('C3 coding')
##win.geometry('300x200+100+100')
##win.resizable(True, False)
##win,mainloop()

##from tkinter import*
##win=Tk()
##label1=Label(win,text='one')
##label2=Label(win,text='two')
##label3=Label(win,text='three')
##label1.pack()
##label2.pack()
##label3.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##lbl1=Label(win,text='orange',width=20,height=3,relief='solid')
##lbl2=Label(win,text='banana',font=('Elephant',20),bg='yellow',relief='sunken')
##lbl3=Label(win,text='apple',fg='red')
##lbl1.pack()
##lbl2.pack()
##lbl3.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##img=PhotoImage(file='pizza.png')
##lbl1=Label(win,image=img)
##labl1=Label(win,text='pizza',bg='yellow',fg='red')
##lbl1.pack()
##labl1.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##btn=Button(win,text='Button')
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##def click():
##     if btn['text']=='red':
##          btn['text']='blue'
##          btn['bg']='blue'
##     else:
##          btn['text']='red'
##          btn['bg']='red'
##btn=Button(win,text='red',fg='white',bg='red',command=click)
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##def click():
##     if lbl['text']=='hello':
##          lbl['text']='python'
##          lbl['bg']='green'
##     else:
##          lbl['text']='hello'
##          lbl['bg']='orange'
##lbl=Label(win,text='hello',bg='orange',fg='white')
##btn=Button(win,text='button',command=click)
##lbl.pack()
##btn.pack()
##win.mainloop()

##from tkinter import*
##win=Tk()
##def message(event):
##     lbl['text']=entry.get()
##entry=Entry(win)
##entry.bind('<Return>',message)
##entry.pack()
##lbl=Label(win,text=' ')
##lbl.pack()
##win.mainloop()

from tkinter import*
win=Tk()
win.title('grid')
label1=Label(win,width=10,height=5,bg='red')
label1.grid(row=0,column=0)
win.mainloop()
