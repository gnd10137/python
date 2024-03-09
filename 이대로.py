##def add(x,y):
##     s=x+y
##     return s
##result=add(10,20)+add(20,30)
##print(result)

##def warning():
##     for _ in range(3):
##          print('Fire!')
##warning()

##def two_times():
##     for i in range(1,10):
##          print('2*%d=%d'%(i,2*i),end=' ')
##two_times()

##from random import*
##def random_number():
##     num=random()+10
##     return num
##print(random_number())

##a=0
##def f():
##     global a
##     global b
##     print(a)
##     a=10
##     b=20
##f()
##print(a)
##print(b)

##def A():
##     print(1)
##     r=B()
##     print(r)
##def B():
##     print(2)
##     return 3
##A()
##print(4)

##def f(n):
##     print(n)
##     if n>1:
##          f(n-1)
##f(3)

##def factorial(n):
##     if n==1:
##          return 1
##     else:
##          return n* factorial(n-1)
##fac=factorial(4)
##print('4!=',fac)

##def judge(n):
##     if n>0:
##          print('plus')
##     elif n<0:
##          print('minus')
##     else:
##          print('zero')
##n=int(input())
##judge(n)

##def season(month):
##     if month == 3 or month == 4 or month == 5:
##          print('spring')
##     elif month == 6 or month == 7 or month == 8:
##          print('summer')
##     elif month == 9 or month == 10 or month == 11:
##          print('fall')
##     else:
##          print('winter')
##a=int(input('입력해'))
##season(a)

##from random import*
##def lotto():
##     lot=set()
##     while len(lot)<6:
##          lot.add(randint(1,45))
##     lot=list(lot)
##     lot.sort()
##     print(lot)
##lotto()

def func_abs(n):
     if n>0:
          print(n)
     elif n<0:
          print(n*-1)
n=int(input('정수입력.'))
func_abs(n)
