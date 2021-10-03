def add_k(arr, k):
    return map(lambda x: x + k, arr)


def add_two_array(arr1, arr2):
    return map(lambda x, y: x + y, arr1, arr2)


def divide_elements_two_array(arr1, arr2):
    """
    This demonstrate lazy evaluation, since 1st 3 elements are
    printed and then the exception occurred
    :param arr1:
    :param arr2:
    :return:
    """
    return map(lambda x, y: x / y, arr1, arr2)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 0, 5]
    [print(i, end=" ") for i in add_k(a, 10)]
    print()
    [print(i, end=" ") for i in add_two_array(a, b)]
    print()
    [print(i, end=" ") for i in divide_elements_two_array(a, b)]
