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


def removeDuplicates(head):
    h = head
    while h:
        temp = h
        while temp and h.val == temp.val:
            temp = temp.next
        h.next = temp
        h = h.next
    return head


if __name__ == '__main__':
    a = [3, 2, -3, -3, 5, 100, -100, 1]
    linked_list = Node(a[0])
    for i in a[1::]:
        linked_list = insert(linked_list, i)
    traverse(linked_list)
    l = removeDuplicates(linked_list)
    traverse(l)