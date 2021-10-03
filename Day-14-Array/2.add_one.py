def add_one(arr):
    res = []
    carry = 1
    for a in arr[::-1]:
        res.append((a+carry)%10)
        carry = (a + carry) // 10
    return res, res[::-1]


if __name__ == '__main__':
    print(add_one([1, 9, 8, 9]))
