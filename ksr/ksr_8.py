# -*- coding: utf-8 -*-
def unpack_array(array, res):
    for i in array:
        if isinstance(i, list):
            unpack_array(i, res)
        else:
            res.append(i)


def get_max_value(array):
    res = []
    unpack_array(array, res)

    return max(res)

if __name__ == '__main__':
    print get_max_value([[0, 4, [3, 4]], [-4, 5, 6], [3]])
