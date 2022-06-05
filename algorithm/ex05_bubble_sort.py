import random

LENGTH = 20
RANDOM_SCOPE = 90

lst_random = []


def bubble_sort(li):
    for j in range(len(li) - 1):
        for k in range(len(li) - j - 1):
            if lst_random[k] > lst_random[k+1]:
                lst_random[k], lst_random[k+1] = lst_random[k+1], lst_random[k]


lst_random = [random.randint(0, RANDOM_SCOPE) for i in range(LENGTH)]
print(lst_random)
bubble_sort(lst_random)
print(lst_random)
