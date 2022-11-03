def find_length_of_longest_nonrepeating_subsequence(s):
    if len(s) == 0:
        return 0

    i = 0
    res = 1
    lookup = {s[i]: i}
    for j in range(1, len(s)):
        if lookup.get(s[j], -1) >= i:
            i = lookup.get(s[j]) + 1
        else:
            res = max(res, j - i + 1)
        lookup[s[j]] = j
    return res


if __name__ == '__main__':
    string = "bbtablud"
    output = find_length_of_longest_nonrepeating_subsequence(string)
    print(output)