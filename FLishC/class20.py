#嵌套函数和闭包
def FunX(x):
    def FunY(y):
        return x*y
    return FunY
#第一种方法 实例化后再调用
i = FunX(8)
#print (type(i))
print (i(5))
#第二种方法 不用实例化 直接调用函数
print(FunX(8)(6))

#正规的方法 可以让内嵌函数成功调用外部函数的局部变量
#当函数方法内有形参时，返回值是一个对象；当函数方法内是实参或者没有参数时，返回方法
def fun1():
    x = 5
    def fun2(y):
        nonlocal x
        x *= y
        return x
    #当函数方法内有形参时，返回值是一个对象
    return fun2
print('fun1=',fun1()(2))

def fun3():
    x = 5
    def fun4():
        nonlocal x
        x *= x
        return x
    #当函数方法内是实参或者没有参数时，返回方法
    return fun4()
print('fun3=',fun3())


#以上方法的投机取巧法
def funOne():
    x =[5]
    def funTwo():
        x[0] *= x[0]
        return x[0]
    return funTwo()

print (funOne())