# -*- coding: utf-8 -*- 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    if not head:
        Node(data)
    else:
        Node(data)
        Node.next = head
    return Node


def build_one_two_three():
    push(None, 3)
    push(Node(3), 2)
    push(Node(2), 1)
    return Node

if __name__ == '__main__':
    print(push(None, 1).data)
