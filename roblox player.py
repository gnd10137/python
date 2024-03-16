##def warning():
##    for _ in range(3):
##        print('fire.')
##warning()

##def two_times():
##    for i in range(1,10):
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
##say('kevin')

##def day(m,d,c,a,b,r):
##    print('Today is %s/%s/%s/%s/%s/%s.'
##          %(m,d,c,a,b,r))
##day(2024,3,16,11,43,34)

##def f() :
##      a = 10
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
##    print(1)
##    r=B()
##    print(r)
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
##    if n>0:
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

##def funs_abs(n):
##    if n>0:
##        print(n)
##    elif n<0:
##        print(n*-1)
##n=int(input('정수입력.'))
