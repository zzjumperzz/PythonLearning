#lambda表达式 匿名函数
#BIF 内置函数
# 1-- filter() 过滤器
def odd(x):
    return x % 2
temp = range(10)
show = filter(odd,temp)
print(list(show))
#使用lambda方法实现同上效果
print(list(filter(lambda x : x % 2,range(10))))

#2 -- map()映射

print(list(map(lambda x : x * 2 ,range(10))))