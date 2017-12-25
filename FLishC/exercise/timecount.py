import time
def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)
    return call

@timeslong
#
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())

print('**************************************')

class timeslong2(object):
    def __init__(self,func):
        self.f = func
    def __call__(self):
        start = time.clock()
        print("It's time starting ! ")
        self.f()
        print("It's time ending ! ")
        end = time.clock()
        return "timeslong2 It's used : %s ." % (end - start)

@timeslong2
def f2():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f2())
