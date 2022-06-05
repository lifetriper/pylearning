"""
函数默认有：return None
1. return  # return None
2. return 值  # 函数有一个返回值
3. return 值1, 值2, 值3,...  # 函数有多个返回值，调用者收到一个返回值构成的元组
"""


def func(a, b):
    return a+b


ret = func(10, 20)
print(ret * 3)
