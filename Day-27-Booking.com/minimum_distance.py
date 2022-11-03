"""
Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[]. The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples:
Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 and 2 is 1.

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 and 5 is 2.

Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
Output: Minimum distance between 3 and 2 is 1.
"""


def find_minimum_distance(arr, lookup):
    n = len(arr)
    min_dist, p1, p2 = n, n, n
    for i in range(n):
        if arr[i] == lookup[0]:
            p1 = i
        if arr[i] == lookup[1]:
            p2 = i
        min_dist = min(abs(p2-p1), min_dist)
    return min_dist


if __name__ == '__main__':
    arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    lookup = [3, 6]
    print(find_minimum_distance(arr, lookup))

    arr = [2, 5, 3, 5, 4, 4, 2, 3]
    lookup = [3, 2]
    print(find_minimum_distance(arr, lookup))

    arr = [3, 4, 5]
    lookup = [3, 5]
    print(find_minimum_distance(arr, lookup))

    arr = [1, 2]
    lookup = [1, 2]
    print(find_minimum_distance(arr, lookup))
