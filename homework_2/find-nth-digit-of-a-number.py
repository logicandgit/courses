def find_digit(num, nth):
    res = -1
    if 0 < nth:
        res = (abs(num) // 10**(nth-1)) % 10
    return res

if __name__ == '__main__':
    print(find_digit(-123412341234, 3))
