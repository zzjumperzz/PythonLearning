#字典：当索引不好用时
#映射
brand=['李宁','阿迪达斯','耐克']
slogan=['一切就有可能','impossible is nothing','Just do it']
print('李宁的广告是：',slogan[brand.index('李宁')])

#字典 是映射类型 其他事序列类型
dirc={'李宁':'一切就有可能','阿迪达斯':'impossible is nothing','耐克':'Just do it'}
print('耐克的广告是：',dirc['耐克'])

#dict方法
dict1=dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict1)
dict2=dict(钓鱼岛='是中国的',苍井空='是世界的')
#dict中 关键字不能用引号
print(dict2)