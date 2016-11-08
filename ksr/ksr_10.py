# -*- coding: utf-8 -*-
ALL_BRACKETS = '()[]{}'


def logger(path='logs.txt'):
    def wrapper(func):
        def replacement_function(*args, **kwargs):
            try:
                if len(args) != 4:
                    raise Exception('Incorrect count args')

                for value in args[:-1]:
                    if not isinstance(value, str):
                        raise Exception('Argument №{} must be string'.format(args.index(value) + 1))
                    if not value:
                        raise Exception('Argument №{} cannot be empty'.format(args.index(value) + 1))

                brackets = args[-2]
                if brackets not in ALL_BRACKETS:
                    raise Exception('Argument №{} is not bracket'.format(args.index(brackets) + 1))

                replace = args[-1]
                if not isinstance(replace, int):
                    raise Exception('Argument №{} must be int'.format(args.index(replace) + 1))
                if not (0 <= replace <= 1):
                    raise Exception('Argument №{} must be have value 0 or 1'.format(args.index(replace) + 1))

            except Exception, err:
                with open(path, 'a') as log_file:
                    log_file.write(err.message)
            else:
                return func(*args, **kwargs)
        return replacement_function
    return wrapper


@logger()
def replace_sub(string, new_substring, bracket, replace_all):
    res = []
    start = 0
    end = len(string)
    marker = 0

    for ich in range(len(string)):
        if string[ich] == bracket[0]:
            if marker == 0:
                end = ich
                res.append(string[start:end + 1])
                start = ich
                marker += 1
            else:
                marker += 1

        if string[ich] == bracket[-1]:
            if marker == 1:
                res.append(new_substring)
                res.append(bracket[-1])
                marker -= 1
                start = ich + 1
                end = len(string)

                if not replace_all:
                    break
            elif marker > 0:
                marker -= 1

    if start < len(string):
        res.append(string[start:end])
    return ''.join(res)


if __name__ == '__main__':
    print replace_sub('asdf as {asdf ass} asd {asd}', 'q', '{}', 0)
    print replace_sub('asdf as {asdf {ass as}s} asd {asd}', 'qqq qqq', '{}', 1)
    print replace_sub('asdf }as {asdf {ass as}s} asd {asd}', 'qqq qqq', '{}', 1)
    print replace_sub('asdf asdf {', 'qqq qqq', '{}', 0)
    print replace_sub('', 'qqq qqq', '{}', 0)