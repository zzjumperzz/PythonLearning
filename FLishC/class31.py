#pickle
import pickle
list=[123,3.14,['list']]
pickle_file=open('pickle.pkl','wb')
#写入文件
pickle.dump(list,pickle_file)
pickle_file.close()

pickle_file=open('pickle.pkl','rb')
my_list=pickle.load(pickle_file)
print(my_list)
pickle_file.close()