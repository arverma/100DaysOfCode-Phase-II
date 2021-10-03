class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def insert(head, data):
    h = head
    while h.next:
        h = h.next
    h.next = Node(data)
    return head


def traverse(head):
    h = head
    while h:
        print(h.val, end=" ")
        h = h.next
    print()


def reverse_ll_extra_space(head, k):
    temp = Node(head.val)
    head = head.next
    res = None
    while head:
        res = Node(head.val)
        res.next = temp
        temp = res
        head = head.next
    return res


def reverse_ll_without_extra_space(head, k):
    prev = head.next
    head.next = None
    while prev:
        curr = prev.next
        prev.next = head
        head = prev
        prev = curr
    return head


def reverse_ll_in_group_without_extra_space(head, k):
    current = head
    prev, next = None, None

    count = 0
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    return prev


def reverse(head, k):
    if head is None:
        return None

    current = head
    prev, next = None, None

    count = 0
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    print("head.val", head.val)
    head.next = reverse(next, k)
    print(prev.val)
    return prev


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    linked_list = Node(a[0])
    for i in a[1::]:
        linked_list = insert(linked_list, i)
    traverse(linked_list)
    # l = reverse_ll_extra_space(linked_list, 4)
    # traverse(l)
    # l1 = reverse_ll_without_extra_space(linked_list, 4)
    # traverse(l1)
    l2 = reverse(linked_list, 3)
    traverse(l2)
