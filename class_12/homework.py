# -*- coding: utf-8 -*-
import csv
import json
import yaml


class Book(object):
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return 'Book: name - "{name}", author - {author}, isbn - {isbn}'\
            .format(name=self.name, author=self.author, isbn=self.isbn)


class Library(object):

    def add(self, name, author, isbn):
        book = Book(name, author, isbn)

        # add to yaml
        with open('library.yaml', 'r') as yaml_f:
            yaml_lib = yaml.load(yaml_f)

        if not yaml_lib:
            yaml_lib = []
        if all(item.isbn != isbn for item in yaml_lib):
            yaml_lib.append(book)

            with open('library.yaml', 'w') as yaml_f:
                yaml.dump(yaml_lib, yaml_f, default_flow_style=False)

        # add to json
        with open('library.json', 'r') as json_r:
            try:
                json_lib = json.load(json_r)
            except ValueError:
                json_lib = []

        if all(item['isbn'] != isbn for item in json_lib):
            json_lib.append(book.__dict__)

            with open('library.json', 'w') as json_w:
                json.dump(json_lib, json_w, indent=4)

        # add to csv
        with open('library.csv', 'r+') as csv_f:
            csv_lib = csv.reader(csv_f)
            if all(str(isbn) != row[2] for row in csv_lib):
                csv_writer = csv.writer(csv_f)
                csv_writer.writerow([name, author, isbn])

    def remove(self, book):
        # remove to json
        with open('library.json', 'r') as json_r:
            lib = json.load(json_r)

        if lib:
            try:
                lib.remove(book.__dict__)
            except ValueError:
                print 'Book is absent'
            else:
                with open('library.json', 'w') as json_w:
                    json.dump(lib, json_w, indent=4)

    def exist(self, book):
        # exist to json
        with open('library.json', 'r') as json_r:
            lib = json.load(json_r)

        if lib:
            return lib.count(book.__dict__) == 1
        print 'Library is empty'

    def search(self, *args):
        result = []
        for dbook in self.list_book():
            if all(arg in dbook.values() for arg in args):
                result.append(dbook)
        return result

    def list_book(self):
        # list to json
        with open('library.json', 'r') as json_r:
            return json.load(json_r)

    def print_book(self):
        print self.list_book()

if __name__ == '__main__':
    mylibrary = Library()
    mylibrary.add('Fasdf Asdf', 'Asdfff', 1234567890)
    mylibrary.add('Fasdf Asdf1', 'Asdfff1', 1234567891)
    mylibrary.add('Fasdf Asdf2', 'Asdfff2', 1234567892)
    book1 = Book('Fasdf Asdf2', 'Asdfff2', 1234567892)
    mylibrary.remove(book1)
    print mylibrary.exist(book1)
    mylibrary.add('Fasdf Asdf2', 'Asdfff2', 1234567892)
    mylibrary.add('Fasdf Asdf2', 'Asdfff2', 1234567892)
    print mylibrary.exist(book1)
    print mylibrary.search('Fasdf Asdf2', 1234567890)
    print mylibrary.search('Asdfff2')
    print mylibrary.search(1234567892)
    print mylibrary.search(None)
