import random

def get_data():
    '''返回0~9之间的三个随机数'''
    return random.sample(range(10),3)

def consume():
    '''显示每次传入整数列表的动态平均值'''
    running_sum = 0
    data_item_seen = 0

    while True:
        data = yield
        data_item_seen +=len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_item_seen)))

def produce(cunsumer):
    '''产生序列集合，传递给消费函数'''
    while True:
        data = get_data()
        print('Produce {}'.format(data))
        cunsumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Produce...')
        next(producer)