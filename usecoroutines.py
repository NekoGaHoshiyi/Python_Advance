import time

# yield挂起
def task_1():
    while True:
        print("This is task 1! --before")
        yield
        print("-- This is task1! --after")
        time.sleep(0.5)

def task_2():
    while True:
        print("-- This is task2! --before")
        yield
        print("This is task 2! --after")
        time.sleep(0.5)

# 生成器
def generate():
    i = 0
    while i < 5:
        print("我在这。。")
        # yield 不仅挂起了函数，还可以接受send发送的内容并返回给xx，
        # 同时next把i 传出，如果未send则yiled为函数内返回None
        xx = yield i
        print(xx)
        i += 1

# 协程的生产-消费者模型
def consumer():
    print('--4、Start excute generator code--')
    response = None
    while True:
        print('--5、yield,中断，保存上下文--')
        n = yield response
        print('--8、获取上下文，继续往下执行--')
        if not n:
            return
        print("[Consumer]: consuming {} ..".format(n))
        response = 'ok'
def producer(c):
    print("--3、启动生成器，开始执行生成器consumer--")
    c.send(None)        # 3、启动生成器，开始执行生成器consumer
    print("--6、继续往下执行--")
    n = 0
    while n < 5:
        n += 1
        print("[Producer]: producing {} ..".format(n))
        print("--7、第{}唤醒生成器，从yield位置继续往下执行！--".format(n+1))
        r = c.send(n) # 第二次唤醒生成器
        print("--9、从第8步往下--")
        print("[Producer]: consumer return {} ..".format(r))
    c.close()

# greenlet+switch 人工切换
from greenlet import greenlet

def task1():
    while True:
        print("--This is task 1!--")
        g2.switch()     # 切换到g2中运行
        time.sleep(0.5)
def task2():
    n = 0
    while n < 5:
        n += 1
        print("--This is task 2!--")
        g1.switch()     # 切换到g1中运行
        time.sleep(0.5)

# gevent+gevent.sleep()遇到io自动切换到其他，他会优先保证总有greenlet在执行而不是等待IO
import gevent

def taskA(num):
    for i in range(num):
        # gevent.getcurrent()获得当前的协程
        print(gevent.getcurrent(), i)
        gevent.sleep(1)     # 模拟一个耗时间的操作，但是不能用time.sleep

# gevent + monkey 补丁 这种方式不需要再使用gevent里的sleep sorcket
from gevent import monkey
import random

def taskB(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)       # 协程碰到耗时操作，自动切换其他协程
def taskC(name):
    for i in range(3):
        print(name, i)
        time.sleep(1)



if __name__ == "__main__":
    # t1 = task_1()
    # t2 = task_2()
    # print(t1, t2)
    # n = 0
    # while n < 3:
    #     c1 = next(t1)
    #     print("\nThe main thread!\n")
    #     c2 = next(t2)
    #     print(c1, c2)
    #     n += 1
    g = generate()
    print(next(g))
    g.send('ok')
    # 一开始要么 next(g),要么g.send(None)，
    # 否则TypeError: can't send non-None value to a just-started generator
    #g.send(None)
    print(g.__next__())
    g.close()
    #g.send("lalala")
    #g.send('xixixi')

    # 消费者yield+生产者send
    c = consumer()
    producer(c)

    # gevent协程人工切换
    g1 = greenlet(task1)
    g2 = greenlet(task2)
    g1.switch()

    # gevent自动切换,观察内存地址 三个地址是交叉执行的，如果不用gevent.sleep()则是按顺序来
    # gevent.spawn(func, arg)
    g1 = gevent.spawn(taskA, 5)   # 协程创建
    g2 = gevent.spawn(taskA, 5)
    g3 = gevent.spawn(taskA, 5)
    g1.join()
    g2.join()
    g3.join()

    # gevent + gevent.monkey补丁搭配time.sleep()
    # 为所有耗时操作打补丁
    monkey.patch_all()

    gevent.joinall([
        gevent.spawn(taskB, "taskb"),
        gevent.spawn(taskC, "taskc")
    ])
    print("the main thread!")