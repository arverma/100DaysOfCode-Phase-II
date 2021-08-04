# Write fibonacci series

def nth_fibonacci(x, y, n):
    if n > 0:
        nth_fibonacci(y, x + y, n - 1)
    else:
        print(x + y)


def all_n_fibonacci(x, y, n):
    if n > 0:
        print(x + y)
        all_n_fibonacci(y, x + y, n - 1)
    else:
        print(x + y)


def all_n_fibonacci_in_reverse(x, y, n):
    if n > 0:
        all_n_fibonacci_in_reverse(y, x + y, n - 1)
        print(x + y)
    else:
        print(x + y)


if __name__ == '__main__':
    a, b = 0, 1
    n = 25
    nth_fibonacci(a, b, n+2)
    all_n_fibonacci(a, b, n+2)
    all_n_fibonacci_in_reverse(a, b, n + 2)


# res = {}
# def fibonacci(n):
#     if res.get(n):
#         return res.get(n)
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         res[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return res[n]
#
#
# if __name__ == '__main__':
#     print(fibonacci(128))