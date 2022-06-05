a = 10

def func1():
    a = 20  # 创建了一个局部变量，并没有改变全局变量a


func1()
print(a)


def func1():
    global a  # 把外部的全局变量引入到函数内
    a = 20


func1()
print(a)


def func1():
    a = 10
    def func2():
        nonlocal a  # 向外找一层，看看有没有该变量，如果没有继续向外一层，直到全局（不包括全局）
        a = 20
    func2()
    print(a)


func1()
