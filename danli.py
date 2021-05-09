# 参考地址： https://www.cnblogs.com/huchong/p/8244279.html
import time
import threading



# 使用模块，作为外置模块导入就是天然的单例

# 使用类的__new__方法

class DanLiLei:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

a = DanLiLei()
print(a)
b = DanLiLei()
print(b)

time.sleep(1)
print('--------------------------------------------------------------------------')

# 通过上面例子，我们可以知道，当我们实现单例时，为了保证线程安全需要在内部加入锁
# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
# 实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

class Singleton_new(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton_new, "_instance"):
            with Singleton_new._instance_lock:
                if not hasattr(Singleton_new, "_instance"):
                    Singleton_new._instance = object.__new__(cls)
        return Singleton_new._instance

obj1 = Singleton_new()
obj2 = Singleton_new()
print(obj1, obj2)

def task(arg):
    obj = Singleton_new()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

time.sleep(1)
print('--------------------------------------------------------------------------')
# 使用类实现简单的装饰器

class Singleton_s(object):

    def __init__(self):
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


s1 = Singleton_s()
print(s1)
s2 = Singleton_s()
print(s2)

time.sleep(1)
print('--------------------------------------------------------------------------')
# 使用类且考虑多线程，但是如果__init__中有io或其他耗时操作则会出问题

class Singleton_t(object):

    def __init__(self):
        # 注释当前代码改pass则因为执行速度很快产生的是单例
        import time
        time.sleep(1)
    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton_t, "_instance"):
            Singleton_t._instance = Singleton_t(*args, **kwargs)
        return Singleton_t._instance

import threading

def task(arg):
    obj = Singleton_t.instance()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

time.sleep(1)
print('--------------------------------------------------------------------------')
# 考虑__init__耗时操作，线程加锁的方式创建单例


class Singleton_tlock(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with Singleton_tlock._instance_lock:
            if not hasattr(Singleton_tlock, "_instance"):
                Singleton_tlock._instance = Singleton_tlock(*args, **kwargs)
        return Singleton_tlock._instance


def task(arg):
    obj = Singleton_tlock.instance()
    print(obj)
for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
# time.sleep(20)
# obj = Singleton_tlock.instance()
# print(obj)


time.sleep(1)
print('--------------------------------------------------------------------------')
# 使用装饰器 + 字典 类作为键，实例作为值

def Singleton(cls):
    _instance = {}
    def _singleton(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton

@Singleton
class A(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

a1 = A(2)
a2 = A(3)
print(a1)
print(a2)


time.sleep(1)
print('--------------------------------------------------------------------------')
# 基于__metaclass__元类实现单例

# 元类的使用

class SingletonType(type):
    def __init__(self,*args,**kwargs):
        super(SingletonType,self).__init__(*args,**kwargs)

    def __call__(cls, *args, **kwargs): # 这里的cls，即Foo类
        print('cls',cls)
        obj = cls.__new__(cls,*args, **kwargs)
        cls.__init__(obj,*args, **kwargs) # Foo.__init__(obj)
        return obj

class Foo(metaclass=SingletonType): # 指定创建Foo的type为SingletonType
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

obj = Foo('xx')


time.sleep(1)
print('--------------------------------------------------------------------------')
# 元类实现单例,考虑线程

class SingletonType_t(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType_t._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType_t,cls).__call__(*args, **kwargs)
        return cls._instance

class Foo_t(metaclass=SingletonType_t):
    def __init__(self,name):
        self.name = name


obj1 = Foo_t('name')
obj2 = Foo_t('name')
print(obj1, obj2)

