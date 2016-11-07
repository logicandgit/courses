# -*- coding: utf-8 -*-
import sys
import os


def read_and_sort(inputf):
    # all_lines = []
    with open(inputf, 'r+') as open_file:
        all_lines = open_file.read().split('\n')
        all_lines = sorted(all_lines, key=len)
        open_file.seek(0)
        open_file.write('\n'.join(all_lines))


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception('Need one argument, path to file')

        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            raise Exception('File is absent by path: {}'.format(file_path))
        # file_path = 'b.txt'
        read_and_sort(file_path)
    except Exception, err:
        print(err.message)
