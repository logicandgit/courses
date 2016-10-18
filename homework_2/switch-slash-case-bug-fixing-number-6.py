def eval_object(v):
    return {"+": v['a'] + v['b'],
            "-": v['a'] - v['b'],
            "/": v['a'] / v['b'],
            "*": v['a'] * v['b'],
            "%": v['a'] % v['b'],
            "**": v['a'] ** v['b']
            }.get(v['operation'], 1)

if __name__ == '__main__':
   print(eval_object({'a': 1, 'b': 1, 'operation': '+'}))
