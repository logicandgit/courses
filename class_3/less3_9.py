def replaca_sub(string, bracket, new_substring, onlyfirst=1):
    res = []
    enter = 1
    for sub in string.split(bracket[0]):
        if sub.count(bracket[-1]) > 0 and enter == 1:
                res.append(sub.replace(sub[:sub.find(bracket[-1])], new_substring))
                res.append(bracket[0])
                if onlyfirst:
                    enter = 0
        else:
            res.append(sub)
            res.append(bracket[0])
    return "".join(res)[:-1]

if __name__ == "__main__":
    print replaca_sub("asdf as {asdf ass} asd {asd}", '{\}', "qqq qqq")
    print replaca_sub("asdf as {asdf ass} asd {asd}", '{\}', "qqq qqq", onlyfirst=0)
