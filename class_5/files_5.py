import os
import sys


def replace_sub(string, bracket, new_substring, onlyfirst=1):
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

                if onlyfirst:
                    break

            elif marker > 0:
                marker -= 1

    if start < len(string):
        res.append(string[start:end])
    return "".join(res)


def create_description_system(description_file, facts_file, outputf):
    with open(description_file) as description, open(facts_file) as facts, open(outputf, 'w') as output_file:
        info = description.readline()
        for fact in facts:
            planet, distance, unit, star = fact.split(',')
            output_file.write(info.format(first=planet, dist=distance, unit=unit, star=star))


if __name__ == '__main__':
    try:
        # if len(sys.argv) != 4:
        #     raise Exception('Need two argument, path to files')

        # description_file_path, facts_file_path, out_file_path = sys.argv[1:3]

        # if not os.path.exists(description_file_path):
        #     raise Exception('File is absent by path: {}'.format(description_file_path))

        # if not os.path.exists(facts_file_path):
        #     raise Exception('File is absent by path: {}'.format(facts_file_path))
        description_file_path = 'Description.txt'
        facts_file_path = 'facts.txt'
        out_file_path = 'Result.txt'

        create_description_system(description_file_path, facts_file_path, out_file_path)

    except Exception, err:
        print(err.message)

