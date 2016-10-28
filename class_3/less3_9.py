def replace_sub(string, bracket, new_substring, onlyfirst=1):
    res = []
    enter = 1
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

        if string[ich] == bracket[-1] and enter == 1:
            if marker == 1:
                res.append(new_substring)
                res.append(bracket[-1])
                marker -= 1
                start = ich + 1
                end = len(string)

                if onlyfirst:
                    break

            elif marker > 0:
                marker -= 1

    if start < len(string):
        res.append(string[start:end])
    return "".join(res)

if __name__ == "__main__":
    print replace_sub("asdf as {asdf ass} asd {asd}", '{}', "qqq qqq")
    print replace_sub("asdf as {asdf {ass as}s} asd {asd}", '{}', "qqq qqq", onlyfirst=0)
    print replace_sub("asdf }as {asdf {ass as}s} asd {asd}", '{}', "qqq qqq", onlyfirst=0)
    print replace_sub("asdf asdf {", '{}', "qqq qqq")
