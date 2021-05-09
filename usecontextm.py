from contextlib import contextmanager,closing

#contextmanager装饰器
@contextmanager
def open_func(filename):
    # __enter__方法
    print('open file:', filename, 'in __enter__')
    filehandler = open(filename, 'r')
    yield filehandler

    # __exit__方法
    print('close file:', filename, 'in __exit__')
    filehandler.close()
    return


with open_func('1.txt') as file:
    for line in file:
        print(line)

# closing类
class MyOpen2():
    def __init__(self, filename):
        '''初始化方法'''
        self.filehandler = open(filename, 'r')
        return
    # 使用contexlib.closing,对类写close方法
    def close(self):
        '''关闭文件，会被自动调用'''
        print("call close in MyOpen2")
        if self.filehandler:
            self.filehandler.close()
with closing(MyOpen2('1.txt')) as file:
    # TypeError: 'MyOpen2' object is not iterable
    # for line in file:
    #     print(line)
    print(file)


# 以下是contextlib.closing的内部
class closing():
    '''Context to automatically close something at the end of a block'''
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()

