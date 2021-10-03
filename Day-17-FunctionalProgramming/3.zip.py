def create_pair(x, y):
    return [(i, j) for i, j in zip(x, y)]


def zip_unzip(x, y):
    zipped = list(zip(x, y))
    print(zipped)
    x, y = list(zip(*zipped))
    print(x, y)


if __name__ == '__main__':
    a = [i for i in range(1, 10)]
    [print(i, end=" ") for i in create_pair(a, reversed(a))]
    print()
    zip_unzip(a, reversed(a))

