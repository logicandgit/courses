def no_boring_zeros(n):
    for i in reversed(range(len(str(n)))):
        if not (n % 10 ** i):
            return n // 10 ** i

if __name__ == '__main__':
    print(no_boring_zeros(1100))
