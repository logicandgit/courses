def symmetric_point(p, q):
    # len_x = q[0] - p[0]
    # len_y = q[1] - p[1]
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]
if __name__ == '__main__':
    print('-----------------------------------')
    print(symmetric_point([0, 0], [1, 1]))
    print(symmetric_point([2, 6], [-2, -6]))
    print(symmetric_point([1000, 15], [-7, -214]))
