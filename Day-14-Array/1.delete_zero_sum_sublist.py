def remove_zero_sum_sub_list(arr):
    res = {}
    prefix = 0
    for i, a in enumerate(arr):
        prefix += a
        res[prefix] = i
        print(prefix, i)
    print(res)


if __name__ == '__main__':
    remove_zero_sum_sub_list([3, 2, -3, -2, 5, 100, -5, -100, 1])  # [1]
