# -*- coding: utf-8 -*- 
def add_min_member_array(array):
    disbalance = sum(array)
    if disbalance:
        k, i = divmod(abs(disbalance), 9)
        sign = -1 * abs(disbalance) / disbalance
        list_to_add = [9 * sign] * k
        array.extend(list_to_add + [i * sign]) if i else array.extend(list_to_add)
    return array, sum(array)

if __name__ == '__main__':
    print add_min_member_array([1, 2, 3, -1, 0, 4])
    print add_min_member_array([1, 2, 3, -1, 0, 5])
    print add_min_member_array([-2, -2, -3, -1, 0, -4])
