def max_heapify(h):
    c = len(h)-1
    while c:
        p = c
        if c%2 == 0:
            c = c//2 -1
        else:
            c = c//2
        if h[p] > h[c]:
            h[p], h[c] = h[c], h[p]
    return h


def heap_pop(h):
    max_val = h[0]
    h = [h[-1]] + h[1:-1]
    l = 1
    r = 2
    p = 0
    while r < len(h):
        if h[l] < h[r]:
            h[p], h[r] = h[r], h[p]
            p = r
        else:
            h[p], h[l] = h[l], h[p]
            p = l
        l = 2 * p + 1
        r = 2 * p + 2
    return max_val, h


def insert(h, value):
    h.append(value)
    return max_heapify(h)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    # Insert
    heap = []
    for element in a:
        heap = insert(heap, element)
        print(heap)

    # Delete
    for h in heap:
        val, heap = heap_pop(heap)
        print(val, heap)


