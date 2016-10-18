def sum_mul(n, m):
    if 0 < n and 0 < m:
        return sum([i for i in range(m) if i % n == 0])
    return 'INVALID'

if __name__ == '__main__':
    print(sum_mul(10, 9))
