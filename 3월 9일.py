##def add(x,y):
##    s=x+y
##    return s
##result=add(10,20)+add(20,30)
##print(result)

##def f(n):
##    n=20
##    return n
##n=10
##f(n)
##print(n)
##n=f(n)
##print(n)

##def get_max(x,y):
##    if x>y:
##        return x
##    else:
##        return y
##x=int(input())
##y=int(input())
##n=get_max(x,y)
##print(n)

##def get_sum(n):
##    s=0
##    for i in range(1,n+1):
##        s+=i
##    return s
##n=int(input())
##print('1부터 %d까지의 합은 %d입니다.'%(n,get_sum
##(n)))

##def rect(w,h):
##    return w*h
##def tri(w,h):
##    return w*h/2
##def circle(r):
##    return r**2*3.14
##print('Choose a shape:')
##print('1.Rectangle','2.Triangle','3.circle',
##sep='/n')
##n=int(input())
##if n==1:
##    w=int(input('width:'))
##    h=int(input('height:'))
##    area=rect(w,h)
##elif n==2:
##    w=int(input('width:'))
##    h=int(input('height:'))
##    area=tri(w,h)
##elif n==3:
##    r=int(input('radius:'))
##    area=circle(r)
##print(area)

##def warning():
##    for _ in range(3):
##        print('Fire!')
##warning()

##def two_times():
##    for i in range(1,2):
##        print('2*%d=%d'%(i,2*i),end=' ')
##two_times()

##from random import*
##def random_number():
##    num=random()+10
##    return num
##print(random_number())

##def say(name):
##    print('Welcome,',name)
##    return
##say('minsu')

##def day(m,d):
##    print('Today is %s/%s.'%(m,d))
##day(12,7)

##def f():
##    a=10
##    print(a)
##f()
##print(a)

##a=0
##def f():
##    global a
##    global b
##    print(a)
##    a=10
##    b=20
##f()
##print(a)
##print(b)

##def A():
##  print(1)
##  r=B()
##  print(r)
##def B():
##    print(2)
##    return 3
##A()
##print(4)

##def A():
##    B()
##def B():
##    print(1)
##A()

##def f(n):
##    print(n)
##    if n>1:
##        f(n-1)
##f(3)

##def factorial(n):
##    if n==1:
##        return 1
##    else:
##        return n*factorial(n-1)
##fac=factorial(4)
##print('4!=',fac)

##def judge(n):
##    if n<0:
##        print('plus')
##    elif n<0:
##        print('minus')
##    else:
##        print('zero')
##n=int(input())
##judge(n)

##from random import*
##def lotto():
##    lot=[]
##    for i in range(6):
##        lot.append(randint(1,45))
##    lot.sort()
##    print(lot)
##lotto()

def average(n,tot):
    avg=tot/n
    return avg
def total():
    tot=0
    score=input('score:').split()
    for i in score:
        tot+=int(i)
    avg=average(len(score),tot)
    print('total score:%d'%tot)
    print('average score:%.2f'%avg)
total()
