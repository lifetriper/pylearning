"""
函数定义
def 函数名(函数参数):
    函数体

函数的调用
函数名(参数1, 参数2, ...)

"""
import random


def func1(a):
    print("id of func1 is: ", id(func1))
    print(a)


func1(2)
func1(3)

# 讨论函数的内存管理机制
print("*" * 20)

# 1. 对于无参全局函数而言，每次函数调用时，函数都是同一个id
def func1():
    a = random.randint(1, 10)
    print("func1's id: ", id(func1), f"{a=}'s id: ", id(a))


for i in range(random.randint(1, 10)):
    func1()


# 2. 对于对于带全局函数而言，每次函数调用时，函数都是同一个id
print("*" * 20)


def func1(index):
    print("func1's id: ", id(func1), f"{index=}'s id: ", id(index))


for i in range(random.randint(1, 10)):
    func1(random.randint(1, 10))