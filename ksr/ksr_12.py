# -*- coding: utf-8 -*-
import os
import random
import sys


def change_bank_account(name, score):
    all_result = []
    names_accounts = []
    file_accounts = 'accounts.txt'

    if not os.path.exists(file_accounts):
        open(file_accounts, 'w').close()

    try:
        with open(file_accounts, 'r+') as score_file:
            for line in score_file:
                if not line:
                    continue

                split_line = line.split('|')
                split_line[-1] = split_line[-1][:-1]  # delete \n
                names_accounts.append(split_line[1])

                if name == split_line[1]:
                    if not score:
                        return line

                    old_score = float(split_line[-1])
                    score = float(score)
                    split_line[-1] = str(old_score + score)

                all_result.append(split_line)

            score = float(score)
            if name not in names_accounts:
                if score == 0.00:
                    all_result.append([name, str(random.randrange(10 ** 10, 10 ** 11)), str(score)])
                elif not score:
                    raise Exception('No such client' + name)
                else:
                    raise Exception('Error - invalid operation')

            all_result.sort(key=lambda x: x[1])
            score_file.seek(0)

            for index in range(0, len(all_result)):
                info_account = '{}|{}|{}'.format(all_result[index][1], all_result[index][2], all_result[index][3])
                score_file.write('{}|{}\n'.format(index + 1, info_account))

        return 'Operation is finished'

    except Exception, err:
        print(err.message)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        name_account = ' '.join(sys.argv[1:-1])
        score_player = sys.argv[-1]
    else:
        name_account = ' '.join(sys.argv[1:])
        score_player = None
    # name_account = ' '.join(['fff', 'fff'])
    # score_player = None
    print change_bank_account(name_account, score_player)
    # change_bank_account(name_account, float(124))
    # change_bank_account(name_account, float(-123.5))

