"""
函数的嵌套：函数定义时，可以在一个函数里面定义另外一个函数

总结：
1. 函数可以作为返回值返回
2. 函数可以作为参数互相传递
3. 函数名本质上是一个变量名，表示的是一个内存地址
"""
import random

def func1():
    def func2():  # 嵌套函数，局部变量
        print("func2")
    func2()  # 局部的东西，一般都是在局部自己访问和使用


func1()


def func1():
    print("func1: 123")
    def func2():
        print("func2: 456")
        def func3():
            print("func3: 789")
        print("func2: 1")
        func3()
        print("func2: 2")
    print("func1: 3")
    func2()
    print("func1: 4")


func1()


def func1():
    def inner(*args):
        print("inner: 123")
        print(args)
    print(inner)
    print("inner id is:", format(id(inner), "x"))
    return inner


b1 = func1()
print(b1)
b1 = func1()
print(b1)
print("*" * 20)


# 代理模式
def func1(an):
    print(an)
    an()


def func2():
    print("func2")


# func1(2)
func1(func2) # 实参可以是一个函数

# 全局函数和全局函数的变量的id不变，但是内嵌函数的id各不相同，表示每次调用时都产生新的内嵌函数对象
print("*" * 30)
def func1():
    a = [1, 2, 3, 4]
    # a = 2
    lst = [random.randint(1, 10) for i in range(random.randint(4, 10))]
    print(f"{lst=}'s id: ", id(lst))
    def func2():
        print("func1's id: ", id(func1), "func2's id: ", id(func2))
    func2()


for i in range(random.randint(1, 20)):
    func1()