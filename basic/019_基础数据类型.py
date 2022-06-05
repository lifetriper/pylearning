# int

# float
a = 10.5
print(a)

print(10/3)  # Ans: 3.3333333333333335
# 0~1之间的浮点数是无限的，那么计算机该如何表示0～1之间的浮点数？
# 计算机表示一个小数是有误差的
print(0.1+0.2)  # Ans: 0.30000000000000004

# bool: 用来做条件判断，取值只有True和False

# 基础数据类型的转化
a = "10"
print(type(a))
b = int(a)
print(type(b))

a = -9
print(bool(a))
a = 0
print(bool(a))

s = ""
print('"" is:', bool(s))

lst = []
print('[] is: ', bool(lst))

while True:
    content = input("请输入内容：")
    if content:
        print("您输入的内容：", content)
    else:
        break
