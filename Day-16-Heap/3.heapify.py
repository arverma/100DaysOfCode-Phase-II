def heapify(h):
    i = len(h)-1
    while i >= 0:
        l = 2*i + 1
        r = 2*i + 2
        p = i
        while r < len(h):
            # print(h[i])
            if h[l] > h[r] and h[p] < h[l]:
                h[l], h[p] = h[p], h[l]
                p = l
            elif h[l] < h[r] and h[p] < h[r]:
                h[r], h[p] = h[p], h[r]
                p = r
            else:
                p = len(h)
            l = 2 * p + 1
            r = 2 * p + 2
        i -= 1

    return h


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapify(a))
    print(heapify([9, 8, 7, 4, 5, 6, 3, 2, 1]))
