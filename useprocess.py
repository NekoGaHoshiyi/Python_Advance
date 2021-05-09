from multiprocessing import Process
import os
import time
from crawnews import craw_huanqiu





if __name__=='__main__':
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    p1 = Process(target=craw_huanqiu, args=('mil', 50))
    p2 = Process(target=craw_huanqiu, args=('world', 50))
    print('等待所有子进程完成。')
    p2.start()
    p1.start()
    p1.join()
    p2.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))

