def unpack_array(array, res):
    """Unpack the arbitrary nested array and saves all value into the list
    :array: array with arbitrary nested
    :res: list will be saved elements array
    """
    for i in range(len(array)):
        if type(array[i]) == type(array):
            unpack_array(array[i], res)
        else:
            res.append(array[i])


def check_uniqueness_array(array):
    """Check the unique elements of the array.

    :array: list
    :returns: "Unique" or "Not unique"

    """
    res = []
    unpack_array(array, res)

    if len(set(res)) == len(res):
        return True
    return False


if __name__ == "__main__":
    print(check_uniqueness_array([['ab', 'a', [3, 4]], [-4, 5, 6]]))
    print(check_uniqueness_array([['a', 'a', [3, 4]], [-4, 5, 6]]))
    print(check_uniqueness_array([['ab', 'a', [3, 4]], [-4, 5, 6], [3]]))
