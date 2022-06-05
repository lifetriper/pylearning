"""
形参分类
1. 位置参数：按照位置一个个声明的变量
2. 关键字参数：在函数声明的时候，给函数的参数一个默认值，默认值参数必须在位置参数的后面
3. 动态位置参数(*args)：表示位置参数数量可变的形参，这些形参被放入一个元组中，动态参数需要在位置参数和默认参数之后
4. 动态关键字参数(**kwargs)：表示接收关键字的动态传参，这些参数被传入后放在一个字典中

形参的顺序：
位置参数，*args, 关键字参数，**kwargs
上述参数可以随意搭配使用
"""


def luru(name, age, gender="女"):
    print(name, age, gender)


def eat(main, *food):
    print(main, food)


def eat_keyword(**food):
    print(food)


def func(a, b, c="哈哈", *args, **kwargs):
    print(f"{a=}, {b=}, {c=}, {args=}, {kwargs=}")  # c的默认值无法启用


def func1(a, b, *args, c="哈哈", **kwargs):
    print(f"{a=}, {b=}, {c=}, {args=}, {kwargs=}")  # c的默认值可以启用


# 没有参数限制
def func2(*args, **kwargs):
    print(args, kwargs)


luru("张无忌", 21, "男")
luru("赵敏", 18)

eat("大米饭")
eat("意粉", "罗宋汤", "冰棍")
eat_keyword(main="意粉", soup="紫菜汤")

print("func(1, 2, 3, 4, 5, 6, 7, 8, 9: ", end="")
func(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("func(1, 2, 3, 4, 5, 6, 7, 8, 9, kw1=123, kw2=456): ", end="")
func(1, 2, 3, 4, 5, 6, 7, 8, 9, kw1=123, kw2=456)
print("func(1, 2, kw1=123, kw2=456): ", end="")
func(1, 2, kw1=123, kw2=456)
print("func1(1, 2, 3, 4, 5， 6，kw1=123, kw2=456): ", end="")
func1(1, 2, 3, 4, 5, 6, kw1=123, kw2=456)
func1(1, 2, 3, 4, 5, 6, c=20, kw=123, kw2=456)

lst_team = ["流川枫", "樱木花道", "大猩猩", "大叔"]


def pnt_team(*args):
    print(args)


pnt_team(lst_team)
pnt_team(*lst_team)  # 把列表打散，作为实参传递给函数
