"""

"""
lst = []

# append
lst.append(1)
lst.append("张三丰")

# insert
lst.insert(1, "张无忌")

# extend，可以合并两个列表
lst.extend(["武则天", "马超"])

print(lst)

# pop，删除列表的元素
ret = lst.pop(3)

# remove, 直接给元素
lst.remove("马超")

print(lst, ret)

# 修改
lst[0] = "赵敏"
print(lst)

# 查询，直接用索引进行操作
print(lst[2])