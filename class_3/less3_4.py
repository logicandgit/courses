def sum_mul(n):
    sum_numbers = 0
    multiplication_numbers = 1
    temp_value = n
    while temp_value > 0:
        temp_value, number = divmod(temp_value, 10)
        sum_numbers += number
        multiplication_numbers *= number
    return sum_numbers, multiplication_numbers

if __name__ == '__main__':
    print(sum_mul(59))
