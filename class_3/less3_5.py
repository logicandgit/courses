def check_simple(n):
    for i in range(2, n):
        if not n % i:
            return False
    return True


def multi(number):
    result = []
    for i in range(1, number):
        if (not number % i) and check_simple(i):
            result.append(i)
    return max(result)


if __name__ == "__main__":
    print(multi(15))
