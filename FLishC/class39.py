#组合 例一 MAX_in
class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,y):
        self.num = y
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_pool(self):
        print ('池子里有%s条鱼，有%s个乌龟'%(self.fish.num,self.turtle.num))

pool = Pool(3,5)
pool.print_pool()

#类 类对象 实例对象
    # 类                    C
    #                       |
    #  类对象               C
    #              ________|________
    #              |       |       |
    # 实例对象      a       b       c

#属性与方法名相同 属性会覆盖方法