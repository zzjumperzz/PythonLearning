#集合
#集合可排重，但是不能排序和索引
set1=set([1,2,3,4,5,2])
print(set1)#返回的是集合
print(list(set1))#list 将集合变为列表
#使用 IN 和 NOT IN 可以判断元素是否在集合内
set1.add(6)
print(set1)
set1.remove(1)
print(set1)
#不可变集合
frozenset([0,1,2])