"""
内容回顾：
1. 函数可以作为参数传递
2. 函数可以作为返回值返回
3. 函数名称可以当成变量进行赋值操作

装饰器：
1. 本质上是一个闭包，作用是不改变原有函数调用方式的情况下，给原有函数增加新的功能
2. 被装饰的函数被调用时，实际上调用的是装饰器的inner函数

雏形：
wrapper: 装饰器，fn：目标函数
def wrapper(fn):
    def inner():
        新功能
        fn()
        新功能
    return inner
"""


def guanjian(game):
    def inner():
        print("开外挂")
        print("inner id: ", id(inner))
        game()
        print("关闭外挂")
    return inner


@guanjian  # 相当于play_dnf = guanjian(play_dnf)
def play_dnf():
    print("playing dnf")


@guanjian  # 相当于# play_lol = guanjian(play_lol)
def play_lol():
    print("playing lol")


# play_dnf = guanjian(play_dnf)  # 管家把dnf重新封装了一遍，我把游戏替换成带外挂的游戏
# play_lol = guanjian(play_lol)  # 管家把lol重新封装了一遍，我把游戏替换成带外挂的游戏
play_dnf()
play_lol()
