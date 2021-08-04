# Binary search

def binary_search(arr, k):
    mid = len(arr)//2
    if k != arr[mid] and mid < 1:
        return False
    if k == arr[mid]:
        return True
    elif k > arr[mid]:
        return binary_search(arr[mid:], k)
    else:
        return binary_search(arr[:mid], k)


if __name__ == '__main__':
    l = [0, 1, 2, 3, 4, 56, 78, 89]
    for i in range(100):
        print(i, "Present" if binary_search(l, i) else "Not Present")