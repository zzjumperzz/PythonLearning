#属相访问
#例一：
class C:
    def __getattribute__(self, name):
        print('getattribute')
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print('getattr')
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key,value)
    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)

c = C()

c.X
print('******************')
c.X=1
print('******************')
print(c.X)
print('******************')
del c.X
print('******************')

#例二
class Rentangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    def __setattr__(self, name, value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            #注释一，此语句会造成死循环
            #self.name = value
            
            #注释二，此语句时较高级的用法
            #self.__dict__[name] = value
            
            #注释三，此写法是常规写法
            super(Rentangle, self).__setattr__(name,value)

    def getArea(self):
        return self.width * self.height

r1 = Rentangle(4,5)
print(r1.getArea())
r1.square = 10
print(r1.getArea())