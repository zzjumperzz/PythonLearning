#递归
import sys
#设置递归层数
sys.setrecursionlimit(100)

#课题一 阶乘
#练习一 不用递归求阶乘
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
#计算结构是n*1*2*3*...*(n-1)
#range(1,n)的逻辑是 1<=range<n
number = int(input('请输入正整数：'))
result = factorial(number)
print('%d的阶乘是%d'%(number,result))


#练习二 递归调用
#递归要慎用，栈操作太频繁
def factoial2(n):
    if n == 1:
        return n;
    else:
        return n * factoial2(n-1)
n = int(input('请输入正整数：'))
sum = factoial2(n)
print('%d的阶乘是%d'%(n,sum))


