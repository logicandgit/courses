# -*- coding: utf-8 -*- 
def is_palindrome(string):
    return string[::-1] == string

if __name__ == '__main__':
    print is_palindrome('asdf')
    print is_palindrome('aaa')
    print is_palindrome('asdffdsa')
    print is_palindrome('asdf, fdsa')
    print is_palindrome('asdff fdsa')
