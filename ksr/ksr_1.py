# -*- coding: utf-8 -*- 
def check_multiple(n):
    if n % 3 == 0 and n % 10 == 0:
        return True
    return False

if __name__ == '__main__':
    print check_multiple(10)
    print check_multiple(3)
    print check_multiple(30)
    print check_multiple(21)
    print check_multiple(60)
