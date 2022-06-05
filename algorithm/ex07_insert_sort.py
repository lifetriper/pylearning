# 将数据分为已排序区和未排序区，每次从未排序区选择一个最左边的数，插入到已排序区合适的位置中
import random

SCOPE = 50
LIST_LENGTH = 10

# lst_random = [random.randint(1, SCOPE) for i in range(LIST_LENGTH)]
lst_random = [i for i in range(10000)]
random.shuffle(lst_random)
# print(lst_random)

# for i in range(len(lst_random)-1):
#     for j in range(0, i+1):
#         if lst_random[i+1-j] >= lst_random[i-j]:
#             break
#         else:
#             lst_random[i+1-j], lst_random[i-j] = lst_random[i-j], lst_random[i+1-j]

for i in range(1, len(lst_random)):
    tmp = lst_random[i]
    for j in range(i):
        if tmp <= lst_random[i-1-j]:
            lst_random[i-j] = lst_random[i-j-1]
        else:
            lst_random[i-j] = tmp
            break
    else:
        lst_random[0] = tmp
    # print(lst_random)

print(lst_random)
