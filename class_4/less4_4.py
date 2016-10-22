def is_magic_square(square):
    """TODO: Check square on magic properties
    :square: array
    :returns: "Not magic square" or "Magic square"

    """
    len_square = len(square)
    magic_number = len_square*(len_square**2 + 1)/2
    sum_main_diagonals = 0
    sum_second_diagonals = 0

    for line in range(len_square):
        sum_column = 0

        if sum(square[line]) != magic_number:
            return "Not magic square"

        for column in range(len_square):
            sum_column += square[column][line]

            if line == column:
                sum_main_diagonals += square[line][column]

            if column == (len_square - line - 1):
                sum_second_diagonals += square[line][column]

        if sum_column != magic_number:
            return "Not magic square"

    if sum_main_diagonals != magic_number or sum_second_diagonals != magic_number:
        return "Not magic square"

    return "Magic square"


if __name__ == "__main__":
    print(is_magic_square([[2, 7, 6], [9, 5, 2], [4, 3, 8]]))
    print(is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
    print(is_magic_square([[4, 23, 7, 15, 16],
                           [12, 20, 1, 24, 8],
                           [21, 9, 13, 17, 5],
                           [18, 2, 25, 6, 14],
                           [10, 11, 19, 3, 22]]))
