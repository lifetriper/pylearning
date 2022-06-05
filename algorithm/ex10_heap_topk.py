import random

LENGTH = 30


def sift(lst, root, last_leaf):
    tmp = lst[root]
    i = 2*root+1
    while i < last_leaf:
        if i+1 <= last_leaf and lst[i] > lst[i+1]:
            i = i+1
        if lst[i] < tmp:
            lst[root] = lst[i]
            root = i
            i = 2*root+1
        else:
            lst[root] = tmp
            break
    else:
        lst[root] = tmp


def heap_topk(lst, k):
    for i in range((k-2) // 2, -1, -1):
        sift(lst, i, k-1)
    for i in range(k, len(lst)):
        if lst[i] > lst[0]:
            lst[0] = lst[i]
            sift(lst, 0, k-1)


lst_random = [random.randint(1, 100) for i in range(20)]
random.shuffle(lst_random)
print(lst_random)
heap_topk(lst_random, 5)
print(lst_random)
