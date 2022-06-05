# 1. 变量用来区分不同数据，变量指向了一个内存空间
# 2. 变量使用前需要初始化
# 3. 变量的命名规范：必须用字母、数字、下划线组成的，数字不能作为变量名的开头
# 4. python中不建议变量名用_（下划线）开头
# 5. 变量名不要使用中文
# 6. 变量名建议使用驼峰命名法
var1 = "第一篇作文"
var2 = "第二篇作文"

print(var1)
print(var2)

# 变量可以指向一个新的数据
var1 = 188
print(var1)

lst1 = [3]
lst2 = [3]
print(id(lst1), id(lst2))

def func1():
    def func2():
        pass
    return func2

a = func1()
b = func1()
print(id(a), id(b))

