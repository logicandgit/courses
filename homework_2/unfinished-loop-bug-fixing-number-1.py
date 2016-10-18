def create_array(n):
    # res = []
    # i = 1
    # while i <= n:
        # res.append(i)
        # i += 1
    # return res
    return [i + 1 for i in range(n)]

if __name__ == '__main__':
    print(create_array(2))
