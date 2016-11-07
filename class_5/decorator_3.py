# -*- coding: utf-8 -*- 
import os
import time


def logger(path='logs.txt', day=1):
    def wrapper(func):
        def replacement_function(*args, **kwargs):
            # count_date = 86400 * day
            count_date = 3600 * day
            creation_time_file = os.path.getctime(path)
            now = time.time()
            time_live_file = now - creation_time_file

            if time_live_file > count_date:
                os.remove(path)

            with open(path, 'a') as log_file:
                # date_time = time.asctime(time.localtime())
                date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                log_file.write('Function {} is execute at {}\n'.format(func.__name__, date_time))
            return func(*args, **kwargs)
        return replacement_function
    return wrapper


@logger('a.txt')
def summarize(x, y):
    return x + y


@logger('a.txt')
def mult(x, y):
    return x * y

if __name__ == '__main__':
    summarize(1, 2)
    summarize(3, 4)
    summarize(5, 6)
    mult(7, 8)
