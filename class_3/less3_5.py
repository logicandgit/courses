def check_simple(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True


def multi(number):
    for i in reversed(range(number)):
        if (not number % i) and check_simple(i):
            return i
    return 1


if __name__ == "__main__":
    print(multi(15))
