# -*- coding: utf-8 -*- 
def get_sting_without_incorrect_space(string):
    new_list = string.split()
    begin = ''
    end = ''
    if string[1] == ' ':
        begin = ' '
    if string[-1] == ' ':
        end = ' '
    return '{}{}{}'.format(begin, ' '.join(new_list), end)

if __name__ == '__main__':
    print get_sting_without_incorrect_space('aaa  aaa')
    print get_sting_without_incorrect_space('aaa aaa  ')
    print get_sting_without_incorrect_space('  aaa aaa')
    print get_sting_without_incorrect_space('  aaa    aaa   ')
