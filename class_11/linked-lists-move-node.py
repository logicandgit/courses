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


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if source:
        new_list = Node(source.data)
        new_list.next = dest
        source = source.next
    return Context(source, new_list)

if __name__ == '__main__':
    print move_node(build_one_two_three(), build_one_two_three())