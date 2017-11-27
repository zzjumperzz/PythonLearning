#汉诺塔实现
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi((n-1),x,z,y)
        print(x, '-->', z)
        hanoi((n-1),y,x,z)
n=int(input('汉诺塔层数：'))
hanoi(n,'x','y','z')