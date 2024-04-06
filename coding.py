##f=open('example.txt','w')
##for i in range(1,4):
##     f.write('Line %d\n'% i)
##f.close()

##f=open('example.txt','a')
##alphabet=['A','B','C','D','E']
##for c in alphabet:
##     f.write(c)
##f.close()

##f=open('example.txt','r')
##data=f.read()
##print(data)
##f.close()

##f=open('example.txt','r')
##while True:
##     line=f.readline()
##     if not line:break
##     print(line,end='')
##f.close()

##f=open('example.txt','r')
##data=f.readlines()
##for line in data:
##     print(line,end='')
##f.close()

##f=open('example.txt','r')
##while True:
##     print(f.tell(),end=' ')
##     line=f.readline()
##     print(line.strip())
##     if not line:break
##f.seek(24)
##print('포인터의 위치%d%s%s%s'%(f.tell(),f.read()[0],f.read()[2],f.read()[4]))
##f.close()

##f=open('profile.txt','w')
##name=input('Name: ')
##age=input('Age:')
##f.write('Name:%s\n'%name)
##f.write('Age:%s\n'%age)
##f.close()

##f=open('profile.txt','a')
##name=input('Name: ')
##age=input('Age:')
##School=input('School:')
##f.write('Name:%s\n'%name)
##f.write('Age:%s\n'%age)
##f.write('School:%s\n'%School)
##f.close()

##f=open('profile.txt','r')
##f.seek(17)
##data=f.readline()
##print(data)
##f.close()

##f=open('alphabet.txt','w')
##f.write('ABCDEFGHIJKLMNOPQRXTUVWXYZ')
##f.close()

##index=int(input('index:'))
##f=open('alphabet.txt','r')
##f.seek(index)
##line=f.readline()
##print(line,end='')
##f.close()

##f=open('fruit.txt','r')
##data=f.readlines()
##for word in data:
##     word=word.strip()
##     if len(word) >=10:
##          print(word)
##f.close()

##f=open('anna.txt','r')
##data=f.readline()
##data=data.split()
##
##for word in data:
##     if 'b' in word:
##          print(word)
##f.close
