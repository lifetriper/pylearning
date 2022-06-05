"""
实参：
1. 位置传参：按照参数位置传参数
2. 关键字传参：按照参数的名字传参数
3. 混合传参：必须先用位置传参，然后用关键字传参

函数调用时，形参必须保证能够获得数据
"""


def eat(main, dish, soup, desert):
    print(main, dish, soup, desert)


print("按照位置传递参数：", end="")
eat("大米饭", "西红柿抄鸡蛋", "紫菜汤", "哈根达斯")
print("按照关键字传递参数：", end="")
eat(main="意粉", soup="罗宋汤", desert="冰棍", dish="炒腰子")
print("按照混合方式传递参数：", end="")
eat("意粉", "炒腰子", desert="冰棍", soup="罗宋汤")


