"""
字符串的操作一般不会对原字符串改变，一般会返回一个新的字符串
"""

# 字符串大小写转换
s = "python"
print(s.capitalize())

# 单词的首字母大写
s = "I have a dream!"
print(s.title())

# 变成小写字母
s = "I HAVE A DREAM!"
print(s.lower())

# 变成大写字母
# 用于验证码忽略大下小，一般都变成大写字母
s = "I have a dream!"
print(s.upper())
