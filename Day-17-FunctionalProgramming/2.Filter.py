def find_odd(arr):
    return filter(lambda x: x % 2 != 0, arr)


# def aman(a, b):
#     return filter(lambda x, y: x == y, zip(a, b))


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    [print(i, end=" ") for i in find_odd(a)]
    # [print(i, end=" ") for i in aman(a, reversed(a))]
    print()
    # returns all non-zero values
    [print(i, end=" ") for i in filter(None, (1, 0, 6))]
    print()
    # returns all non-zero and True values
    [print(i, end=" ") for i in filter(None, (1, 0, False, True))]
