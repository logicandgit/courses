# -*- coding: utf-8 -*-
def get_sum_members_number(n):
    sum_numbers = 0
    temp_value = n
    while temp_value > 0:
        temp_value, remainder = divmod(temp_value, 10)
        sum_numbers += remainder
    return sum_numbers


def get_number_sum_member_equally_seven():
    result = []

    for number in range(100, 1000):
        if get_sum_members_number(number) == 7:
            result.append(number)
    return result


if __name__ == '__main__':
    print get_number_sum_member_equally_seven()
