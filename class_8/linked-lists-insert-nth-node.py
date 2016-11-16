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


def insert_nth(head, index, data):
    try:
        head_node = head
        if index:
            index -= 1
            while head_node:
                if not index:
                    new_node = Node(data)
                    new_node.next = head_node.next
                    head_node.next = new_node
                    return head
                index -= 1
                # old_node = head
                head_node = head_node.next
            raise Exception('Invalid index value should raise error.')
        if not index:
            new_node = Node(data)
            new_node.next = head
            return new_node
    except Exception:
        return Exception.message

if __name__ == '__main__':
    list_node = build_one_two_three()
    # print(insert_nth(build_one_two_three(), 1, 23).data)
    print(insert_nth(build_one_two_three(), 1, 23).next.next.data)
    # print(insert_nth(build_one_two_three(), 3, 23).data)
    # print(insert_nth(None, 0, 12).data)
    # print(insert_nth(None, 0, 12).next)
