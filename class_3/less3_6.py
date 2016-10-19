def percent(strings):

    def _count_per(n):
        return round(100 * float(n)/float(len(strings)), 2)

    count_a = count_d = count_w = 0

    for char in strings:
        if char.isalpha():
            count_a += 1
        elif char.isdigit():
            count_d += 1
        else:
            count_w += 1

    return map(_count_per, [count_a, count_d, count_w])

if __name__ == "__main__":
    print(percent('wqwe3'))
