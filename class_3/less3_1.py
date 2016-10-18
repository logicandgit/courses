def check_simple(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True

if __name__ == '__main__':
    print(check_simple(90))
