# Find middle element in the list

class Node:
    def __init__(self, data):
        self.data = data
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
        print(h.data)
        h = h.next


def search_linked_list(head, k):
    h = head
    i = 0
    while h:
        if k == h.data:
            return i
        i += 1
        h = h.next
    return False


def find_middle_element(head):
    h1 = head
    h2 = head.next
    while h2 and h2.next:
        h1 = h1.next
        h2 = h2.next.next
    return h1.data


def delete_element(head, value):
    h = head
    while h.next:
        if h.next.data == value:
            h.next = h.next.next
        else:
            h = h.next
    return head


if __name__ == '__main__':
    a = [2, 4, 3, 7, 9, 4, 6, 7]
    linked_list = Node(a[0])
    for i in a[1::]:
        linked_list = insert(linked_list, i)
    traverse(linked_list)
    print("Element {} present at index {}.".format(3, search_linked_list(linked_list, 3)))
    print("Middle element of the list is: {}".format(find_middle_element(linked_list)))
    print("Elements after deletion:")
    new_link_list = delete_element(linked_list, 7)
    traverse(new_link_list)

