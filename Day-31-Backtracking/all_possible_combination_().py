def create_valid_pattern_imp(n, pattern, diff, res):
    if len(pattern) == 2*n and diff == 0:
        res.append(pattern)

    if len(pattern) < 2*n:
        if diff < n:
            create_valid_pattern_imp(n, pattern+"(", diff+1, res)
        if diff > 0:
            create_valid_pattern_imp(n, pattern + ")", diff-1, res)
    return res


def create_valid_pattern(n):
    if n >= 1:
        return create_valid_pattern_imp(n, "", 0, [])
    else:
        return "Not a valid input"


if __name__ == '__main__':
    output = create_valid_pattern(3)
    print(output)

    output = create_valid_pattern(1)
    print(output)

    output = create_valid_pattern(2)
    print(output)