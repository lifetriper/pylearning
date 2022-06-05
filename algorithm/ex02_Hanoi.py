# 汉诺依塔
import functools
import datetime

count = 0


# @functools.lru_cache(maxsize=128, typed=True)
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        global count
        count += 1
        print(f'{a} 移动到 {c}, count={count}, "n, a, b, c" = {n, a, b, c}')
        hanoi(n - 1, b, a, c)


@functools.lru_cache
def hanoi_steps(x):
    if x == 0:
        return 0
    else:
        return 2 * hanoi_steps(x - 1) + 1


hanoi(4, 'A', 'B', 'C')

start_time = datetime.datetime.now()
print(hanoi_steps(64))
end_time = datetime.datetime.now()
print((end_time - start_time).total_seconds())

