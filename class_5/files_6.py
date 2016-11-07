# -*- coding: utf-8 -*-
import sys


def add_score(name, score):
    all_result = []
    names_players = []
    with open('Score.txt', 'r+') as score_file:
        for line in score_file:
            if not line:
                continue

            split_line = line.split()
            names_players.append(split_line[1])

            if name == split_line[1] and score > int(split_line[-1]):
                split_line[-1] = score

            all_result.append(split_line)

        if name not in names_players:
            all_result.append([0, name, '-', score])

        all_result.sort(key=lambda x: int(x[-1]), reverse=True)
        score_file.seek(0)
        for index in range(0, len(all_result)):
            score_file.write('{}. {} - {}\n'.format(index + 1, all_result[index][-3], all_result[index][-1]))

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise Exception('Need three arguments')

        name_player, score_player = sys.argv[1:3]

        if not isinstance(name_player, str):
            raise Exception('Name player must be string')

        if not name_player:
            raise Exception('Name player must be not empty')

        if not score_player.isdigit():
            raise Exception('Score must be integer')

        # name_player = 'ccc'
        # score_player = 124
        add_score(name_player, int(score_player))

    except Exception, err:
        print(err.message)
