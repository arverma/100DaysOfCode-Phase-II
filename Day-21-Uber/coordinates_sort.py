def coordinates(arr):
    arr.sort()
    marker = arr[0][1] - arr[0][0] + 1
    for i in range(len(arr)-1):
        if arr[i][1] >= arr[i+1][0]:
            marker += (arr[i+1][1]-arr[i][1])
        else:
            marker += (arr[i+1][1] - arr[i+1][0] + 1)
    return marker


if __name__ == '__main__':
    arr = [[4, 7], [-1, 5], [3, 6]]  # 9
    # arr = [[4, 7], [8, 10], [9, 13], [-1, 5], [3, 6]] #15
    print(coordinates(arr))
