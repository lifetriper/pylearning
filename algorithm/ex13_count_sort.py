import random

SCOPE = 30


def count_sort(lst, max_no):
    lst1 = [0 for _ in range(max_no+1)]
    for i in lst:
        lst1[i] += 1
    lst.clear()
    for ind, val in enumerate(lst1):
        for i in range(val):
            lst.append(ind)


lst_random = [random.randint(1, SCOPE+1) for i in range(20)]
print(lst_random)
count_sort(lst_random, SCOPE)
print(lst_random)
