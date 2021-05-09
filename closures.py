from functools import wraps
def foo(func):
    a = 111
    print(id(a))
    print(a)
    b = 1
    print(id(b))
    @wraps(func)
    def func(c,a):
        nonlocal b
        print(a)
        print(id(a))
        print(a+b)
        print(id(b))
        return a+c
    return func

def func(c):
    print(c)

func = foo(func)

print(func(2,222))

def f1():
    print("in  f1..")
    num=111
    def f2():
        # 注释nonlocal将打印的是 222 111
        nonlocal num
        num=222
        print(num)
    f2()
    print(num)
f1()

# global num   这里可以说明  就算是只有内层函数global  他引用的也不是外层函数的同名变量 而是函数外的，除非内层函数也global
num = 2
print(num)
print(id(num))

def f3():
    print("in  f1..")
    #global num
    # print(num)
    # print(id(num))
    num = 111
    print(num)
    print(id(num))
    def f4():
        global num
        #num=222
        print(f4,num)
        print(id(num))
    f4()
    print(num)
    print(id(num))
f3()