from multiprocessing import Pool, cpu_count
import os
import time
from crawnews import craw_huanqiu, node



if __name__ == '__main__':
    print('CPU cores: {}'.format(cpu_count()))
    start = time.time()
    p = Pool(cpu_count())
    for n in node:
        p.apply_async(func=craw_huanqiu, args=(n, 200))
    print('耐心等待所有任务完成')
    p.close()
    p.join()
    end = time.time()
    print('总共用时：{}秒'.format(end - start))



# Pool对象的方法：

# 1.apply_async
#
# 函数原型：apply_async(func[, args=()[, kwds={}[, callback=None]]])
#
# 其作用是向进程池提交需要执行的函数及参数， 各个进程采用非阻塞（异步）的调用方式，即每个子进程只管运行自己的，不管其它进程是否已经完成。这是默认方式。
#
# 2.map()
#
# 函数原型：map(func, iterable[, chunksize=None])
#
# Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到结果返回。 注意：虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
#
# 3.map_async()
#
# 函数原型：map_async(func, iterable[, chunksize[, callback]])
# 与map用法一致，但是它是非阻塞的。其有关事项见apply_async。
#
# 4.close()
#
# 关闭进程池（pool），使其不在接受新的任务。
#
# 5. terminate()
#
# 结束工作进程，不在处理未处理的任务。
#
# 6.join()
#
# 主进程阻塞等待子进程的退出， join方法要在close或terminate之后使用。