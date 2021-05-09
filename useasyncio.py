#### 异步协程 asyncio
#参见：   https://blog.csdn.net/weixin_41599977/article/details/93656042

# python 3.7 以前的版本调用异步函数的步骤：
# 1、调用asyncio.get_event_loop()函数获取事件循环loop对象
# 2、通过不同的策略调用loop.run_forever()方法或者loop.run_until_complete()
# 方法执行异步函数

import asyncio

async def work(x):    # 通过async关键字加到函数定义之前定义一个协程
    for _ in range(3):
        print('Work {} is running ..'.format(x))
    return "Work {} is finished".format(x)
corotine_1 = work(1)    # 协程是一个对象，不能直接运行

def call_back(future):
    print("Callback: {}".format(future.result()))


# 方式一
loop = asyncio.get_event_loop()     # 创建事件循环
result = loop.run_until_complete(corotine_1)    #协程对象放入循环，并执行
print(result)       #协程对象并没有返回结果，打印None,返回则可以打印返回值
# 方式二(适用于 python3.7+)
#asyncio.run(corotine_1)         #直接用run方法创建事件循环并放入协程

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

mainc = main()
#asyncio.run(main())
loop = asyncio.get_event_loop()
result = loop.run_until_complete(mainc)
#print(result)

# create task
corotine_2 = work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(corotine_2)
#task = asyncio.ensure_future(corotine_2)   # task的另一种创建
print(task)
loop.run_until_complete(task)
print(task)
print(type(task))
print('task是不是asyncio.Future的子类:', isinstance(task, asyncio.Future))

# isinstance(obj, class) 和 type()的区别：
# type()不会认为子类是一种父类类型，不考虑继承关系，得到的就是当前是什么类
# isinstance会考虑继承关系，认为子类是一种父类关系

corotine_3 = work(3)
loop = asyncio.get_event_loop()
#task = asyncio.ensure_future(corotine_3)
task = loop.create_task(corotine_3)
# 创建一个函数用来接受future,调用future.result()回调得到task对应函数的返回
# task.add_done_callback(以future为形参,通过future.result()得到返回的回调函数名)
task.add_done_callback(call_back)
loop.run_until_complete(task)       #返回任务的结果
# 如果task结束也可以用task.result.result()
print("The task's result is '{}'".format(task.result()))
