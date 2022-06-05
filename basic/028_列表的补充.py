"""
排序：列表的保存是有顺序的
"""
import random

lst = [1, 2, 3, "潘金莲", "武大郎"]
print(lst)

lst = [random.randint(1, 100) for i in range(10)]
print(lst)
lst.reverse()
print(lst)

# 列表的循环删除
lst = ["赵敏", "张无忌", "欧阳锋", "张三丰", "张大侠", "杨过", "张三"]
i = 0
while i < len(lst):
    if lst[i].startswith("张"):
        lst.pop(i)
    else:
        i = i+1

print(lst)
