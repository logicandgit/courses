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

if __name__ == '__main__':
    print(push(None, 1).data)
    print(push(None, 1).next)
    print(push(Node(1), 2).data)
    print(push(Node(1), 2).next.data)
    print
    print(build_one_two_three().next.next.data)
