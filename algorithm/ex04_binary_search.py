lst_number = list(range(3, 10))


def binary_search(lst_number, value):
    pt_left, pt_right = 0, len(lst_number) - 1
    while pt_left <= pt_right:
        pt_mid = int((pt_left + pt_right) / 2)
        if lst_number[pt_mid] == value:
            return pt_mid
        elif lst_number[pt_mid] < value:
            pt_left = pt_mid + 1
        else:
            pt_right = pt_mid - 1
    else:
        return None


print(lst_number, binary_search(lst_number, 3))
