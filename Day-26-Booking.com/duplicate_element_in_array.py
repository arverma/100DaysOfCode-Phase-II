"""
Question 1: given an array, determine if there are repeated elements. If an element is repeated more than 3 times, return those elements.
"""


def find_duplicate_elements(arr):
    temp_res = {}
    for a in arr:
        temp_res[a] = temp_res.get(a, 0) + 1

    ans = []
    for key, val in temp_res.items():
        if val >= 3:
            ans.append(key)
    return ans


if __name__ == '__main__':
    arr = [1, 2, 1, 1, 4, 3, 4, 3, 4, 4]
    res = find_duplicate_elements(arr)
    print(res)