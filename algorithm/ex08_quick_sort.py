import random


def partition(data, left, right):
    temp = data[left]
    while left < right:
        while data[right] >= temp and right > left:
            right -= 1
        data[left] = data[right]
        while data[left] <= temp and right > left:
            left += 1
        data[right] = data[left]
    data[left] = temp
    print(data)
    return left


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)


lst_random = [i for i in range(1, 10001)]

random.shuffle(lst_random)

# lst_random = [5, 1, 2, 5, 6, 7, 8, 5, 2, 3, 5, 6, 7, 9]
# lst_random = [4, 2, 3, 8, 7, 6, 1, 9, 5]
print(lst_random)

quick_sort(lst_random, 0, len(lst_random)-1)
print(lst_random)
