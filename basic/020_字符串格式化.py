name = input('请输入您的名字：')
address = input('请输入您的地址：')
age = int(input('请输入您的年纪：'))
hobby = input('请输入您的爱好：')

# %s, 字符串占位, %d, 整数占位, %f, 浮点数占位
s1 = "我叫%s, 我的地址%s, 我的年纪%d, 我的爱好%s" % (name, address, age, hobby)
print("方法1: ", s1)

s2 = "我叫{}, 我的地址{}, 我的年纪{}, 我的爱好{}".format(name, address, age, hobby)
print("方法2: ", s2)

s3 = f"我叫{name}, 我的地址{address}, 我的年纪{age}, 我的爱好{hobby}"
print("方法3: ", s3)