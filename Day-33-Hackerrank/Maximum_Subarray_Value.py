def find_maximum_sum_array(arr):
    even = arr[0]
    start, odd = 0, 0
    ans = even**2

    for i in range(1, len(arr)):
        index = i - start

        if index%2 == 0:
            t1 = (even+arr[i]-odd)**2
        else:
            t1 = (even - arr[i] - odd) ** 2
        t2 = arr[i]**2

        if t2 > t1:
            ans = max(ans, t2)
            even = arr[i]
            odd = 0
            start = i
        else:
            ans = max(ans, t1)
            if index%2 == 0:
                even += arr[i]
            else:
                odd += arr[i]
    return ans


if __name__ == '__main__':
    # arr = [-1, 2, 3, 4, -5] # 81
    # arr = [1, -2, -3, 7, 5] # 100
    arr = [1, -1, 1, -1, 1] # 25
    print(find_maximum_sum_array(arr))