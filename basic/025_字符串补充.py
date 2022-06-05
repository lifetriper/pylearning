# len
s = "大家好"
print(len(s))

# join
s1 = "python_java_c_javascript"
lst = s1.split("_")
print(lst)

s = "-".join(lst)
print(s)

"""
总结：
 1. f-String: 
 2. 索引：从0开始
 3. 切片：s[start:end:step]，end位置的数据无法拿到
 4. 操作：对原字符串不发生改变，返回一个新的字符串
    - upper，忽略大小写
    - strip，去掉字符串两端的空白
    - replace，字符串的替换
    - split，对字符串切割
    - join，拼接列表，产生新的字符串
    - startswith，
    - len
    - for c in s:
    - in，判断字符串是否包括特定字符串
"""

