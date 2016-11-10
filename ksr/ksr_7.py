# -*- coding: utf-8 -*- 
def get_turn_array(array):
    return map(list, zip(*array))

if __name__ == '__main__':
    print get_turn_array([[1, 2, 3], [4, 5, 6]])
