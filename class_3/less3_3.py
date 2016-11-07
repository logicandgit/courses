def fiban(n):
    first = 1
    second = 1
    for i in range(1, n):
        first, second = second, first + second
    return first


# def fiban_rec(n):  # not sure about memory
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fiban_rec(n - 1) + fiban_rec(n - 2)

if __name__ == '__main__':
    print(fiban(8))
    # print(fiban_rec(8))
