# Merge sort

def merge(Left, Right, arr):
    i, j = 0, 0
    k = 0
    while i < len(Left) and j < len(Right):
        if Left[i] <= Right[j]:
            arr[k] = Left[i]
            i += 1
        else:
            arr[k] = Right[j]
            j += 1
        k += 1
    for p in range(j, len(Right)):
        arr[k] = Right[p]
        k += 1
    for q in range(i, len(Left)):
        arr[k] = Left[q]
        k += 1


def merge_sort(a):
    if len(a) < 2:
        return
    else:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, a)


if __name__ == '__main__':
    arr = [2, -1, 2, 9, 4, 5, 3, -100]
    merge_sort(arr)
    [print(i) for i in arr]