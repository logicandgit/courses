def check_uniqueness_array(array):
    """Check the unique elements of the two-dimensional list.

    :array: Check the unique elements of the two-dimensional list.
    :returns: "Unique" or "Not unique"

    """
    res = []
    len_arrays = 0

    for i in range(len(array)):
        len_arrays += len(array[i])
        for y in range(len(array[i])):
            res.append(array[i][y])

    if len(set(res)) == len_arrays:
        return "Unique"
    return "Not unique"


if __name__ == "__main__":
    print(check_uniqueness_array([[1, 2, 3], [-4, 5, 6]]))
