"""
闭包的要求：
1. 内层函数必须使用外层函数的local变量
2. 必须返回内嵌的函数

闭包的本质：内层函数对外层函数局部变量的使用，此时内层函数被称为闭包函数

闭包的作用：
1. 可以让一个变量常驻于内存，不会被回收。比如下面例子中的a
2. 在全局操作局部变量，可以避免全局变量使用时被更改。而通过闭包的方式，保证了变量只能在某些地方（inner）修改
"""
import random


def func1():
    a = 0
    def inner():
        nonlocal a
        a += 1
        return a
    return inner


ret = func1()

ret()


def func1(a):  # func 每次调用时，inner的id都不同
    b = a + 1
    print("id of b", id(b), b)
    def inner():
        print("the id of inner: ", id(inner))
        print(a)
    return inner


print(id(2), id(3), id(4))
ret = func1(2)
ret()
ret = func1(3)
ret()
ret = func1(2)
ret()

print("*" * 10)


def func2():
    # a = [1, 2, 3, 4]
    b = [7, 8, 9]

    # print("id of func2 is: ", id(func2))
    # print("id of a is: ", id(a))
    # print("id of b is: ", id(b))
    def inner():
        # print('id of a is: ', id(a), a)
        print('id of b is: ', id(b), b)
        print("id of inner is: ", id(inner))
    return inner


for i in range(random.randint(1, 20)):
    f1 = func2()
    f1()