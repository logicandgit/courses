def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

if __name__ == '__main__':
    print(greet("asdf"))
