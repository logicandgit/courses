def pipe_fix(lists):
    min_v = min(lists)
    max_v = max(lists)
    return [i for i in range(min_v, max_v + 1)]

if __name__ == '__main__':
    print(pipe_fix([2, 3, 5, 6, 8, 9]))
