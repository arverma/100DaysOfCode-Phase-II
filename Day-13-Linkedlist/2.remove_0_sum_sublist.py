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


def remove_zero_sum_sublist(head):
    prefix = 0
    seen = {}
    seen[0] = dummy = Node(0)
    dummy.next = head
    while head:
        prefix += head.val
        seen[prefix] = head
        # print("prefix", prefix)
        head = head.next
    head = dummy.next
    prefix = 0
    print([(i, j.val) for i, j in seen.items()])
    while head:
        prefix += head.val
        head.next = seen[prefix].next
        print("prefix", prefix, head.val)
        head = head.next
    return dummy.next


if __name__ == '__main__':
    a = [3, 2, -3, -2, 5, 100, -5, -100, 1]  # [3, 2, -3, -2, 5, 100, -100, 1]
    linked_list = Node(a[0])
    for i in a[1::]:
        linked_list = insert(linked_list, i)
    traverse(linked_list)
    res = remove_zero_sum_sublist(linked_list)
    traverse(res)
