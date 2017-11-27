#继承 父类 基类 超类
import random as r

class Parent:
    def hello(self):
        print ('hello')

class Son(Parent):
    pass
    #def hello():
        #print('子类的方法hello')

p = Parent()
s = Son()
#子类可以继承父类的方法
p.hello()
s.hello()

#例
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x -=  1
        print('我的位置是：',self.x,self.y)

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('我饿了')
        else:
            print('我吃饱了')

goldfish = Goldfish()
goldfish.move()
carp = Carp()
carp.move()
salmon = Salmon()
salmon.move()
shark = Shark()
shark.move()
shark.eat()