# 插入排序：记录无序区最小元素的位置，最后将无序区的第一个元素和最小元素对调

import random

SCOPE = 30
LST_LENGTH = 10

lst_random = [random.randint(1, SCOPE) for i in range(LST_LENGTH)]
print(lst_random)


# 需要一个新的存储结构存数据
def select_sort_01(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


# 在原来的待排序存储中直接排序
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


# print(select_sort_01(lst_random))
select_sort(lst_random)
print(lst_random)
