def pattern(n):
    result = ""
    for i in range(n):
        if i:
            result += "1{}{}\n".format('*' * i, str(i + 1))
        else:
            result += "1\n"
    return result[:-1]
    # return ''.join(["1{}{}\n".format('*' * i, str(i + 1)) if i else "1\n" for i in range(n)])[:-1]

if __name__ == '__main__':
    print(pattern(5))
