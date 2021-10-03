from functools import lru_cache, reduce, partial


@lru_cache(100)
def calculate_fib_nos(n):
    if n <= 0:
        return 0
    elif n in (1, 2):
        return 1
    return calculate_fib_nos(n - 1) + calculate_fib_nos(n - 2)


def calculate_sum_of_arr(arr):
    return reduce(lambda x, y: x + y, arr, 80)


def add_two_num(a, b):
    return a+b


if __name__ == '__main__':
    print(calculate_fib_nos(10))
    a = [i for i in range(10)]
    print(calculate_sum_of_arr(a))

    print(add_two_num(10, 1))
    add_one = partial(add_two_num, a=1)
    print(add_one(b=10))
    add_one = partial(add_two_num, b=3)
    print(add_one(a=1))
    add_one = partial(add_two_num, 4)
    print(add_one(9))
