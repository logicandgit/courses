def calculate_average(value, *args):
    return float(sum(args) + value) / (len(args) + 1) if args else value


def calculate_array(array):
    negative_value = []

    for i in array:
        for y in i:
            if y < 0:
                negative_value.append(y)

    if negative_value:
        return calculate_average(*negative_value)
    else:
        return "NOTHING"

if __name__ == "__main__":
    print calculate_array([[1, -2, 3], [4, -5, 6]])
