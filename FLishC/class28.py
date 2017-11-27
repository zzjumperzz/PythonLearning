#文件
f=open('E:\\release2.txt')
print(f.read(5))
print(f.tell())
f.seek(20,0)
print(f.readline())
f.seek(0,0)
#print(list(f))

for each_line in f:
    print(each_line)