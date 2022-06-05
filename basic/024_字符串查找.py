# find, -1 表示没有找到
s = "你好啊，我是周润发"
ret = s.find("周润发a")
print(ret)

# index
ret = s.index("周润发")
print(ret)

# in 和 not in
print("周润发" in s)
print("周杰伦" not in s)

# 判断，startswith(), endswith(), isDecimal(), isdigit()
name = input("请输入你的名字：")
if name.startswith("张"):
    print("你姓张")

money = input("请输入你的工资：")
if money.isdigit():  # 判断字符串是否由整数组成
    print("可以花钱")
