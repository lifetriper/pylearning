"""
作用域：变量访问的权限

总结：函数里面可以访问外面定义的变量（默认无法修改），函数外面默认无法访问函数里面的变量
"""


a = 10  # 全局变量 -> 全局作用域，变量初始化后，全局可见


def func1():  # 全局函数，其他函数也可以调用该函数
    print(a)
    b = 20  # 局部变量 -> 函数/局部作用域，变量初始化后，仅在定义的函数内可见
    print(b)


def func2():
    func1()


