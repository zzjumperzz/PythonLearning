#定制容器
#编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数

class CountList:
    #*args表示可变数量的对象，即可传入随意多个对象
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

c1 = CountList(1,3,5,7)
c2 = CountList(2,4,6,8)

c1[0]
c2[2]
c1[0]+c2[2]
print(c1.count)