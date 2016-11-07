def digitize(n):
    n_copy = n
    result = []
    while n_copy > 0:
        n_copy, number = divmod(n_copy, 10)
        result.append(number)
    reversed(result)
    # for i in range(len(str(n))-1, -1, -1):
    #     position = 10 ** i
    #     res = n_copy // position
    #     n_copy -= res * position
    #     result.insert(0, res)
    return result


if __name__ == '__main__':
    print(digitize(123))
