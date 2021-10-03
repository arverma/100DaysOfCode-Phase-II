def find_island(arr):
    arr = mark_visited_index(arr, 0, 0, len(arr), len(arr[0]))
    [print("\t".join([str(i) for i in j])) for j in arr]


def mark_visited_index(arr, i, j, n, m):
    if i < 0 or i >= n or j >= m or m < 0:
        return
    if arr[i][j] in (-1, 1):
        return
    arr[i][j] = 1
    mark_visited_index(arr, i + 1, j, n, m)
    mark_visited_index(arr, i - 1, j, n, m)
    mark_visited_index(arr, i, j + 1, n, m)
    mark_visited_index(arr, i, j - 1, n, m)
    return arr


grid = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
]

print(find_island(grid))
