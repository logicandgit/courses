# -*- coding: utf-8 -*- 
def get_turn_array(array):
    new_list = []
    columns = map(lambda x, y: (x, y), array[0], array[1])

    for column in columns:
        new_list.append(list(column))
    return new_list

if __name__ == '__main__':
    print get_turn_array([[1, 2, 3], [4, 5, 6]])
