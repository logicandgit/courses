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


def append(listA, listB):
    head = listA if listA else listB
    if head != listB and listB:
        while listA.next:
            listA = listA.next
        listA.next = listB
    return head

if __name__ == '__main__':
    # print(append(None, None))
    # print(append(None, build_one_two_three()))
    print(append(build_one_two_three(), Node(4)))
    # print(append(build_four_five_six(), build_one_two_three()).next.next.next.next.next.next)

