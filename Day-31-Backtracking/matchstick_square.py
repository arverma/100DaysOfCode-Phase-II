def can_make_square(a, i, side, square):
    if i == len(a):
        return True

    for j in range(4):
        if square[j] + a[i] <= side:
            square[j] = square[j] + a[i]
            if can_make_square(a, i+1, side, square):
                return True
            square[j] = square[j] - a[i]

    return False


if __name__ == '__main__':
    a = [1, 1, 2, 2, 2]
    side_length = sum(a)/4
    if side_length == int(side_length):
        output = can_make_square(a, i=0, side=side_length, square=[0]*4)
    else:
        output = False
    print(output)

    a = [2, 2, 4, 4, 4, 4]
    side_length = sum(a)/4
    if side_length == int(side_length):
        output = can_make_square(a, i=0, side=side_length, square=[0]*4)
    else:
        output = False
    print(output)
