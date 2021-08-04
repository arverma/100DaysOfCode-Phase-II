# Print Duplicates in a list

def print_duplicates(arr):
    res = {}
    for i in arr:
        res[i] = res.get(i, 0) + 1
    [print(i) for i, j in res.items() if j >= 2]


if __name__ == '__main__':
    print_duplicates(["aman", 1, 3, 2, 1, "aman", "ranj", 3.45, 2.1, 3.45])