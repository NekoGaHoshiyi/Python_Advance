import threading
import time

# 元类实现考虑多线程的单例
class Singleton_t(type):
    _instance_lock = threading.Lock()
    def __call__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            with self._instance_lock:
                self._instance = super(Singleton_t, self).__call__(self)
        return self._instance


class Single(metaclass=Singleton_t):
    def __init__(self, name):
        self.name = name
        time.sleep(1)


S1 = Single('s1')
S2 = Single('s2')
print(S1, S2)


# __new__实现单例
class Simple():
    _instance_lock = threading.Lock()
    def __init__(self, name):
        self.name = name
        time.sleep(1)
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                cls._instance = super(Simple, cls).__new__(cls)
        return cls._instance


s1 = Simple('s1')
s2 = Simple('s2')
print(s1, s2)

# 装饰器实现单例
def Singledeco(cls):
    _instance = {}
    def _single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _single
@Singledeco
class A():
    def __init__(self, name):
        self.name = name


a1 = A('a1')
a2 = A('a2')

print(a1, a2)


#  简单的工厂模式


class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)

class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


factory = Factory()
person = factory.getPerson("Avril", "F")