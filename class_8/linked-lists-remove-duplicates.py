# -*- coding: utf-8 -*- 
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_one_two_three():
    third = push(None, 1)
    second = push(third, 2)
    head = push(second, 3)

    return head


def insert_sort(head):
    if not head:
        return

    def sorted_insert(head, data):
        head_node = head
        old_node = None
        if head:
            while head_node:
                if data <= head_node.data:
                    new_node = Node(data)
                    new_node.next = head_node
                    if old_node:
                        old_node.next = new_node
                        return head
                    return new_node
                old_node = head_node
                head_node = head_node.next
            new_node = Node(data)
            old_node.next = new_node
            return head
        new_node = Node(data)
        new_node.next = head
        return new_node

    res = Node(head.data)
    head = head.next

    while head:
        res = sorted_insert(res, head.data)
        head = head.next

    return res


def remove_duplicates(head):
    res = head
    while head:
        if head.next:
            if head.data == head.next.data:
                head.next = head.next.next
            else:
                head = head.next
        else:
            break
    return res

if __name__ == '__main__':
    print(remove_duplicates(None))
    print(remove_duplicates(Node(23)))
    # print(insert_sort(build_one_two_three()).next.data)


