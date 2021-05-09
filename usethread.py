import threading
import _thread
import time

# 因为_thread.start_new或者start_new_thread创建的线程一创建就运行，运行过程中可以看出守护属性为True
# 主进程守护属性为False，但是_thread创建的默认为True，很容易主线程完成直接退出
# 而threading.Thread模块创建的默认为False
def long_time_task(i):
    print('当子线程: {}'.format(threading.current_thread().name))
    print(threading.currentThread().daemon)
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
        _thread.start_new_thread(long_time_task, (i,))
        print(threading.currentThread().daemon)
    end = time.time()
    # 注释改行，子进程将不会运行完全
    time.sleep(3)
    print("总共用时{}秒".format((end - start)))