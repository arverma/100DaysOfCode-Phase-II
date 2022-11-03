def even_odd_index_sum_O_n(arr):
    left_even, left_odd = [0], [0]
    n = len(arr)
    right_even, right_odd = [0]*n, [0]*n

    for i in range(1, n):
        if i % 2 == 0:
            left_even.append(left_even[i - 1] + arr[i])
            left_odd.append(left_odd[i - 1])
        else:
            left_even.append(left_even[i - 1])
            left_odd.append(left_odd[i - 1] + arr[i])

        if (n - 1 - i) % 2 == 0:
            right_even[n-1-i] = right_even[i - 1] + arr[n - 1 - i]
            right_odd[n-1-i] = right_odd[i - 1]
        else:
            right_odd[n-1-i] = right_even[i - 1]
            right_odd[n-1-i] = right_odd[i - 1] + arr[n - 1 - i]

    print(left_even, left_odd)
    print(right_even, right_odd)
    count = 0
    for i in range(n):
        print(left_even[i], right_odd[i], right_even[i], left_odd[i])
        if left_even[i] + right_odd[i] == right_even[i] + left_odd[i]:
            count += 1
    return count


def even_odd_index_sum_O_n_square(arr):
    even_func = lambda x: x % 2 == 0
    count = 0
    for index, val in enumerate(arr):
        new_arr = arr[0:index] + arr[index+1::]
        even_sum = sum([a for i, a in enumerate(new_arr) if even_func(i)])
        odd_sum = sum([a for i, a in enumerate(new_arr) if even_func(i) == False])
        if odd_sum == even_sum:
            count += 1
            print(index, arr[index])
    return count


if __name__ == '__main__':
    arr = [2, 1, 6, 4]
    # arr = [1, 1, 1]

    # O(n^2)
    print(even_odd_index_sum_O_n_square(arr))

    # O(n)
    print(even_odd_index_sum_O_n(arr))

