def sum_mul(n, m):
    if n > 0 and m > 0:
        return sum([i for i in range(m) if i % n == 0])
    return 'INVALID'

if __name__ == '__main__':
    print(sum_mul(10, 9))
