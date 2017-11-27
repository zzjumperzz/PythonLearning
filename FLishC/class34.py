#else 和 with

try:
    int('abc')
except ValueError as reason:
    print(str(reason))
else:
    print('没有任何异常')


try:
    #with 会自动关闭文件，不需要单独关闭
    with open('pickle.pkl','r') as f:
        for each_line in f:
            print(each_line)
except UnicodeDecodeError as reason:
    print(str(reason))
# finally:
#     f.close()