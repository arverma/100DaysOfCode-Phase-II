class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(a):
    head = Node(a[0])
    start = head
    for element in a[1::]:
        head.next = Node(element)
        head = head.next
    return start


def traverse_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

if __name__ == '__main__':
    a = [2, 1, 4, 8, 19, 0, -1]
    head = create_linked_list(a)
    traverse_linked_list(head)
