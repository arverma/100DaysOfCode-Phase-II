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


def add_one(head):
    if head.next is None:
        head.val += 1
        return head

    temp = head
    rightmost_non_9 = head
    while temp.next:
        if temp.val != 9:
            rightmost_non_9 = temp
        temp = temp.next
    if temp.val == 9:
        temp = rightmost_non_9
        temp.val += 1
        while temp.next:
            temp = temp.next
            temp.val = 0
    else:
        temp.val += 1
    return head


if __name__ == '__main__':
    a = [2, 9, 0, 9, 9]  # [2, 9, 1, 0, 0]
    linked_list = Node(a[0])
    for i in a[1::]:
        linked_list = insert(linked_list, i)
    traverse(linked_list)
    l = add_one(linked_list)
    traverse(l)