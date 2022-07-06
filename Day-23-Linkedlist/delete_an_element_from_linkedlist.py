from insert_print import traverse_linked_list, create_linked_list


def delete_an_element_at_pos(head_, pos):
    if pos == 0:
        return head_.next
    start, i = head_, 0
    while i < pos - 1:
        # print(head_.data)
        head_ = head_.next
        i += 1
    head_.next = head_.next.next

    return start


if __name__ == '__main__':
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    start = head
    traverse_linked_list(head)
    # alt_head = delete_an_element_at_pos(head, 3)
    # traverse_linked_list(alt_head)
    # traverse_linked_list(start)
    # alt_head = delete_an_element_at_pos(head, 0)
    # traverse_linked_list(alt_head)
    # traverse_linked_list(start)
    alt_head = delete_an_element_at_pos(head, 5)
    traverse_linked_list(alt_head)
