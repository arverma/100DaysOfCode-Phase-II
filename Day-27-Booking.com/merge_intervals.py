def insert_in_a_sorted_array(a, x):
    for i in range(len(a)):
        if a[i][0] > x[0]:
            return a[0:i] + [x] + a[i::]
    return a + [x]


def insert_merge(a, x):
    res = []
    for a in insert_in_a_sorted_array(a, sorted(x)):
        if res and res[-1][1] >= a[0]:
            res[-1][1] = max(res[-1][1], a[1])
        else:
            res += [a]
    return res


if __name__ == '__main__':
    arr = [[1, 2], [3, 6]]
    x = [10, 8]
    # output = (1, 2) (3, 6) (8, 10)
    output = insert_merge(arr, x)
    print(output)

    arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    x = [4, 9]
    # [[1,2],[3,5],[4,9], [6,7],[8,10],[12,16]]
    # output = [1,2],[3,10],[12,16]
    output = insert_merge(arr, x)
    print(output)

    arr = [[1, 3], [6, 9]]
    x = [2, 5]
    # output = [1,5],[6,9]

    output = insert_merge(arr, x)
    print(output)
