##from random import*
##a=randint(1,100)
##while True:
##     b=int(input('정수입력'))
##     if a>b:
##          print('up')
##     elif b>a:
##          print('down')
##     elif a==b:
##          print('correct')
##          break

##a=int(input('정수입력'))
##for i in range(1,a+1):

##a=int(input('정수입력'))
##if a%2==0:
##     print('짝수')
##else:
##     print('홀수')

##a=int(input('정수입력'))
##i=0
##sum=0
##while i<=a:
##     if i%3==0:
##          sum+=i
##     i+=1
##print(sum)

##for i in range(1,101):
##     if i%2==0:
##          print(i)

##a=int(input('a:'))
##b=int(input('b:'))
##print('%d+%d=%d'%(a,b,a+b))
##print('%d-%d=%d'%(a,b,a-b))
##print('%d*%d=%d'%(a,b,a*b))
##print('%d//%d=%d'%(a,b,a//b))

##a=int(input('height:'))
##b=int(input('width:'))
##print('area:%.1f'%(a*b/2))

L=int(input('L 판매 개수:'))
M=int(input('M 판매 개수:'))
S=int(input('S 판매 개수:'))
sum=2500*L
sum=1000*M
sum=500*S
print('오늘의 총 매출은 %d원입니다.'%sum)
