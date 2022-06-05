"""
python存储set数据时，需要对数据进行hash计算，根据计算出来的哈希值进行存储
字符串，元组可哈希，可哈希的数据是不可变的数据
列表，set，字典都是不可哈希的
set 可以用于去重
"""

s = {1, 2, "测试", 3}
print(s)
#  s = {1, 2, [1, 2]}  错误，不可哈希
s = set()   # 空集合
s.add("赵本山")
s.add("马化腾")
s.add("范伟")
print(s)
# s.pop()
s.remove("范伟")
print(s)

for item in s:
    print(item)

# 交集，并集，差集
s1 = {"关云长", "刘备", "张飞", "曹操"}
s2 = {"刘备", "曹操", "孙权"}
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))
