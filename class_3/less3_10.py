def sort_words(string):
    new_list = []
    for word in string.split():
        for w in new_list:
            if len(word) < w:
                new_list.insert(0, word)
            new_list.append(word)
    return new_list


if __name__ == "__main__":
    print sort_words("asdf ds asd")
