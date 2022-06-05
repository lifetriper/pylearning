import random


def insert_sort_gap(lst, gap):
    for i in range(gap, len(lst)):
        tmp = lst[i]
        # j 表示已排序区间的最后一个（最大元素）所在的位置
        j = i - gap
        # while 循环把比待排序元素大的值都向后移动
        while j >= 0 and lst[j] > tmp:
            lst[j+gap] = lst[j]
            j -= gap
        lst[j+gap] = tmp


def shell_sort(lst):
    d = len(lst) // 4
    while d >= 1:
        insert_sort_gap(lst, d)
        d //= 4


lst_random = [i for i in range(10000)]
random.shuffle(lst_random)
# print(lst_random)

shell_sort(lst_random)
print(lst_random)


