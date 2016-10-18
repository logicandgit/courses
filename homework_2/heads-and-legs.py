import math


def animals(heads, legs):
    Cows = int(math.trunc(legs/4) - (heads - math.ceil(float(legs)/float(4))))
    Chickens = int(heads - Cows)
    if ((Chickens * 2 + Cows * 4) == legs) and 0 <= Chickens and 0 <= Cows:
        return (Chickens, Cows)
    else:
        return "No solutions"

if __name__ == '__main__':
    print ('--------------------')
    # print(animals(116, 282))
    # print(animals(25, 555))
    # print(animals(0, 0))
    print(animals(12, 25))
