def fiban(n):
    res = [1, 1]
    for i in range(1, n-1):
        res.append(res[i-1] + res[i])
    return res[n-1]

if __name__ == '__main__':
    print(fiban(5))
