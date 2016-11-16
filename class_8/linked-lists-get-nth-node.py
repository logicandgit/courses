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


def get_nth(node, index):
    try:
        if node:
            if index >= 0:
                while node:
                    if not index:
                        return node
                    index -= 1
                    node = node.next
                raise Exception('Invalid index value should throw error.')
            else:
                raise Exception('Invalid index value should throw error.')
        else:
            raise Exception('None linked list should throw error.')

    except Exception, err:
        return err.message

if __name__ == '__main__':
    list_node = build_one_two_three()
    print(get_nth(list_node, -1))
    print(get_nth(list_node, 1).data)
