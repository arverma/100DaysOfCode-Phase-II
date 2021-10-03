def min_heapify(h):
    i = len(h)-1
    while i:
        if i%2 == 0:
            p = i//2-1
        else:
            p = i//2
        if h[i] < h[p]:
            h[i], h[p] = h[p], h[i]
        i = p
    return h


def heap_pop(h):
    min_ele = h[0]
    h = [h[-1]] + h[1:-1]
    l, r = 1, 2
    p = 0
    while r < len(h):
        if h[l] < h[r] and h[p] > h[l]:
            h[l], h[p] = h[p], h[l]
            p = l
        elif h[l] > h[r] and h[p] > h[r]:
            h[r], h[p] = h[p], h[r]
            p = r
        # print(h, l, r)
        l = 2*p+1
        r = 2*p+2
    return min_ele, h


def insert(h, value):
    h.append(value)
    return min_heapify(h)


if __name__ == '__main__':
    a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heap = []
    for element in a:
        heap = insert(heap, element)
        print(heap)
    # print(heap)
    for element in heap:
        min_val, heap = heap_pop(heap)
        print(min_val, heap)
