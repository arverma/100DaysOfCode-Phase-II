# Merge two sorted array

def merge_two_sorted_array(a, b):
    i, j = 0, 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    for p in range(j, len(b)):
        res.append(b[p])
    for q in range(i, len(a)):
        res.append(a[q])
    return res


if __name__ == '__main__':
    arr1 = [1, 4, 7, 9, 19, 40, 600]
    arr2 = [3, 5, 6, 9, 10]
    print(merge_two_sorted_array(a=arr1, b=arr2))
