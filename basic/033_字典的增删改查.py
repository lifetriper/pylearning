dict1 = {"jay": "周杰伦", "金毛狮王": "谢逊", "神雕大侠": "杨过"}

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

for item in dict1.items():
    print(item)

# 元组的解构
for key, value in dict1.items():
    print(key, value)


# 字典的嵌套
wangfeng = {
    "name": "汪峰",
    "age": "18",
    "wife": {
        "name": "章子怡",
        "hobby": "演戏"
    },
    "children": [
        {"name": "孩子1", "age": "18"},
        {"name": "孩子2", "age": "12"}
    ]
}
