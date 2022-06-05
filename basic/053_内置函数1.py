"""
内置函数：直接可以拿来用的函数
"""
import random

a = "18"
print(int(a), float(a), bool(a))

a = 18
print(bin(a), oct(a), hex(a))

a = 0b10011
print(a)

a = [1, 2, 3, 4]
print(min(a), max(a), sum(a))

s = {1, 2, 3, 4}
print(list(s))
s = "IntelliJ"
print(list(s))

# format, chr, ord
a = 18
print(format(a, "b"))  # b 二进制
print(format(a, "o"))
print(format(a, "x"))  # x 十六进制
print(format(a, "08b"))

a = "中"  # python中使用unicode编码
print(ord(a))
print(chr(20012))
# for i in range(65536):
#     print(chr(i), end=" ")

# enumerate, all, any
print(all([12, "呵呵", "豆沙包"]))  # True
print(all([0, "呵呵", "豆沙包"]))  # False, 相当于and
print(any([0, "", '']))  # False，相当于or
lst = ["张无忌", "张翠山", "张三丰"]
for item in enumerate(lst):
    print(item)
for index, item in enumerate(lst):
    print(index, item)

lst = [random.randint(1, 100000) for i in range(1000000)]

s = "哈哈"
print(hash(s), hash(s), hash(s))  # hash 一定是一个数字->内存地址, 保存数据-> 字典/集合，哈希表
print(id(s))

print(dir(s))  # 当前数据可以执行的操作
