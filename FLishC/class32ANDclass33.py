#exception 异常处理机制
try:
    list = ['123']
    assert len(list) < 0
    print('1')
except AssertionError as a:
    print('有异常'+str(a))

