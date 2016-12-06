# -*- coding: utf-8 -*- 
import csv
import yaml

# with open('login.csv', 'r') as login_file:
#     reader1 = csv.reader(login_file)
#     for line in reader1:
#         user, password, is_valid = line
#         print user, password, bool(is_valid)

# reader2 = csv.reader(open('login.csv', 'r'))
# for row in reader2:
#     print reader2.line_num
#     print row
#
# dialect = reader2.dialect
#
# for attrib in dir(dialect):
#     if not attrib.startswith('__'):
#         print attrib ,dialect.__getattribute__(attrib)

# data = [[2, True], [3, True], [12, False], [13, True]]
#
# csv_writer = csv.writer(open('prime.csv', 'w'))
# csv_writer.writerows(data

data = list(yaml.load_all(open('login.yaml')))

print data