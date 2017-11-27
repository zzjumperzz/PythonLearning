#字典 课程二
dict1=dict.fromkeys((1,2,3,),'number')
#fromkeys会创造一个新得字典 所以不支持修改字典中关键字的值
print(dict1)

#keys(),values(),items()

dict2=dict.fromkeys(range(32),'赞')
for eachkey in dict2.keys():
    print(eachkey)
for eachvalue in dict2.values():
    print(eachvalue)
for eachitems in dict2.items():
    print(eachitems)

#get() 访问字典中的项
print(dict2.get(32))

print(31 in dict2)
print(32 in dict2)

#clear() 清空字典
#dict1.clear()
#copy() 浅拷贝
#是对对象的拷贝，不同于赋值，浅拷贝后值地址会变

#pop
print(dict1.pop(3))
print(dict1)
#popitem
print(dict1.popitem())
print(dict1)

#setdefault
dict1.setdefault('加班中。。。')
print(dict1)
dict1.setdefault(5,'test')
print(dict1)

#update()
a={'加班中。。。':'苦逼啊'}
dict1.update(a)
print(dict1)
