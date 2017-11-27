# 题目：
# 输入一个正整数n，建立一个有n个元素的列表，列表中的元素为4个质数之和，第0元素为第一个质数到第四个质素之和（2+3+5+7），
# 第1个元素为第二个质数到第五个质素之和（3+5+7+11），第2个元素为第三个质数到第六个质素之和（5+7+11+13），以此类推。

#n=int(input('请输入一个正整数'))
number=set([])
for i in range(2,20):
    if i==2:
        number.add(i)
    if i==3:
        number.add(i)
    elif i%2!=0 and i%3!=0:
        number.add(i)

lists=list(number)
lens=len(number)

def sums():
    list2=[]
    for i in range(0,lens-1):
        if i+3 < lens:
            result=lists[i]+lists[i+1]+lists[i+2]+lists[i+3]
            list2.append(result)
    return list2
print(sums())



