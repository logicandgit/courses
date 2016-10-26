def count_by(x, n):
    # temp = x
    # res = [temp]
    # for y in range(1, n):
        # temp += x
        # res.append(temp)
    # return res
    return [x * y for y in range(1, n + 1)]
if __name__ == '__main__':
    print(count_by(50, 5))
