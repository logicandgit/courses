def piglatin(string):
    res = []
    list_consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J',
                      'K', 'L', 'M', 'N', 'P', 'Q', 'R',
                      'S', 'T', 'V', 'X', 'Z']
    list_word = string.split()
    for word in list_word:
        if word[0].upper() in list_consonant:
            new_w = "{}{}ay".format(word[1:], word[0])
            res.append(new_w)
        else:
            new_w = "{}way".format(word[:])
            res.append(new_w)
    return " ".join(res)

if __name__ == "__main__":
    print piglatin("asdf dfsa qwer")
