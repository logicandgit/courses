# -*- coding: utf-8 -*- 
def found_triangular(nth):
    result = (1 * nth * (nth + 1)) / 2
    return result

if __name__ == '__main__':
    print found_triangular(1)
    print found_triangular(3)
    print found_triangular(5)
