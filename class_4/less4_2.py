def check_uniqueness_array(array):
    """Check the unique elements of the two-dimensional list.

    :array: Check the unique elements of the two-dimensional list.
    :returns: "Unique" or "Not unique"

    """
    for internal in array:
        if len(set(internal)) != len(internal):
            return False
    return True


if __name__ == "__main__":
    print(check_uniqueness_array([[1, 2, 3], [-4, 3, 6]]))
