#斐波那契函数
#使用迭代方式实现（自己完成的,闭包方式）
def function(n):
    def one():
        nonlocal n
        sums = [1,1]
        for i in range(2,n):
            sum=sums[0]+sums[1]
            sums[0]=sums[1]
            sums[1]=sum
        return sum
    return one()
#n = int(input('请输入一个正整数：'))
n=30
if n <= 2:
    print('%d的斐波那契值是%d'%(n,1))
else:
    result=function(n)
print('%d的斐波那契值是%d'%(n,result))

#使用递归的方式(老师写的）
def functionTwo(n):
    if n <= 2 :
        return 1
    else:
        return functionTwo(n-1)+functionTwo(n-2)
n=20
result=functionTwo(n)
print('%d的斐波那契值是%d'%(n,result))

#递归方法非常耗时，但是在递归层数不高时，是个很好的方法




