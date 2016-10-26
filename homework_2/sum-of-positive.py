def positive_sum(arr):
    total = 0
    for i in arr:
        total += i if i >= 0 else 0
    return total

if __name__ == '__main__':
    print(positive_sum([1, -2, 3, 4, 5]))
