# -*- coding: utf-8 -*- 
class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, string):
        # ''.join(self.map2[self.map1.index(char)] if char in self.map1 else char for char in string)
        result = ''
        for char in string:
            if char in self.map1:
                result += self.map2[self.map1.index(char)]
            else:
                result += char
        return result

    def decode(self, string):
        result = ''
        for char in string:
            if char in self.map2:
                result += self.map1[self.map2.index(char)]
            else:
                result += char
        return result

if __name__ == '__main__':
    map1 = "abcdefghijklmnopqrstuvwxyz"
    map2 = "etaoinshrdlucmfwypvbgkjqxz"

    cipher = Cipher(map1, map2)
    print cipher.encode("abc.")
