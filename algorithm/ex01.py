import random


def random_list(count, scope):
    lst_random = []
    for i in range(count):
        lst_random.append(random.randint(0, scope))
    return lst_random


lst1 = random_list(7, 20)
lst1.sort()
print(lst1)

a, b = 2, 3
a, b = b, a
print(a, b)

for i in range(10):
    pass
else:
    print(i)

i = 998

if i := i+1 >= 1000:
    print("more than 1000")
else:
    print("less than 1000")

print(i := i+1)
