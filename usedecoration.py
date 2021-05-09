import time


def out(func):
    def inside(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return ret
    return inside


@out
def func(a, b=3):
    time.sleep(0.5)
    return a+b


print(func(3))
print(func(3, 7))
print(func(3, b=10))

# @deco(可能含参或者不含参)   需要再包一层  三层
#coding: utf-8
from time import time
from time import sleep

def count_time(msg):
    def tmp(func):
        def wrapped(*args, **kargs):
            begin_time = time()
            result = func(*args, **kargs)
            end_time = time()
            cost_time = end_time - begin_time
            print('msg: %s ,%s called cost time : %s' %(msg, func.__name__, cost_time))
            return result
        return wrapped
    return tmp

@count_time("foobar")
def test():
    sleep(0.5)

@count_time("测试消息")
def test2():
    sleep(0.7)

if __name__ == '__main__':
    test()
    test2()