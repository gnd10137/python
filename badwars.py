#from tkinter import*
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

##from tkinter import*
##def Click(shape):
##     if shape=='circle':
##          img=PhotoImage(file='circle.png')
##     elif shape=='triangle':
##          img=PhotoImage(file='triangle.png')
##     else:
##          img=PhotoImage(file='star.png')
##     lbl['image']=img
##     lbl.image=img
##win=Tk()
##img=PhotoImage(file='circle.png')
##lbl=Label(win,image=img)
##btn1=Button(win,text='circle',command=lambda:Click('circle'))
##btn2=Button(win,text='triangle',command=lambda:Click('triangle'))
##btn3=Button(win,text='star',command=lambda:Click('star'))
##lbl.grid(row=0, column=0, columnspan=3)
##btn1.grid(row=1, column=0)
##btn2.grid(row=1, column=1)
##btn3.grid(row=1, column=2)
##win.mainloop()

##f=open('example.txt','w')
##f.close()

##f=open('example.txt','w')
##for i in range(1,4):
##    f.write('Line %d\n'% i)
##f.close()

##f=open('example.txt','a')
##alphabet=['A','B','C','D','E']
##for c in alphabet:
##    f.write(c)
##f.close()

##f=open('example.txt','r')
##data=f.read()
##print(data)
##f.close()

##f=open('example.txt','r')
##while True:
##    line=f.readline()
##    if not line:break
##    print(line,end='')
##f.close()

##f=open('example.txt','r')
##data=f.readlines()
##for line in data:
##    print(line,end='')
##f.close()

##f=open('example.txt','r')
##while True:
##    print(f.tell(),end=' ')
##    line=f.readline()
##    print(line.strip())
##    if not line:break
##f.seek(26)
##print('after setting a pointer:%d(%s)'%(f.tell(),f.read()[0]))
##f.close

##f=open('profile.txt','w')
##name=input('Name: ')
##age=input('Age: ')
##f.write('Name:%s\n'%name)
##f.write('Age:%s\n'%age)
##f.close()

from tkinter tmport*
def get_click():
    lbl2['text']=txt_box.get(1.0,END)
def ins_click():
    txt_box.insert(1.0,lbl1['text'])
def del_click():
    txt_box.delete(1.0,END)
win=Tk()
txt_box=Text(win,width=40,height=5)
lbl1=Label(win,text='Click the 'insert' button to insert this string.',
width=40,height5,bg='sktblue')
lbl2=Label(win,text='Click the 'get' button to import textbox
strings\ninto this label.',width=40,height=5, bg='pink'
           
