# 线性查找

seasons = ['spring', 'summer', 'fall', 'winter']


def linear_search(lst, value):
    for ind, v in enumerate(lst, 1):
        if v == value:
            return ind
    else:
        return None


print(linear_search(seasons, 'summer1'))
