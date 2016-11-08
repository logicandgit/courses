# -*- coding: utf-8 -*- 
def add_min_member_array(array):
    sum_array = sum(array)
    all_number = range(-9, 10)
    if sum_array:
        diff = sum_array - 0

        if diff > 0:
            for number in all_number:
                sum_array = sum(array)
                diff = sum_array - 0

                if diff + number > 0:
                    array.append(number)
                elif not diff + number:
                    array.append(number)
                    return array

        if diff < 0:
            for number in reversed(all_number):
                sum_array = sum(array)
                diff = sum_array - 0

                if diff + number < 0:
                    array.append(number)
                elif not diff + number:
                    array.append(number)
                    return array
    return array

if __name__ == '__main__':
    print add_min_member_array([1, 2, 3, -1, 0, 4])
    print add_min_member_array([1, 2, 3, -1, 0, 5])
    print add_min_member_array([-2, -2, -3, -1, 0, -4])
