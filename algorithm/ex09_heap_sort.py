import random

SCOPE = 300000


def sift(lst, root, last_leaf):
    tmp = lst[root]
    i = 2*root + 1
    while i <= last_leaf:
        if i+1 <= last_leaf and lst[i+1] > lst[i]:
            i = i+1
        if lst[i] > tmp:
            lst[root] = lst[i]
            root = i
            i = 2*root+1
        else:
            lst[root] = tmp
            break
    else:
        lst[root] = tmp


def heap_sort(lst):
    n = len(lst)
    for i in range((n-2)//2, -1, -1):
        sift(lst, i, n-1)
    for i in range(n):
        lst[0], lst[n-1-i] = lst[n-1-i], lst[0]
        sift(lst, 0, n-2-i)


lst_random = [random.randint(1, SCOPE) for i in range(10000)]
# print(lst_random)
heap_sort(lst_random)
print(lst_random)

