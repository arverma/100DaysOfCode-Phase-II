__author__ = 'aman.rv'


def find_pow(x, n):
    sign = True if n > 0 else False

    pow = 1
    while n:
        if n % 2 == 1:
            pow *= x
        x *= x
        n = n // 2
    return pow if sign else 1 / sign


if __name__ == '__main__':
    print(find_pow(1.00012, 1024))
