def calculate_average(value, *args):
    return float(sum(args) + value) / (len(args) + 1) if args else value


def calculate_array(array):
    negative_value = []

    for i in range(2):
        for y in range(len(array[i])):
            if array[i][y] < 0:
                negative_value.append(array[i][y])

    if negative_value:
        return calculate_average(*negative_value)
    else:
        return "NOTHING"

if __name__ == "__main__":
    print calculate_array([[1, -2, 3], [4, -5, 6]])
