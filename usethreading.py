import threading
import time


def long_time_task(i):
    print('当子线程: {}'.format(threading.current_thread().name))
    if i == 0:
        time.sleep(2.2)
    else:
        time.sleep(2)
    with open('./'+str(i)+'.txt','w',encoding='utf-8'):
        pass
    print("结果: {}".format(8 ** 20))

# i = 0对应的子线程t.setDaemon(True),则主线程结束，i=0对应的Thread-1如果还未运行完会直接结束
if __name__=='__main__':
    start = time.time()
    print('这是主线程：{}'.format(threading.current_thread().name))
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=long_time_task, args=(i,))
        print(t.getName())
        # True则 主线程结束
        if i == 0:
            t.setDaemon(True)
        else:
            t.setDaemon(False)
        thread_list.append(t)
    for t in thread_list:
        t.start()
    #
    # for t in thread_list:
    #     t.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))