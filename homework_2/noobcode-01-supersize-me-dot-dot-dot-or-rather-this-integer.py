def super_size(n):
    res = ''

    result = [str(n)[i] for i in range(len(str(n)))]
    result.sort(reverse=True)

    for i in result:
        res += str(i)
    return int(res)

if __name__ == '__main__':
    super_size(123456)
