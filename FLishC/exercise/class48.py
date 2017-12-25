#迭代器
#斐波那契
class fibs:
    def __init__(self,n=10):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

fibs = fibs(50)
for each in fibs:
    print(each)

