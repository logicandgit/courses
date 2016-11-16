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
    third = push(None, 3)
    second = push(third, 2)
    head = push(second, 1)

    return head


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

if __name__ == '__main__':
    print(sorted_insert(build_one_two_three(), 2.5).next.next.data)
    print(sorted_insert(build_one_two_three(), 0.5).data)
    print(sorted_insert(build_one_two_three(), 3.5).data)
    print(sorted_insert(None, 23).data)

