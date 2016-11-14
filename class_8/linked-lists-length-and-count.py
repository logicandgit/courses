# -*- coding: utf-8 -*- 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    head1 = new_node
    return head1


def build_one_two_three():
    third = push(None, 3)
    second = push(third, 2)
    head = push(second, 1)

    return head


def length(node):
    res = 0
    while node:
        res += 1
        node = node.next
    return res


def count(node, data):
    res = 0
    while node:
        if node.data == data:
            res += 1
        node = node.next
    return res

if __name__ == '__main__':
    list_node = build_one_two_three()

    print(length(None))
    print(length(Node(99)))
    print(length(list_node))
    print
    print(count(list_node, 1))
    print(count(list_node, 99))
    print(count(None, 1))


