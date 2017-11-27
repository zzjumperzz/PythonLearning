#构造和解析
#__init__
#_new__(cls[,...])
#__del__(self)

class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)

a = CapStr('i love littlebith')
print(a)

class C:
    def __init__(self):
        print('我调用了__init__')
    def __del__(self):
        print('我掉用了__del__')

c = C()
c2 = c
c3 = c2

# del c2
# del c3
del c