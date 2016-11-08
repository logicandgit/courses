# -*- coding: utf-8 -*- 
def is_palindrome(string):
    reversed_chars = []
    for char in string:
        reversed_chars.insert(0, char)
    reversed_string = ''.join(reversed_chars)
    if reversed_string == string:
        return True
    return False

if __name__ == '__main__':
    print is_palindrome('asdf')
    print is_palindrome('aaa')
    print is_palindrome('asdffdsa')
    print is_palindrome('asdf fdsa')
    print is_palindrome('asdff fdsa')
