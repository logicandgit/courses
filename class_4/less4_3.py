def add_sum_last_element(array):
    """TODO: Write to the last row of the matrix element,
             the amount of the previous same line.

    :array: array digit
    :returns: array with  the last row of the matrix element,
              the amount of the previous same line.

    """
    for line in range(len(array)):
        array[line].append(sum(array[line]))
    return array

if __name__ == "__main__":
    print(add_sum_last_element([[1, 2, 3], [4, 5, 6], [1, 2, 3]]))
