def no_boring_zeros(n):
    if n:
        while n % 10 == 0:
            n //= 10
        return n
    return n
    # for i in reversed(range(len(str(n)))):
    #     if not (n % 10 ** i):
    #         return n // 10 ** i

if __name__ == '__main__':
    print(no_boring_zeros(110))
