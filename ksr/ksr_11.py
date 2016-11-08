# -*- coding: utf-8 -*- 
def get_count_string(path, string):
    with open(path) as orig_file:
        return orig_file.read().count(string)

if __name__ == '__main__':
    print get_count_string('logs.txt', 'asdf')