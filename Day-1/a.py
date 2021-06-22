# https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/

import math


def find_sqrt(num, n):
    ans = num
    start = 0
    end = num
    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            ans = mid
            break
        elif mid * mid < num:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    incr = 0.1
    for i in range(n):
        while ans * ans <= num:
            ans += incr
        ans -= incr
        incr /= 10
    return ans


a = [50, 6, 3, 9, 0, 11, 16, 65, 96, 144]
for a_i in a:
    print(round(find_sqrt(a_i, 4), 4), math.sqrt(a_i))
