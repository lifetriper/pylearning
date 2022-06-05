"""
索引：按照位置提取元素
"""

s = "我叫周杰伦，你叫周润发"
print(s[1])
print(s[-2])

# 切片，切片拿不到:之后的元素位置
print(s[3:6])
print(s[3:-1])
print(s[3:])
print("s[-3:-1]:", s[-3:-1])
print("s[-1:-6:-1]", s[-1:-6:-1])
print("s[::-1]", s[::-1])

s = "abcdefghijklmnopqrstuvwxyz"
print("s[2:11:3]: ", s[2:11:3])
print("s[2:11:3]: ", s[-1:-10:-3])
