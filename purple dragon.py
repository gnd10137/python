##class Car:
##     model='BMW'
##     color='white'
##
##     def speedChange(self,v):
##          print('speedChange:%d'%v)
##          self.speed=v
##bmw=Car()
##bmw.speedChange(20)

##class Car:
##     model='BMW'
##     color='white'
##
##bmw=Car()
##benz=Car()
##
##benz.model='Benz'
##benz.color='black'
##
##print(bmw.model)
##print(bmw.color)
##
##print(benz.model)
##print(benz.color)

##class Car:
##     model='BMW'
##     color='white'
##
##     def speedChange(self,v):
##          self.speed=v
##bmw=Car()
##bmw.speedChange(20)

##class Car:
##     count=0
##     speed=0
##
##     def speedChange(self,v):
##          Car.count+=1
##          self.speed=v
##
##bmw=Car()
##benz=Car()
##
##bmw.speedChange(100)
##print('bmw speed:',bmw.speed)
##print('number of speedChange:',Car.count)
##
##benz.speedChange(120)
##print('benz speed:',benz.speed)
##print('number of speedChange:',Car.count)

##class Car:
##     def __init__(self,model,color):
##          self.model=model
##          self.color=color
##
##     def info(self):
##          print('Model:',self.model,'Color:',self.color)
##bmw=Car('BMW','white')
##bmw.info()

##class Car:
##     def __init__(self,model,color):
##          self.model=model
##          self.color=color
##
##     def info(self):
##          print('Model:',self.model,'Color:',self.color)
##bmw=Car('BMW','white')
##benz=Car('BENZ','black')
##bmw.info()
##benz.info()

##class Car:
##     def __init__(self,model,color):
##          self.model=model
##          self.color=color
##     def info(self):
##          print('Model:',self.model,'Color:',self.color)
##
##class CarDrive(Car):
##     def speedChange(self,v):
##          self.speed=v
##          print('speedChange:',self.speed)
##
##bmw=CarDrive('BMW','white')
##bmw.info()
##bmw.speedChange(100)

##class Car:
##     def __init__(self,model,color):
##          self.model=model
##          self.color=color
##
##     def info(self):
##          print('Model:',self.model,',Color:',self.color)
##
##class CarDrive(Car):
##     def info(self):
##          print('The model of this car is %s.' % self.model)
##          print('The color is %s.' % self.color)
##
##     def speedChange(self,v):
##          self.speed=v
##          print('speedChange:',self.speed)
##
##bmw=CarDrive('BMW','white')
##bmw.info()

##class Character:
##     def __init__(self,name,weapon):
##          self.name=name
##          self.weapon=weapon
##
##     def intro(self):
##          print('Name:',self.name)
##          print('weapon:',self.weapon)
##lugo=Character('Lugo','gun')
##lugo.intro()
