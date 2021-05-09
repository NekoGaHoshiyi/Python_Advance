class Human:
    live = '有理想'  # 类共有的属性
    __desires = '有欲望'  # (程序级别)类私有的属性
    _desires = '有欲望'  # (程序员之间约定俗称)类私有的属性
    def __init__(self,name,age,sex,hobby):
        self.name = name
        self.age = age
        self.sex = sex  # 对象的共有的属性
        self.__hobby = hobby  # 对象的私有属性
    def func(self):
        # 类内部可以查看对象的私有属性
        print(self.__hobby)
    def foo(self):
        # 类内部可以查看类的私有属性
        print(self.__desires)
    def __abc(self):  # 私有方法 只有内部可以使用
        print('is abc')
class subHuman(Human):
    pass
obj = Human('beauty',28,'man','woman')
print(obj.name)
print(Human.live)
Human.live = '无脑'
print(Human.live)
print('________________')
print(obj._desires)
sb = subHuman('beauty',28,'man','woman')
print(dir(sb))
print(sb._desires)
print(obj._Human__desires)
obj._Human__abc()   # 会报错 因为外部不可以调用类的私有方法
print(Human._Human__desires)