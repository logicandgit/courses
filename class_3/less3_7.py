def min_string(string):
    return min(map(len, string.split()))

if __name__ == "__main__":
    print(min_string("asdf sdf as"))
