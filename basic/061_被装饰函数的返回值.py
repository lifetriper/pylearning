"""
通用装饰器的写法：
def wrapper(fn):
    def inner(*args, **kwargs):
        处理1
        ret = fn(*args, **kwargs)
        处理2
        return ret
    return inner

@wrapper
def func():
    函数体
"""


def guanjia(game):
    def inner(*args, **kwargs):
        print("开外挂")
        ret1 = game(*args, **kwargs)
        print("关闭外挂")
        return ret1
    return inner


@guanjia
def play_dnf(username, password):
    print(f"playing dnf with {username}, {password}")
    return 100


@guanjia
def play_lol(username, password, hero):
    print(f"playing lol with {username}, {password}, {hero}")
    return 200


ret = play_dnf("admin", "password")
print(ret)

ret = play_lol("admin", "password", "big hero")
print(ret)
