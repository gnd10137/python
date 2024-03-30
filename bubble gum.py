from tkinter import*
from random import*
win=Tk()
win.title('Rock Scissors Paper Game')

def change_img(user):
     List=['scissors.png','rock.png','paper.png']
     
     com=randint(0,2)
     
     computer_img=PhotoImage(file=List[com])
     useruser_img=PhotoImage(file=List[user])
     
     com_img['image']=computer_img
     com_img.Image=computer_img
     
     user_img['image']=useruser_img
     user_img.Image=useruser_img

     game(com,user)

def game(com,user):
     if user==0:
          if com==0:
               result['text']='Draw'
          elif com==1:
               result['text']='Loss'
          else:
               result['text']='Win'
     elif user==1:
          if com==0:
               result['text']='Win'
          elif com==1:
               result['text']='Draw'
          else:
               result['text']='Loss'
     elif user==2:
          if com==0:
               result['text']='Loss'
          elif com==1:
               result['text']='Win'
          else:
               result['text']='Draw'
     
basic_img=PhotoImage(file='ready.png')

com_img=Label(win,image=basic_img,relief='solid')
user_img=Label(win,image=basic_img,relief='solid')
com_lbl=Label(win,text='computer')
user_lbl=Label(win,text='user')
result=Label(win,text=' ',width=15,fg='brown',bg='lightyellow')
scissors_btn=Button(win,text='scissors',bg='skyblue',width=15,command=lambda:change_img(0))
rock_btn=Button(win,text='rock',bg='pink',width=15,command=lambda:change_img(1))
paper_btn=Button(win,text='paper',bg='lightgreen',width=15,command=lambda:change_img(2))

com_img.grid(row=0,column=0)
result.grid(row=0,column=1)
user_img.grid(row=0,column=2)
com_lbl.grid(row=1,column=0)
user_lbl.grid(row=1,column=2)
scissors_btn.grid(row=2,column=0)
rock_btn.grid(row=2,column=1)
paper_btn.grid(row=2,column=2)
win.mainloop()
