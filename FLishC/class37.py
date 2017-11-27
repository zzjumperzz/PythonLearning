#面向对象编程

#__init__(self) 构造器
class Ball:
    def __init__(self,name):
        self.name = name
    def click(self):
        print('%s是我的名字啊'%self.name)

a = Ball('张鹏')
a.click()

#公有和私有
class Person:
    #在变量前加双下划线，变量成为私有
    __name='张鹏'
    def getName(self):
        return self.__name

p = Person()
name = p.getName()
print(name)